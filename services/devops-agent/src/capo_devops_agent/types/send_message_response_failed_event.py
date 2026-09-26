"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponseFailedEvent``."""

import json

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent._protocol.eventstream import HeaderValue, Message


class SendMessageResponseFailedEvent(TypedDict, closed=True):
    response_id: NotRequired["str"]
    """<p>The response ID</p>"""
    error_code: NotRequired["str"]
    """<p>Error code</p>"""
    error_message: NotRequired["str"]
    """<p>Error message</p>"""
    sequence_number: NotRequired["int"]
    """<p>Event sequence number</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponseFailedEvent) -> dict:
    out: dict = {}
    if "response_id" in value:
        out["responseId"] = value["response_id"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_json(data: dict) -> SendMessageResponseFailedEvent:
    out: SendMessageResponseFailedEvent = {}  # type: ignore[typeddict-item]
    if data.get("responseId") is not None:
        out["response_id"] = data["responseId"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    return out


def serialize_event_json(value: SendMessageResponseFailedEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "responseFailed",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> SendMessageResponseFailedEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: SendMessageResponseFailedEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
