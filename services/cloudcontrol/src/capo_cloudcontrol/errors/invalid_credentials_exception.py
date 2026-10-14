"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#InvalidCredentialsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.error_message


class InvalidCredentialsException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidCredentialsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidCredentialsException_:
    out: InvalidCredentialsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidCredentialsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#InvalidCredentialsException``."""

    code: str | None = "InvalidCredentialsException"

    def __init__(
        self,
        data: InvalidCredentialsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCredentialsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCredentialsException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
