"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockStartEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.content_block_start
    import capo_bedrock_runtime.types.non_negative_integer


class ContentBlockStartEvent(TypedDict, closed=True):
    start: "capo_bedrock_runtime.types.content_block_start.ContentBlockStart"
    """<p>Start information about a content block start event. </p>"""
    content_block_index: (
        "capo_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The index for a content block start event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockStartEvent) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.content_block_start

    out["start"] = capo_bedrock_runtime.types.content_block_start.serialize_json(
        value["start"]
    )
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockStartEvent:
    out: ContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    if data.get("start") is not None:
        import capo_bedrock_runtime.types.content_block_start

        out["start"] = capo_bedrock_runtime.types.content_block_start.deserialize_json(
            data["start"]
        )
    else:
        raise DeserializationError("ContentBlockStartEvent.start required")
    if data.get("contentBlockIndex") is not None:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "ContentBlockStartEvent.content_block_index required"
        )
    return out


def serialize_event_json(value: ContentBlockStartEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "contentBlockStart",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ContentBlockStartEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
