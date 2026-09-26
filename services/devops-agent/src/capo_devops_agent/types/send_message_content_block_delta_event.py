"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContentBlockDeltaEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_devops_agent.types.send_message_content_block_delta


class SendMessageContentBlockDeltaEvent(TypedDict, closed=True):
    index: NotRequired["int"]
    """<p>Zero-based index of the content block</p>"""
    delta: NotRequired[
        "capo_devops_agent.types.send_message_content_block_delta.SendMessageContentBlockDelta"
    ]
    """<p>The incremental content delta</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContentBlockDeltaEvent) -> dict:
    out: dict = {}
    if "index" in value:
        out["index"] = value["index"]
    if "delta" in value:
        import capo_devops_agent.types.send_message_content_block_delta

        out["delta"] = (
            capo_devops_agent.types.send_message_content_block_delta.serialize_json(
                value["delta"]
            )
        )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageContentBlockDeltaEvent:
    out: SendMessageContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if data.get("index") is not None:
        out["index"] = data["index"]
    if data.get("delta") is not None:
        import capo_devops_agent.types.send_message_content_block_delta

        out["delta"] = (
            capo_devops_agent.types.send_message_content_block_delta.deserialize_json(
                data["delta"]
            )
        )
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageContentBlockDeltaEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "contentBlockDelta",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageContentBlockDeltaEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageContentBlockDeltaEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
