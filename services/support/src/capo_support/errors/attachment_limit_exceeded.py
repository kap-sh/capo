"""Generated from Smithy shape ``com.amazonaws.support#AttachmentLimitExceeded``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_support.errors import ServiceError

if TYPE_CHECKING:
    import capo_support.types.error_message


class AttachmentLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_support.types.error_message.ErrorMessage"]
    """<p>The limit for the number of attachment sets created in a short period of time has been exceeded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentLimitExceeded_:
    out: AttachmentLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class AttachmentLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#AttachmentLimitExceeded``."""

    code: str | None = "AttachmentLimitExceeded"

    def __init__(
        self,
        data: AttachmentLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AttachmentLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AttachmentLimitExceeded":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
