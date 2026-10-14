"""Generated from Smithy shape ``com.amazonaws.support#AttachmentSetSizeLimitExceeded``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_support.errors import ServiceError

if TYPE_CHECKING:
    import capo_support.types.error_message


class AttachmentSetSizeLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_support.types.error_message.ErrorMessage"]
    """<p>A limit for the size of an attachment set has been exceeded. The limits are three attachments and 5 MB per attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentSetSizeLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentSetSizeLimitExceeded_:
    out: AttachmentSetSizeLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AttachmentSetSizeLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#AttachmentSetSizeLimitExceeded``."""

    code: str | None = "AttachmentSetSizeLimitExceeded"

    def __init__(
        self,
        data: AttachmentSetSizeLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentSetSizeLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AttachmentSetSizeLimitExceeded":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
