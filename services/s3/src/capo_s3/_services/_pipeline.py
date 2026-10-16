from __future__ import annotations

import logging
import random
import time
from collections.abc import AsyncIterator, Iterator, Sequence
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Generic,
    TypeVar,
    cast,
)

from typing_extensions import Never
from zapros import (
    AsyncClient,
    Client,
    ConnectionError,
    ConnectTimeoutError,
    PoolTimeoutError,
    Response,
    SSLError,
    TimeoutError,
)

from capo_s3._async import anysleep
from capo_s3._aws import (
    KNOWN_RETRYABLE_CODES,
    KNOWN_RETRYABLE_STATUSES,
    KNOWN_THROTTLING_CODES,
    KNOWN_THROTTLING_STATUSES,
)
from capo_s3._body import Body
from capo_s3._iter import StaticAnyIterator
from capo_s3.errors import ServiceError, UnknownServiceError

if TYPE_CHECKING:
    from capo_s3._auth._identity import Credentials
    from capo_s3._auth._providers import IdentityProvider

logger = logging.getLogger("capo_s3.operation")

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


@dataclass
class OperationOptions:
    client: Client
    use_fips: bool | None = None
    use_dual_stack: bool | None = None
    force_path_style: bool | None = None
    accelerate: bool | None = None
    use_global_endpoint: bool | None = None
    disable_multi_region_access_points: bool | None = None
    bucket: str | None = None
    region: str | None = None
    endpoint: str | None = None
    use_object_lambda_endpoint: bool | None = None
    key: str | None = None
    prefix: str | None = None
    copy_source: str | None = None
    disable_access_points: bool | None = None
    use_arn_region: bool | None = None
    use_s3_express_control_endpoint: bool | None = None
    disable_s3_express_session_auth: bool | None = None
    retry_max_attempts: int | None = None
    credentials_provider: IdentityProvider[Credentials] | None = None
    anonymous: bool | None = None


@dataclass
class AsyncOperationOptions:
    client: AsyncClient
    use_fips: bool | None = None
    use_dual_stack: bool | None = None
    force_path_style: bool | None = None
    accelerate: bool | None = None
    use_global_endpoint: bool | None = None
    disable_multi_region_access_points: bool | None = None
    bucket: str | None = None
    region: str | None = None
    endpoint: str | None = None
    use_object_lambda_endpoint: bool | None = None
    key: str | None = None
    prefix: str | None = None
    copy_source: str | None = None
    disable_access_points: bool | None = None
    use_arn_region: bool | None = None
    use_s3_express_control_endpoint: bool | None = None
    disable_s3_express_session_auth: bool | None = None
    retry_max_attempts: int | None = None
    credentials_provider: IdentityProvider[Credentials] | None = None
    anonymous: bool | None = None


@dataclass
class OperationRequest(Generic[TInput]):
    input: TInput
    options: OperationOptions


@dataclass
class AsyncOperationRequest(Generic[TInput]):
    input: TInput
    options: AsyncOperationOptions


@dataclass
class OperationResponse(Generic[TOutput]):
    output: TOutput
    response: Response


@dataclass
class AsyncOperationResponse(Generic[TOutput]):
    output: TOutput
    response: Response


NextFn = Callable[
    [OperationRequest[TInput]],
    OperationResponse[TOutput],
]

AsyncNextFn = Callable[
    [AsyncOperationRequest[TInput]],
    Awaitable[AsyncOperationResponse[TOutput]],
]

Interceptor = Callable[
    [OperationRequest[TInput], NextFn[TInput, TOutput]],
    OperationResponse[TOutput],
]

AsyncInterceptor = Callable[
    [AsyncOperationRequest[TInput], AsyncNextFn[TInput, TOutput]],
    Awaitable[AsyncOperationResponse[TOutput]],
]


@dataclass
class OperationLogging:
    """What the logging interceptor needs to know about one operation call."""

    operation: str
    # Return a copy that is safe to log; None when the shape has nothing to hide.
    redact_input: Callable[[Any], dict[str, Any]] | None = None
    redact_output: Callable[[Any], dict[str, Any]] | None = None


