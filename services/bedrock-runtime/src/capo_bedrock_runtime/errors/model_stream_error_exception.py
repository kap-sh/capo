"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelStreamErrorException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.non_blank_string
    import capo_bedrock_runtime.types.status_code


class ModelStreamErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock_runtime.types.non_blank_string.NonBlankString"]
    original_status_code: NotRequired[
        "capo_bedrock_runtime.types.status_code.StatusCode"
    ]
    """<p>The original status code.</p>"""
    original_message: NotRequired[
        "capo_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The original message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelStreamErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "original_status_code" in value:
        out["originalStatusCode"] = value["original_status_code"]
    if "original_message" in value:
        out["originalMessage"] = value["original_message"]
    return out


def deserialize_json(data: dict) -> ModelStreamErrorException_:
    out: ModelStreamErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("originalStatusCode") is not None:
        out["original_status_code"] = data["originalStatusCode"]
    if data.get("originalMessage") is not None:
        out["original_message"] = data["originalMessage"]
    return out


class ModelStreamErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelStreamErrorException``."""

    code: str | None = "ModelStreamErrorException"

    def __init__(self, data: ModelStreamErrorException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelStreamErrorException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ModelStreamErrorException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: ModelStreamErrorException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "modelStreamErrorException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ModelStreamErrorException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ModelStreamErrorException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
