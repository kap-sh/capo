"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Trace``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_iotsitewise.types.string


class Trace(TypedDict, closed=True):
    text: NotRequired["capo_iotsitewise.types.string.String"]
    """<p>The cited text from the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> Trace:
    out: Trace = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out


def serialize_event_json(value: Trace) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "trace",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> Trace:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: Trace = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
