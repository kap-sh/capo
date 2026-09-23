"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DTMFInputEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.dtmf_regex
    import capo_lex_runtime_v2.types.epoch_millis
    import capo_lex_runtime_v2.types.event_id


class DTMFInputEvent(TypedDict, closed=True):
    input_character: "capo_lex_runtime_v2.types.dtmf_regex.DTMFRegex"
    """<p>The DTMF character that the user pressed. The allowed characters are A - D, 0 - 9, # and *.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "capo_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DTMFInputEvent) -> dict:
    out: dict = {}
    out["inputCharacter"] = value["input_character"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> DTMFInputEvent:
    out: DTMFInputEvent = {}  # type: ignore[typeddict-item]
    if data.get("inputCharacter") is not None:
        out["input_character"] = data["inputCharacter"]
    else:
        raise DeserializationError("DTMFInputEvent.input_character required")
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("clientTimestampMillis") is not None:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out


def serialize_event_json(value: DTMFInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "DTMFInputEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> DTMFInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: DTMFInputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
