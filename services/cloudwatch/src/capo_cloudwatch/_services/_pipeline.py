from __future__ import annotations

import logging
import math
import random
import threading
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

from capo_cloudwatch._async import anysleep
from capo_cloudwatch._aws import (
    KNOWN_RETRYABLE_CODES,
    KNOWN_RETRYABLE_STATUSES,
    KNOWN_THROTTLING_CODES,
    KNOWN_THROTTLING_STATUSES,
)
from capo_cloudwatch._body import Body
from capo_cloudwatch._iter import StaticAnyIterator
from capo_cloudwatch.errors import ServiceError, UnknownServiceError

if TYPE_CHECKING:
    from capo_cloudwatch._auth._identity import Credentials
    from capo_cloudwatch._auth._providers import IdentityProvider

logger = logging.getLogger("capo_cloudwatch.operation")

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class RetryQuota:
    """Retry tokens shared by all operations of one client: retries spend them, successes refund them."""

    CAPACITY: int = 500
    TRANSIENT_COST: int = 14
    THROTTLING_COST: int = 5
    NO_RETRY_INCREMENT: int = 1

    def __init__(self) -> None:
        self._available: int = self.CAPACITY

    def acquire(self, is_throttling: bool) -> int | None:
        cost = self.THROTTLING_COST if is_throttling else self.TRANSIENT_COST
        if cost > self._available:
            return None
        self._available -= cost
        return cost

    def release(self, last_retry_cost: int | None) -> None:
        refund = self.NO_RETRY_INCREMENT if last_retry_cost is None else last_retry_cost
        self._available = min(self.CAPACITY, self._available + refund)


class ThreadSafeRetryQuota(RetryQuota):
    """A ``RetryQuota`` that sync clients can share across threads."""

    def __init__(self) -> None:
        super().__init__()
        self._lock: threading.Lock = threading.Lock()

    def acquire(self, is_throttling: bool) -> int | None:
        with self._lock:
            return super().acquire(is_throttling)

    def release(self, last_retry_cost: int | None) -> None:
        with self._lock:
            super().release(last_retry_cost)


class RateLimiter:
    """Send tokens shared by all operations of one client in adaptive retry mode: the rate drops on throttling and regrows on success."""

    MIN_FILL_RATE: float = 0.5
    MIN_CAPACITY: float = 1.0
    BETA: float = 0.7
    SCALE_CONSTANT: float = 0.4
    SMOOTHING: float = 0.8
    MAX_RATE_SCALE: float = 2.0

    def __init__(self, clock: Callable[[], float] = time.monotonic) -> None:
        self._clock = clock
        now = clock()
        self._enabled: bool = False
        self._fill_rate: float = 1.0
        self._max_capacity: float = 1.0
        self._capacity: float = 0.0
        self._last_refill: float = now
        self._last_max_rate: float = 0.0
        self._last_throttle: float = now
        self._measured_rate: float = 0.0
        self._rate_bucket: float = math.floor(now)
        self._request_count: int = 0

    def acquire(self) -> float:
        """Take a send token: return 0, or the seconds to wait before asking again."""
        if not self._enabled:
            return 0.0
        self._refill(self._clock())
        if self._capacity >= 1:
            self._capacity -= 1
            return 0.0
        return (1 - self._capacity) / self._fill_rate

    def update(self, is_throttling: bool) -> None:
        """Adjust the send rate after an attempt: cut it on throttling, regrow it otherwise."""
        now = self._clock()
        self._measure(now)
        self._adjust(is_throttling, now)

    def throttled_mid_stream(self) -> None:
        """Cut the send rate for throttling reported inside an open event stream. No new request was sent, so the measured rate is left alone."""
        self._adjust(True, self._clock())

    def _adjust(self, is_throttling: bool, now: float) -> None:
        if is_throttling:
            rate = (
                min(self._measured_rate, self._fill_rate)
                if self._enabled
                else self._measured_rate
            )
            self._last_max_rate = rate
            self._last_throttle = now
            new_rate = rate * self.BETA
            self._enabled = True
        else:
            window = (self._last_max_rate * (1 - self.BETA) / self.SCALE_CONSTANT) ** (
                1 / 3
            )
            new_rate = (
                self.SCALE_CONSTANT * (now - self._last_throttle - window) ** 3
                + self._last_max_rate
            )
        self._set_rate(min(new_rate, self.MAX_RATE_SCALE * self._measured_rate), now)
        if is_throttling:
            logger.debug(
                "throttled, send rate lowered to %.2f requests/s",
                self._fill_rate,
                extra={"send_rate": self._fill_rate},
            )

    def _refill(self, now: float) -> None:
        self._capacity = min(
            self._max_capacity,
            self._capacity + (now - self._last_refill) * self._fill_rate,
        )
        self._last_refill = now

    def _measure(self, now: float) -> None:
        # Requests per second, counted in half-second buckets and smoothed.
        bucket = math.floor(now * 2) / 2
        self._request_count += 1
        if bucket > self._rate_bucket:
            current = self._request_count / (bucket - self._rate_bucket)
            self._measured_rate = current * self.SMOOTHING + self._measured_rate * (
                1 - self.SMOOTHING
            )
            self._request_count = 0
            self._rate_bucket = bucket

    def _set_rate(self, rate: float, now: float) -> None:
        self._refill(now)
        self._fill_rate = max(rate, self.MIN_FILL_RATE)
        self._max_capacity = max(rate, self.MIN_CAPACITY)
        self._capacity = min(self._capacity, self._max_capacity)


