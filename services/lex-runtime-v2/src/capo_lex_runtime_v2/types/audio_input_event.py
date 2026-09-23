"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#AudioInputEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message
from capo_lex_runtime_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.audio_chunk
    import capo_lex_runtime_v2.types.epoch_millis
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.non_empty_string


class AudioInputEvent(TypedDict, closed=True):
    audio_chunk: NotRequired["capo_lex_runtime_v2.types.audio_chunk.AudioChunk"]
    """<p>An encoded stream of audio.</p>"""
    content_type: "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    """<p>The encoding used for the audio chunk. You must use 8 KHz PCM 16-bit mono-channel little-endian format. The value of the field should be:</p> <p> <code>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false</code> </p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier that your application assigns to the event. You can use this to identify events in logs.</p>"""
    client_timestamp_millis: "capo_lex_runtime_v2.types.epoch_millis.EpochMillis"
    """<p>A timestamp set by the client of the date and time that the event was sent to Amazon Lex V2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioInputEvent) -> dict:
    out: dict = {}
    if "audio_chunk" in value:
        import capo_lex_runtime_v2.types.audio_chunk

        out["audioChunk"] = capo_lex_runtime_v2.types.audio_chunk.serialize_json(
            value["audio_chunk"]
        )
    out["contentType"] = value["content_type"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    out["clientTimestampMillis"] = value.get("client_timestamp_millis", 0)
    return out


def deserialize_json(data: dict) -> AudioInputEvent:
    out: AudioInputEvent = {}  # type: ignore[typeddict-item]
    if data.get("audioChunk") is not None:
        import capo_lex_runtime_v2.types.audio_chunk

        out["audio_chunk"] = capo_lex_runtime_v2.types.audio_chunk.deserialize_json(
            data["audioChunk"]
        )
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("AudioInputEvent.content_type required")
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("clientTimestampMillis") is not None:
        out["client_timestamp_millis"] = data["clientTimestampMillis"]
    else:
        out["client_timestamp_millis"] = 0
    return out


def serialize_event_json(value: AudioInputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "AudioInputEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AudioInputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AudioInputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
