"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageHeartbeatEvent``."""

import json

from typing_extensions import TypedDict

from capo_devops_agent._protocol.eventstream import HeaderValue, Message


class SendMessageHeartbeatEvent(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageHeartbeatEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendMessageHeartbeatEvent:
    out: SendMessageHeartbeatEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: SendMessageHeartbeatEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "heartbeat",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageHeartbeatEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageHeartbeatEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
