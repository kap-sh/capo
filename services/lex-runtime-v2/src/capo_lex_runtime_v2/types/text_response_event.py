"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#TextResponseEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.messages


class TextResponseEvent(TypedDict, closed=True):
    messages: NotRequired["capo_lex_runtime_v2.types.messages.Messages"]
    """<p>A list of messages to send to the user. Messages are ordered based on the order that you returned the messages from your Lambda function or the order that the messages are defined in the bot.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextResponseEvent) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.serialize_json(
            value["messages"]
        )
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> TextResponseEvent:
    out: TextResponseEvent = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_lex_runtime_v2.types.messages

        out["messages"] = capo_lex_runtime_v2.types.messages.deserialize_json(
            data["messages"]
        )
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    return out


def serialize_event_json(value: TextResponseEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "TextResponseEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TextResponseEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TextResponseEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
