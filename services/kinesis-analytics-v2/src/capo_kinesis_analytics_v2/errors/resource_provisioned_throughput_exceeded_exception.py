"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ResourceProvisionedThroughputExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.error_message


class ResourceProvisionedThroughputExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_analytics_v2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ResourceProvisionedThroughputExceededException_,
) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ResourceProvisionedThroughputExceededException_:
    out: ResourceProvisionedThroughputExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceProvisionedThroughputExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalyticsv2#ResourceProvisionedThroughputExceededException``."""

    code: str | None = "ResourceProvisionedThroughputExceededException"

    def __init__(
        self,
        data: ResourceProvisionedThroughputExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceProvisionedThroughputExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceProvisionedThroughputExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
