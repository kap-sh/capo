"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseCompletedEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_devops_agent.types.send_message_usage_info


class SendMessageResponseCompletedEvent(TypedDict, closed=True):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    usage: NotRequired[
        "capo_devops_agent.types.send_message_usage_info.SendMessageUsageInfo"
    ]
    """<p>Token usage information</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponseCompletedEvent) -> dict:
    out: dict = {}
    if "response_id" in value:
        out["responseId"] = value["response_id"]
    if "usage" in value:
        import capo_devops_agent.types.send_message_usage_info

        out["usage"] = capo_devops_agent.types.send_message_usage_info.serialize_json(
            value["usage"]
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseCompletedEvent:
    out: SendMessageResponseCompletedEvent = {}  # type: ignore[typeddict-item]
    if data.get("responseId") is not None:
        out["response_id"] = data["responseId"]
    if data.get("usage") is not None:
        import capo_devops_agent.types.send_message_usage_info

        out["usage"] = capo_devops_agent.types.send_message_usage_info.deserialize_json(
            data["usage"]
        )
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageResponseCompletedEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "responseCompleted",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageResponseCompletedEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageResponseCompletedEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