def execute_pipeline(
    request: OperationRequest[TInput],
    handler: NextFn[TInput, TOutput],
    interceptors: Sequence[Interceptor[TInput, TOutput]],
) -> OperationResponse[TOutput]:
    def make_chain(index: int) -> NextFn[TInput, TOutput]:
        if index < len(interceptors):
            interceptor = interceptors[index]

            def next_fn(req: OperationRequest[TInput]) -> OperationResponse[TOutput]:
                return interceptor(req, make_chain(index + 1))

            return next_fn
        return handler

    return make_chain(0)(request)


async def aexecute_pipeline(
    request: AsyncOperationRequest[TInput],
    handler: AsyncNextFn[TInput, TOutput],
    interceptors: Sequence[AsyncInterceptor[TInput, TOutput]],
) -> AsyncOperationResponse[TOutput]:
    def make_chain(index: int) -> AsyncNextFn[TInput, TOutput]:
        if index < len(interceptors):
            interceptor = interceptors[index]

            async def next_fn(
                req: AsyncOperationRequest[TInput],
            ) -> AsyncOperationResponse[TOutput]:
                return await interceptor(req, make_chain(index + 1))

            return next_fn
        return handler

    return await make_chain(0)(request)


def raise_error(response: Response, handle_error: Callable[[Response], Never]) -> Never:
    try:
        handle_error(response)
    except ServiceError as exc:
        _apply_retry_rules(exc, response)
        raise
    except Exception as exc:
        # The error body could not be decoded (an HTML page from a proxy, a
        # truncated read): the status code is all there is to go on.
        error = UnknownServiceError(code=None, message=None, response=response)
        _apply_retry_rules(error, response)
        raise error from exc


def _apply_retry_rules(exc: ServiceError, response: Response) -> None:
    # A retry can be safe even when the error is not marked @retryable: a known
    # throttling or transient status or error code, or a Retry-After header.
    if (
        response.status in KNOWN_THROTTLING_STATUSES
        or exc.code in KNOWN_THROTTLING_CODES
    ):
        exc.is_throttling_error = True
        exc.is_retryable = True
    if (
        response.status in KNOWN_RETRYABLE_STATUSES
        or exc.code in KNOWN_RETRYABLE_CODES
        or "retry-after" in response.headers
    ):
        exc.is_retryable = True


def _is_retryable(exc: Exception) -> bool:
    if isinstance(exc, ServiceError):
        return exc.is_retryable
    if isinstance(exc, SSLError):
        return False
    if isinstance(exc, (ConnectionError, TimeoutError)):
        return True
    return False


def _is_pre_transmission(exc: Exception) -> bool:
    # True when the request body was certainly not written before the error,
    # so the same stream can be reused as-is. A bare ConnectionError is
    # ambiguous ("cannot be established or is lost"), so it does not qualify.
    return isinstance(exc, (ConnectTimeoutError, PoolTimeoutError))


def _prepare_retry(inp: object) -> bool:
    if not isinstance(inp, dict):
        return True
    for value in inp.values():
        if isinstance(value, Body):
            value = cast(Body[Iterator[bytes]], value)
            if value.rebuild() is None:
                return False
        elif isinstance(value, StaticAnyIterator):
            continue
        elif isinstance(value, (Iterator, AsyncIterator)):
            return False
    return True


async def _aprepare_retry(inp: object) -> bool:
    if not isinstance(inp, dict):
        return True
    for value in inp.values():
        if isinstance(value, Body):
            value = cast(Body[AsyncIterator[bytes]], value)
            if await value.arebuild() is None:
                return False
        elif isinstance(value, StaticAnyIterator):
            continue
        elif isinstance(value, (Iterator, AsyncIterator)):
            return False
    return True


def _retry_delay(attempt: int, is_throttling: bool) -> float:
    base = 1.0 if is_throttling else 0.5
    delay = base * (2.0 ** min(attempt - 1, 10))
    delay = min(20.0, delay)
    return random.uniform(0.0, delay)


