"""Generated from Smithy shape ``com.amazonaws.support#AttachmentSetExpired``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_support.errors import ServiceError

if TYPE_CHECKING:
    import capo_support.types.error_message


class AttachmentSetExpired_(TypedDict, closed=True):
    message: NotRequired["capo_support.types.error_message.ErrorMessage"]
    """<p>The expiration time of the attachment set has passed. The set expires one hour after it is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentSetExpired_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentSetExpired_:
    out: AttachmentSetExpired_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AttachmentSetExpired(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#AttachmentSetExpired``."""

    code: str | None = "AttachmentSetExpired"

    def __init__(
        self,
        data: AttachmentSetExpired_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentSetExpired",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AttachmentSetExpired":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
