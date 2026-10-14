from typing import Literal

from zapros import Response


class S3Error(Exception):
    """Base class for all S3 service errors."""


class ServiceError(S3Error):
    """Base class for all modeled service errors.

    Args:
        fault: ``"client"`` or ``"server"``.
        is_throttling_error: Whether this error is a throttling error.
        is_retryable: Whether this error is retryable.
        code: The wire error code, or ``None``.
        message: The error message, or ``None``.
        response: The HTTP response the error was read from.
    """

    code: str | None = None

    def __init__(
        self,
        fault: Literal["client", "server"],
        *,
        is_throttling_error: bool,
        is_retryable: bool,
        code: str | None = None,
        message: str | None = None,
        response: Response,
    ) -> None:
        super().__init__(f"{code or '<no code>'}: {message or '<no message>'}")
        self.fault = fault
        self.is_throttling_error = is_throttling_error
        self.is_retryable = is_retryable
        self.code = code
        self.message = message
        self.response = response


class SerializationError(S3Error):
    """Raised when a value cannot be serialized."""


class DeserializationError(S3Error):
    """Raised when a value cannot be deserialized or a required member is missing."""


class UnknownServiceError(ServiceError):
    """Raised when the server returns an error code the client does not model.

    Args:
        code: ``<Code>`` text from the response body, or ``None`` if absent.
        message: ``<Message>`` text from the response body, or ``None``.
        response: The original HTTP response object, for arbitrary inspection.
    """

    def __init__(
        self, *, code: str | None, message: str | None, response: Response
    ) -> None:
        _status = response.status
        _fault: Literal["client", "server"] = "client" if _status < 500 else "server"
        _throttling = _status == 429
        _retryable = _throttling or _status >= 500
        super().__init__(
            _fault,
            is_throttling_error=_throttling,
            is_retryable=_retryable,
            code=code,
            message=message,
            response=response,
        )


class WaiterFailedError(S3Error):
    """Raised when a waiter hits an acceptor with ``state="failure"``.

    Args:
        waiter_name: snake_case waiter name (e.g. ``bucket_exists``).
        reason: Short description of which acceptor fired.
    """

    def __init__(self, waiter_name: str, reason: str) -> None:
        super().__init__(f"waiter {waiter_name} failed: {reason}")
        self.waiter_name = waiter_name
        self.reason = reason


class WaiterTimeoutError(S3Error):
    """Raised when a waiter exhausts ``max_wait_time`` without a terminal acceptor."""

    def __init__(self, waiter_name: str, max_wait_time: float) -> None:
        super().__init__(
            f"waiter {waiter_name} timed out after {max_wait_time} seconds"
        )
        self.waiter_name = waiter_name
        self.max_wait_time = max_wait_time


class ChecksumUnavailable(S3Error):
    """An algorithm whose backing package is not installed."""


class ChecksumMismatch(S3Error):
    """A response body did not match the checksum the service sent."""

    def __init__(self, algorithm: str, expected: str, actual: str) -> None:
        super().__init__(
            f"{algorithm} checksum mismatch: expected {expected}, got {actual}"
        )
        self.algorithm = algorithm
        self.expected = expected
        self.actual = actual
