"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#FailedResourceAccessException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.error_message


class FailedResourceAccessException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_application_auto_scaling.types.error_message.ErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedResourceAccessException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedResourceAccessException_:
    out: FailedResourceAccessException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class FailedResourceAccessException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationautoscaling#FailedResourceAccessException``."""

    code: str | None = "FailedResourceAccessException"

    def __init__(
        self,
        data: FailedResourceAccessException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FailedResourceAccessException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FailedResourceAccessException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
