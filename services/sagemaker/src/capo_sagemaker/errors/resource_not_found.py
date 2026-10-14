"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceNotFound``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker.errors import ServiceError

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason


class ResourceNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFound_:
    out: ResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemaker#ResourceNotFound``."""

    code: str | None = "ResourceNotFound"

    def __init__(
        self,
        data: ResourceNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFound":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
