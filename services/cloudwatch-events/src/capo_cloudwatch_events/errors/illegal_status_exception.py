"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#IllegalStatusException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.error_message


class IllegalStatusException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch_events.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IllegalStatusException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IllegalStatusException_:
    out: IllegalStatusException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class IllegalStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchevents#IllegalStatusException``."""

    code: str | None = "IllegalStatusException"

    def __init__(
        self,
        data: IllegalStatusException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalStatusException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IllegalStatusException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
