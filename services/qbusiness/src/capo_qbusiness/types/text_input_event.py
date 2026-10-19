"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextInputEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_qbusiness.types.user_message


class TextInputEvent(TypedDict, closed=True):
    user_message: "capo_qbusiness.types.user_message.UserMessage"
    """<p>A user message in a text message input event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputEvent) -> dict:
    out: dict = {}
    out["userMessage"] = value["user_message"]
    return out


def deserialize_json(data: dict) -> TextInputEvent:
    out: TextInputEvent = {}  # type: ignore[typeddict-item]
    if data.get("userMessage") is not None:
        out["user_message"] = data["userMessage"]
    else:
        out["user_message"] = ""
    return out


def serialize_event_json(value: TextInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "textEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TextInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TextInputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
