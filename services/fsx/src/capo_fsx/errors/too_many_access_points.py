"""Generated from Smithy shape ``com.amazonaws.fsx#TooManyAccessPoints``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_code
    import capo_fsx.types.error_message


class TooManyAccessPoints_(TypedDict, closed=True):
    error_code: NotRequired["capo_fsx.types.error_code.ErrorCode"]
    """<p>An error code indicating that you have reached the maximum number of S3 access points attachments allowed for your account in this Amazon Web Services Region, or for the file system.</p>"""
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyAccessPoints_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyAccessPoints_:
    out: TooManyAccessPoints_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TooManyAccessPoints(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#TooManyAccessPoints``."""

    code: str | None = "TooManyAccessPoints"

    def __init__(
        self,
        data: TooManyAccessPoints_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyAccessPoints",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyAccessPoints":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
