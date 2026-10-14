"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CloudTrailInvalidClientTokenIdException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class CloudTrailInvalidClientTokenIdException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudTrailInvalidClientTokenIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudTrailInvalidClientTokenIdException_:
    out: CloudTrailInvalidClientTokenIdException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CloudTrailInvalidClientTokenIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#CloudTrailInvalidClientTokenIdException``."""

    code: str | None = "CloudTrailInvalidClientTokenIdException"

    def __init__(
        self,
        data: CloudTrailInvalidClientTokenIdException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudTrailInvalidClientTokenIdException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudTrailInvalidClientTokenIdException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