def retry() -> Interceptor[TInput, TOutput]:
    def interceptor(
        request: OperationRequest[TInput], next: NextFn[TInput, TOutput]
    ) -> OperationResponse[TOutput]:
        max_attempts = request.options.retry_max_attempts or 3
        last_exc: Exception | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                return next(request)
            except Exception as exc:
                if not _is_retryable(exc):
                    raise
                last_exc = exc
                if attempt < max_attempts:
                    if not _is_pre_transmission(exc) and not _prepare_retry(
                        request.input
                    ):
                        logger.debug(
                            "attempt %d/%d failed: %r, not retrying because the request body cannot be replayed",
                            attempt,
                            max_attempts,
                            exc,
                            extra={
                                "attempt": attempt,
                                "max_attempts": max_attempts,
                                "error": exc,
                            },
                        )
                        raise
                    is_throttling = (
                        isinstance(exc, ServiceError) and exc.is_throttling_error
                    )
                    delay = _retry_delay(attempt, is_throttling)
                    logger.debug(
                        "attempt %d/%d failed: %r, retrying in %.2fs",
                        attempt,
                        max_attempts,
                        exc,
                        delay,
                        extra={
                            "attempt": attempt,
                            "max_attempts": max_attempts,
                            "error": exc,
                            "delay": delay,
                        },
                    )
                    time.sleep(delay)

        assert last_exc
        raise last_exc

    return interceptor


def aretry() -> AsyncInterceptor[TInput, TOutput]:
    async def interceptor(
        request: AsyncOperationRequest[TInput], next: AsyncNextFn[TInput, TOutput]
    ) -> AsyncOperationResponse[TOutput]:
        max_attempts = request.options.retry_max_attempts or 3
        last_exc: Exception | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                return await next(request)
            except Exception as exc:
                if not _is_retryable(exc):
                    raise
                last_exc = exc
                if attempt < max_attempts:
                    if not _is_pre_transmission(exc) and not await _aprepare_retry(
                        request.input
                    ):
                        logger.debug(
                            "attempt %d/%d failed: %r, not retrying because the request body cannot be replayed",
                            attempt,
                            max_attempts,
                            exc,
                            extra={
                                "attempt": attempt,
                                "max_attempts": max_attempts,
                                "error": exc,
                            },
                        )
                        raise
                    is_throttling = (
                        isinstance(exc, ServiceError) and exc.is_throttling_error
                    )
                    delay = _retry_delay(attempt, is_throttling)
                    logger.debug(
                        "attempt %d/%d failed: %r, retrying in %.2fs",
                        attempt,
                        max_attempts,
                        exc,
                        delay,
                        extra={
                            "attempt": attempt,
                            "max_attempts": max_attempts,
                            "error": exc,
                            "delay": delay,
                        },
                    )
                    await anysleep(delay)

        assert last_exc
        raise last_exc

    return interceptor


def log_operation(operation_logging: OperationLogging) -> Interceptor[TInput, TOutput]:
    operation = operation_logging.operation
    redact_input = operation_logging.redact_input
    redact_output = operation_logging.redact_output

    def interceptor(
        request: OperationRequest[TInput], next: NextFn[TInput, TOutput]
    ) -> OperationResponse[TOutput]:
        debug = logger.isEnabledFor(logging.DEBUG)
        if debug:
            input_ = (
                request.input if redact_input is None else redact_input(request.input)
            )
            logger.debug(
                "%s input: %r",
                operation,
                input_,
                extra={"operation": operation, "input": input_},
            )
        try:
            response = next(request)
        except Exception as exc:
            logger.debug(
                "%s failed: %r",
                operation,
                exc,
                extra={"operation": operation, "error": exc},
            )
            raise
        if debug:
            output = (
                response.output
                if redact_output is None
                else redact_output(response.output)
            )
            logger.debug(
                "%s output: %r",
                operation,
                output,
                extra={"operation": operation, "output": output},
            )
        return response

    return interceptor


def alog_operation(
    operation_logging: OperationLogging,
) -> AsyncInterceptor[TInput, TOutput]:
    operation = operation_logging.operation
    redact_input = operation_logging.redact_input
    redact_output = operation_logging.redact_output

    async def interceptor(
        request: AsyncOperationRequest[TInput], next: AsyncNextFn[TInput, TOutput]
    ) -> AsyncOperationResponse[TOutput]:
        debug = logger.isEnabledFor(logging.DEBUG)
        if debug:
            input_ = (
                request.input if redact_input is None else redact_input(request.input)
            )
            logger.debug(
                "%s input: %r",
                operation,
                input_,
                extra={"operation": operation, "input": input_},
            )
        try:
            response = await next(request)
        except Exception as exc:
            logger.debug(
                "%s failed: %r",
                operation,
                exc,
                extra={"operation": operation, "error": exc},
            )
            raise
        if debug:
            output = (
                response.output
                if redact_output is None
                else redact_output(response.output)
            )
            logger.debug(
                "%s output: %r",
                operation,
                output,
                extra={"operation": operation, "output": output},
            )
        return response

    return interceptor
