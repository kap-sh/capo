"""Generated from Smithy shape ``com.amazonaws.clouddirectory#InvalidAttachmentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class InvalidAttachmentException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidAttachmentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidAttachmentException_:
    out: InvalidAttachmentException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidAttachmentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#InvalidAttachmentException``."""

    code: str | None = "InvalidAttachmentException"

    def __init__(
        self,
        data: InvalidAttachmentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAttachmentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidAttachmentException":
        return cls(deserialize_json(data), message, response=response)
