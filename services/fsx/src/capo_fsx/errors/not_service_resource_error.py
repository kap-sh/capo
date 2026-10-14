"""Generated from Smithy shape ``com.amazonaws.fsx#NotServiceResourceError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message
    import capo_fsx.types.resource_arn


class NotServiceResourceError_(TypedDict, closed=True):
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the non-Amazon FSx resource.</p>"""
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotServiceResourceError_) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotServiceResourceError_:
    out: NotServiceResourceError_ = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NotServiceResourceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#NotServiceResourceError``."""

    code: str | None = "NotServiceResourceError"

    def __init__(
        self,
        data: NotServiceResourceError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotServiceResourceError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotServiceResourceError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
