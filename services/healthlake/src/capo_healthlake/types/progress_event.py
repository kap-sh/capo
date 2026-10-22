"""Generated from Smithy shape ``com.amazonaws.healthlake#ProgressEvent``."""

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_healthlake._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_healthlake.types.agent_message_string


class ProgressEvent(TypedDict, closed=True):
    message: "capo_healthlake.types.agent_message_string.AgentMessageString"
    """<p>An incremental progress update message by the agent</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgressEvent) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgressEvent:
    out: ProgressEvent = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out


def serialize_event_aws_json_1_0(value: ProgressEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ProgressEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_0(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_0(message: Message) -> ProgressEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ProgressEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_0(json.loads(payload))
    return out


def redact_sensitive(value: ProgressEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
