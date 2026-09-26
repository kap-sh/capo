"""Generated from Smithy shape ``com.amazonaws.supportauthz#ThrottlingException``."""

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.supportauthz#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ThrottlingException":
        return cls(deserialize_json(data), message)
