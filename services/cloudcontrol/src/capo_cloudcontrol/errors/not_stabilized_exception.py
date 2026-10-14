"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#NotStabilizedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.error_message


class NotStabilizedException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotStabilizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotStabilizedException_:
    out: NotStabilizedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NotStabilizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#NotStabilizedException``."""

    code: str | None = "NotStabilizedException"

    def __init__(
        self,
        data: NotStabilizedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotStabilizedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotStabilizedException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
