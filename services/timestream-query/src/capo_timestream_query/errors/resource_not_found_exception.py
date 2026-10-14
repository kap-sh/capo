"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_timestream_query.errors import ServiceError

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.error_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_timestream_query.types.error_message.ErrorMessage"]
    scheduled_query_arn: NotRequired[
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the scheduled query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "scheduled_query_arn" in value:
        out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ScheduledQueryArn") is not None:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.timestreamquery#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(
        self,
        data: ResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
