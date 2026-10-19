"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveResponseEvent``."""

import json

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message


class AgenticRetrieveResponseEvent(TypedDict, closed=True):
    text: "str"
    """<p>The generated text chunk.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveResponseEvent) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveResponseEvent:
    out: AgenticRetrieveResponseEvent = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out


def serialize_event_json(value: AgenticRetrieveResponseEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "responseEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AgenticRetrieveResponseEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AgenticRetrieveResponseEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
