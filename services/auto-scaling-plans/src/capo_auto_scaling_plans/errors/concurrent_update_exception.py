"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ConcurrentUpdateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling_plans.errors import ServiceError

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.error_message


class ConcurrentUpdateException_(TypedDict, closed=True):
    message: NotRequired["capo_auto_scaling_plans.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConcurrentUpdateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConcurrentUpdateException_:
    out: ConcurrentUpdateException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ConcurrentUpdateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.autoscalingplans#ConcurrentUpdateException``."""

    code: str | None = "ConcurrentUpdateException"

    def __init__(
        self,
        data: ConcurrentUpdateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentUpdateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentUpdateException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
