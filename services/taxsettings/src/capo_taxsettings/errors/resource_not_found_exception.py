"""Generated from Smithy shape ``com.amazonaws.taxsettings#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_code
    import capo_taxsettings.types.error_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"
    error_code: "capo_taxsettings.types.error_code.ErrorCode"
    """<p>404</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ResourceNotFoundException_.error_code required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ResourceNotFoundException":
        return cls(deserialize_json(data), message)


def redact_sensitive(value: ResourceNotFoundException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
