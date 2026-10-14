"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#NotUpdatableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.error_message


class NotUpdatableException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotUpdatableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotUpdatableException_:
    out: NotUpdatableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NotUpdatableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#NotUpdatableException``."""

    code: str | None = "NotUpdatableException"

    def __init__(
        self,
        data: NotUpdatableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotUpdatableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotUpdatableException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
