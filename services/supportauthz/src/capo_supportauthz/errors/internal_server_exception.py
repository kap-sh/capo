"""Generated from Smithy shape ``com.amazonaws.supportauthz#InternalServerException``."""

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError, ServiceError


class InternalServerException_(TypedDict, closed=True):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.supportauthz#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message)
