"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockStopEvent``."""

import json

from typing_extensions import TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agentcore.errors import DeserializationError


class HarnessContentBlockStopEvent(TypedDict, closed=True):
    content_block_index: "int"
    """<p>The index of the content block that ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockStopEvent) -> dict:
    out: dict = {}
    out["contentBlockIndex"] = value["content_block_index"]
    return out


def deserialize_json(data: dict) -> HarnessContentBlockStopEvent:
    out: HarnessContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if data.get("contentBlockIndex") is not None:
        out["content_block_index"] = data["contentBlockIndex"]
    else:
        raise DeserializationError(
            "HarnessContentBlockStopEvent.content_block_index required"
        )
    return out


def serialize_event_json(value: HarnessContentBlockStopEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "contentBlockStop",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HarnessContentBlockStopEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HarnessContentBlockStopEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
