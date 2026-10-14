"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidBucketNameFilterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class InvalidBucketNameFilterException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidBucketNameFilterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidBucketNameFilterException_:
    out: InvalidBucketNameFilterException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidBucketNameFilterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidBucketNameFilterException``."""

    code: str | None = "InvalidBucketNameFilterException"

    def __init__(
        self,
        data: InvalidBucketNameFilterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidBucketNameFilterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidBucketNameFilterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
