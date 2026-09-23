"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockStartEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_content_block_start


class HarnessContentBlockStartEvent(TypedDict, closed=True):
    content_block_index: "int"
    """<p>The index of the content block within the message.</p>"""
    start: "capo_bedrock_agentcore.types.harness_content_block_start.HarnessContentBlockStart"
    """<p>The content block start payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockStartEvent) -> dict:
    out: dict = {}
    out["contentBlockIndex"] = value["content_block_index"]
    import capo_bedrock_agentcore.types.harness_content_block_start

    out["start"] = (
        capo_bedrock_agentcore.types.harness_content_block_start.serialize_json(
            value["start"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessContentBlockStartEvent:
    out: HarnessContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    if data.get("contentBlockIndex") is not None:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "HarnessContentBlockStartEvent.content_block_index required"
        )
    if data.get("start") is not None:
        import capo_bedrock_agentcore.types.harness_content_block_start

        out["start"] = (
            capo_bedrock_agentcore.types.harness_content_block_start.deserialize_json(
                data["start"]
            )
        )
    else:
        raise DeserializationError("HarnessContentBlockStartEvent.start required")
    return out


def serialize_event_json(value: HarnessContentBlockStartEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "contentBlockStart",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HarnessContentBlockStartEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HarnessContentBlockStartEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
