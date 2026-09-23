"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateOutputEvent``."""

import json

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import DeserializationError


class RetrieveAndGenerateOutputEvent(TypedDict, closed=True):
    text: "str"
    """<p>A text response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateOutputEvent) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateOutputEvent:
    out: RetrieveAndGenerateOutputEvent = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        raise DeserializationError("RetrieveAndGenerateOutputEvent.text required")
    return out


def serialize_event_json(value: RetrieveAndGenerateOutputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "output",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> RetrieveAndGenerateOutputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: RetrieveAndGenerateOutputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
