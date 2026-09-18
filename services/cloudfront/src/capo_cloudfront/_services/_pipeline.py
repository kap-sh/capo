from __future__ import annotations

import random
import time
from collections.abc import AsyncIterator, Iterator, Sequence
from dataclasses import dataclass
from typing import TYPE_CHECKING, Awaitable, Callable, Generic, TypeVar, cast

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

from capo_cloudfront._async import anysleep
from capo_cloudfront._body import Body
from capo_cloudfront._iter import StaticAnyIterator
from capo_cloudfront.errors import ServiceError

if TYPE_CHECKING:
    from capo_cloudfront._auth._identity import Credentials
    from capo_cloudfront._auth._providers import IdentityProvider

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


@dataclass
class OperationOptions:
    client: Client
    use_dual_stack: bool | None = None
    use_fips: bool | None = None
    endpoint: str | None = None
    region: str | None = None
    retry_max_attempts: int | None = None
    credentials_provider: IdentityProvider[Credentials] | None = None


@dataclass
class AsyncOperationOptions:
    client: AsyncClient
    use_dual_stack: bool | None = None
    use_fips: bool | None = None
    endpoint: str | None = None
    region: str | None = None
    retry_max_attempts: int | None = None
    credentials_provider: IdentityProvider[Credentials] | None = None


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
                        raise
                    is_throttling = (
                        isinstance(exc, ServiceError) and exc.is_throttling_error
                    )
                    time.sleep(_retry_delay(attempt, is_throttling))

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
                        raise
                    is_throttling = (
                        isinstance(exc, ServiceError) and exc.is_throttling_error
                    )
                    await anysleep(_retry_delay(attempt, is_throttling))

        assert last_exc
        raise last_exc

    return interceptor
