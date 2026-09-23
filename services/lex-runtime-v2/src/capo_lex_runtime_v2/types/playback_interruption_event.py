"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PlaybackInterruptionEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.playback_interruption_reason


class PlaybackInterruptionEvent(TypedDict, closed=True):
    event_reason: NotRequired[
        "capo_lex_runtime_v2.types.playback_interruption_reason.PlaybackInterruptionReason"
    ]
    """<p>Indicates the type of user input that Amazon Lex V2 detected.</p>"""
    caused_by_event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>The identifier of the event that contained the audio, DTMF, or text that caused the interruption.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackInterruptionEvent) -> dict:
    out: dict = {}
    if "event_reason" in value:
        import capo_lex_runtime_v2.types.playback_interruption_reason

        out["eventReason"] = (
            capo_lex_runtime_v2.types.playback_interruption_reason.serialize_json(
                value["event_reason"]
            )
        )
    if "caused_by_event_id" in value:
        out["causedByEventId"] = value["caused_by_event_id"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> PlaybackInterruptionEvent:
    out: PlaybackInterruptionEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventReason") is not None:
        import capo_lex_runtime_v2.types.playback_interruption_reason

        out["event_reason"] = (
            capo_lex_runtime_v2.types.playback_interruption_reason.deserialize_json(
                data["eventReason"]
            )
        )
    if data.get("causedByEventId") is not None:
        out["caused_by_event_id"] = data["causedByEventId"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    return out


def serialize_event_json(value: PlaybackInterruptionEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "PlaybackInterruptionEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> PlaybackInterruptionEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: PlaybackInterruptionEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
