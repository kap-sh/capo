"""Generated from Smithy shape ``com.amazonaws.taxsettings#AttachmentUploadException``."""

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_message


class AttachmentUploadException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentUploadException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AttachmentUploadException_:
    out: AttachmentUploadException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AttachmentUploadException_.message required")
    return out


class AttachmentUploadException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#AttachmentUploadException``."""

    code: str | None = "AttachmentUploadException"

    def __init__(
        self,
        data: AttachmentUploadException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentUploadException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AttachmentUploadException":
        return cls(deserialize_json(data), message, response=response)


def redact_sensitive(value: AttachmentUploadException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
