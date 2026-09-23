"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#BadRequestException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message
from capo_transcribe_streaming.errors import ServiceError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.string


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_transcribe_streaming.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transcribestreaming#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "BadRequestException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: BadRequestException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "BadRequestException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> BadRequestException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
