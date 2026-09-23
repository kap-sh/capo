"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockDeltaEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.content_block_delta
    import capo_bedrock_runtime.types.non_negative_integer


class ContentBlockDeltaEvent(TypedDict, closed=True):
    delta: "capo_bedrock_runtime.types.content_block_delta.ContentBlockDelta"
    """<p>The delta for a content block delta event.</p>"""
    content_block_index: (
        "capo_bedrock_runtime.types.non_negative_integer.NonNegativeInteger"
    )
    """<p>The block index for a content block delta event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockDeltaEvent) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.content_block_delta

    out["delta"] = capo_bedrock_runtime.types.content_block_delta.serialize_json(
        value["delta"]
    )
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> ContentBlockDeltaEvent:
    out: ContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if data.get("delta") is not None:
        import capo_bedrock_runtime.types.content_block_delta

        out["delta"] = capo_bedrock_runtime.types.content_block_delta.deserialize_json(
            data["delta"]
        )
    else:
        raise DeserializationError("ContentBlockDeltaEvent.delta required")
    if data.get("contentBlockIndex") is not None:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "ContentBlockDeltaEvent.content_block_index required"
        )
    return out


def serialize_event_json(value: ContentBlockDeltaEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "contentBlockDelta",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ContentBlockDeltaEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
