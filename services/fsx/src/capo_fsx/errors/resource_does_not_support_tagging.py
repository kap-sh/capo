"""Generated from Smithy shape ``com.amazonaws.fsx#ResourceDoesNotSupportTagging``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message
    import capo_fsx.types.resource_arn


class ResourceDoesNotSupportTagging_(TypedDict, closed=True):
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the resource that doesn't support tagging.</p>"""
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDoesNotSupportTagging_) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDoesNotSupportTagging_:
    out: ResourceDoesNotSupportTagging_ = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceDoesNotSupportTagging(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#ResourceDoesNotSupportTagging``."""

    code: str | None = "ResourceDoesNotSupportTagging"

    def __init__(
        self,
        data: ResourceDoesNotSupportTagging_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDoesNotSupportTagging",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceDoesNotSupportTagging":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
