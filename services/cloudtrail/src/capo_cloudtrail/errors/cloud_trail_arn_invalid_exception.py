"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CloudTrailARNInvalidException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class CloudTrailARNInvalidException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudTrailARNInvalidException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudTrailARNInvalidException_:
    out: CloudTrailARNInvalidException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CloudTrailARNInvalidException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#CloudTrailARNInvalidException``."""

    code: str | None = "CloudTrailARNInvalidException"

    def __init__(
        self,
        data: CloudTrailARNInvalidException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudTrailARNInvalidException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudTrailARNInvalidException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
