"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ServiceUnavailableException``."""

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError, ServiceError


class ServiceUnavailableException_(TypedDict, closed=True):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "retry_after_seconds" in value:
        out["retryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceUnavailableException_.message required")
    if data.get("retryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["retryAfterSeconds"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networksecuritymanager#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(self, data: ServiceUnavailableException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="ServiceUnavailableException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ServiceUnavailableException":
        return cls(deserialize_json(data), message)
