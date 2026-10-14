"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ClientTokenConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudcontrol.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudcontrol.types.error_message


class ClientTokenConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudcontrol.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClientTokenConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ClientTokenConflictException_:
    out: ClientTokenConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ClientTokenConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudcontrol#ClientTokenConflictException``."""

    code: str | None = "ClientTokenConflictException"

    def __init__(
        self,
        data: ClientTokenConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClientTokenConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ClientTokenConflictException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
