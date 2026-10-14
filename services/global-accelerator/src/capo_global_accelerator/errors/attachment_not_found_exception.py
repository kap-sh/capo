"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AttachmentNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import ServiceError

if TYPE_CHECKING:
    import capo_global_accelerator.types.error_message


class AttachmentNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_global_accelerator.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentNotFoundException_:
    out: AttachmentNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class AttachmentNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.globalaccelerator#AttachmentNotFoundException``."""

    code: str | None = "AttachmentNotFoundException"

    def __init__(
        self,
        data: AttachmentNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AttachmentNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
