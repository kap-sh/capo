from typing import Literal


class SupportAuthZError(Exception):
    """Base class for all SupportAuthZ service errors."""


class ServiceError(SupportAuthZError):
    """Base class for all modeled service errors.

    Args:
        fault: ``"client"`` or ``"server"``.
        is_throttling_error: Whether this error is a throttling error.
        is_retryable: Whether this error is retryable.
        code: The wire error code, or ``None``.
        message: The error message, or ``None``.
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
    ) -> None:
        super().__init__(f"{code or '<no code>'}: {message or '<no message>'}")
        self.fault = fault
        self.is_throttling_error = is_throttling_error
        self.is_retryable = is_retryable
        self.code = code
        self.message = message


class SerializationError(SupportAuthZError):
    """Raised when a value cannot be serialized."""


class DeserializationError(SupportAuthZError):
    """Raised when a value cannot be deserialized or a required member is missing."""


class UnknownServiceError(ServiceError):
    """Raised when the server returns an error code the client does not model.

    Args:
        code: ``<Code>`` text from the response body, or ``None`` if absent.
        message: ``<Message>`` text from the response body, or ``None``.
        response: The original HTTP response object, for arbitrary inspection.
    """

    def __init__(
        self, *, code: str | None, message: str | None, response: object
    ) -> None:
        _status = getattr(response, "status", 500)
        _fault: Literal["client", "server"] = "client" if _status < 500 else "server"
        _throttling = _status == 429
        _retryable = _throttling or _status >= 500
        super().__init__(
            _fault,
            is_throttling_error=_throttling,
            is_retryable=_retryable,
            code=code,
            message=message,
        )
        self.response = response


class WaiterFailedError(SupportAuthZError):
    """Raised when a waiter hits an acceptor with ``state="failure"``.

    Args:
        waiter_name: snake_case waiter name (e.g. ``bucket_exists``).
        reason: Short description of which acceptor fired.
    """

    def __init__(self, waiter_name: str, reason: str) -> None:
        super().__init__(f"waiter {waiter_name} failed: {reason}")
        self.waiter_name = waiter_name
        self.reason = reason


class WaiterTimeoutError(SupportAuthZError):
    """Raised when a waiter exhausts ``max_wait_time`` without a terminal acceptor."""

    def __init__(self, waiter_name: str, max_wait_time: float) -> None:
        super().__init__(
            f"waiter {waiter_name} timed out after {max_wait_time} seconds"
        )
        self.waiter_name = waiter_name
        self.max_wait_time = max_wait_time
