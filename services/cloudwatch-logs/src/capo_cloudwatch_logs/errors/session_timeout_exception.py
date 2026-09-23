"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SessionTimeoutException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs._protocol.eventstream import HeaderValue, Message
from capo_cloudwatch_logs.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.message


class SessionTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudwatch_logs.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionTimeoutException_:
    out: SessionTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class SessionTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchlogs#SessionTimeoutException``."""

    code: str | None = "SessionTimeoutException"

    def __init__(self, data: SessionTimeoutException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionTimeoutException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "SessionTimeoutException":
        return cls(deserialize_aws_json_1_1(data), message)


def serialize_event_aws_json_1_1(value: SessionTimeoutException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "SessionTimeoutException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_1(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> SessionTimeoutException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SessionTimeoutException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_1(json.loads(payload))
    return out