class ThreadSafeRateLimiter(RateLimiter):
    """A ``RateLimiter`` that sync clients can share across threads."""

    def __init__(self, clock: Callable[[], float] = time.monotonic) -> None:
        super().__init__(clock)
        self._lock: threading.Lock = threading.Lock()

    def acquire(self) -> float:
        with self._lock:
            return super().acquire()

    def update(self, is_throttling: bool) -> None:
        with self._lock:
            super().update(is_throttling)

    def throttled_mid_stream(self) -> None:
        with self._lock:
            super().throttled_mid_stream()


@dataclass
class OperationOptions:
    client: Client
    retry_quota: RetryQuota
    rate_limiter: RateLimiter
    use_dual_stack: bool | None = None
    use_fips: bool | None = None
    endpoint: str | None = None
    region: str | None = None
    retry_max_attempts: int | None = None
    retry_mode: str | None = None
    credentials_provider: IdentityProvider[Credentials] | None = None
    anonymous: bool | None = None


@dataclass
class AsyncOperationOptions:
    client: AsyncClient
    retry_quota: RetryQuota
    rate_limiter: RateLimiter
    use_dual_stack: bool | None = None
    use_fips: bool | None = None
    endpoint: str | None = None
    region: str | None = None
    retry_max_attempts: int | None = None
    retry_mode: str | None = None
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
        quota = request.options.retry_quota
        last_retry_cost: int | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                response = next(request)
            except Exception as exc:
                if not _is_retryable(exc) or attempt == max_attempts:
                    raise
                if not _is_pre_transmission(exc) and not _prepare_retry(request.input):
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
                cost = quota.acquire(is_throttling)
                if cost is None:
                    logger.debug(
                        "attempt %d/%d failed: %r, not retrying because the retry quota is exhausted",
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
                last_retry_cost = cost
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
            else:
                quota.release(last_retry_cost)
                return response
        raise AssertionError("unreachable")

    return interceptor


def aretry() -> AsyncInterceptor[TInput, TOutput]:
    async def interceptor(
        request: AsyncOperationRequest[TInput], next: AsyncNextFn[TInput, TOutput]
    ) -> AsyncOperationResponse[TOutput]:
        max_attempts = request.options.retry_max_attempts or 3
        quota = request.options.retry_quota
        last_retry_cost: int | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                response = await next(request)
            except Exception as exc:
                if not _is_retryable(exc) or attempt == max_attempts:
                    raise
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
                cost = quota.acquire(is_throttling)
                if cost is None:
                    logger.debug(
                        "attempt %d/%d failed: %r, not retrying because the retry quota is exhausted",
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
                last_retry_cost = cost
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
            else:
                quota.release(last_retry_cost)
                return response
        raise AssertionError("unreachable")

    return interceptor


def rate_limit() -> Interceptor[TInput, TOutput]:
    def interceptor(
        request: OperationRequest[TInput], next: NextFn[TInput, TOutput]
    ) -> OperationResponse[TOutput]:
        if request.options.retry_mode != "adaptive":
            return next(request)
        limiter = request.options.rate_limiter
        while (wait := limiter.acquire()) > 0:
            time.sleep(wait)
        try:
            response = next(request)
        except Exception as exc:
            limiter.update(isinstance(exc, ServiceError) and exc.is_throttling_error)
            raise
        limiter.update(False)
        return response

    return interceptor


def arate_limit() -> AsyncInterceptor[TInput, TOutput]:
    async def interceptor(
        request: AsyncOperationRequest[TInput], next: AsyncNextFn[TInput, TOutput]
    ) -> AsyncOperationResponse[TOutput]:
        if request.options.retry_mode != "adaptive":
            return await next(request)
        limiter = request.options.rate_limiter
        while (wait := limiter.acquire()) > 0:
            await anysleep(wait)
        try:
            response = await next(request)
        except Exception as exc:
            limiter.update(isinstance(exc, ServiceError) and exc.is_throttling_error)
            raise
        limiter.update(False)
        return response

    return interceptor


def _on_event_stream_error(
    exc: ServiceError, options: OperationOptions | AsyncOperationOptions
) -> None:
    # An error event arrives after a 200 response, so raise_error never saw it:
    # mark it by its code here. It is not retried, but adaptive mode slows down.
    _apply_retry_rules(exc, exc.response)
    if exc.is_throttling_error and options.retry_mode == "adaptive":
        options.rate_limiter.throttled_mid_stream()


def watch_event_stream(output: Any, member: str, options: OperationOptions) -> None:
    """Wrap the event stream ``output[member]`` so the errors it raises get their retry flags and reach the rate limiter."""
    if member not in output:
        return
    events = output[member]

    def watched() -> Iterator[Any]:
        try:
            yield from events
        except ServiceError as exc:
            _on_event_stream_error(exc, options)
            raise

    output[member] = watched()


def awatch_event_stream(
    output: Any, member: str, options: AsyncOperationOptions
) -> None:
    """Wrap the event stream ``output[member]`` so the errors it raises get their retry flags and reach the rate limiter."""
    if member not in output:
        return
    events = output[member]

    async def watched() -> AsyncIterator[Any]:
        try:
            async for event in events:
                yield event
        except ServiceError as exc:
            _on_event_stream_error(exc, options)
            raise

    output[member] = watched()


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
