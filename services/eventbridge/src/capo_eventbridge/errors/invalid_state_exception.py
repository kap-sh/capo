"""Generated from Smithy shape ``com.amazonaws.eventbridge#InvalidStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import ServiceError

if TYPE_CHECKING:
    import capo_eventbridge.types.error_message


class InvalidStateException_(TypedDict, closed=True):
    message: NotRequired["capo_eventbridge.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridge#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(
        self,
        data: InvalidStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidStateException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
