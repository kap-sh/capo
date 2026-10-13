"""Generated from Smithy shape ``com.amazonaws.proton#AccessDeniedException``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_proton.types.error_message


class AccessDeniedException_(TypedDict, closed=True):
    message: "capo_proton.types.error_message.ErrorMessage"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.proton#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data), message)


def redact_sensitive(value: AccessDeniedException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
