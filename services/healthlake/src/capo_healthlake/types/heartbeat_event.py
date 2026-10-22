"""Generated from Smithy shape ``com.amazonaws.healthlake#HeartbeatEvent``."""

import json

from typing_extensions import TypedDict

from capo_healthlake._protocol.eventstream import HeaderValue, Message


class HeartbeatEvent(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HeartbeatEvent) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> HeartbeatEvent:
    out: HeartbeatEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_aws_json_1_0(value: HeartbeatEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "HeartbeatEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_0(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_0(message: Message) -> HeartbeatEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HeartbeatEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_0(json.loads(payload))
    return out
