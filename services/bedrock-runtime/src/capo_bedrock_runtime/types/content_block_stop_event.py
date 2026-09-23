"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockStopEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.non_negative_integer


class ContentBlockStopEvent(TypedDict, closed=True):
    content_block_index: (
        "capo_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The index for a content block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockStopEvent) -> dict:
    out: dict = {}
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockStopEvent:
    out: ContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if data.get("contentBlockIndex") is not None:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError("ContentBlockStopEvent.content_block_index required")
    return out


def serialize_event_json(value: ContentBlockStopEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "contentBlockStop",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ContentBlockStopEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
