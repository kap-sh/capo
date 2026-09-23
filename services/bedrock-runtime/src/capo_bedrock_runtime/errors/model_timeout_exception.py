"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelTimeoutException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.non_blank_string


class ModelTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock_runtime.types.non_blank_string.NonBlankString"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ModelTimeoutException_:
    out: ModelTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ModelTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelTimeoutException``."""

    code: str | None = "ModelTimeoutException"

    def __init__(self, data: ModelTimeoutException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelTimeoutException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ModelTimeoutException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: ModelTimeoutException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "modelTimeoutException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ModelTimeoutException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ModelTimeoutException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
