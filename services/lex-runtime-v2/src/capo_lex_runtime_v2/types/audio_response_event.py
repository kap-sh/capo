"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#AudioResponseEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_v2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.audio_chunk
    import capo_lex_runtime_v2.types.event_id
    import capo_lex_runtime_v2.types.non_empty_string


class AudioResponseEvent(TypedDict, closed=True):
    audio_chunk: NotRequired["capo_lex_runtime_v2.types.audio_chunk.AudioChunk"]
    """<p>A chunk of the audio to play. </p>"""
    content_type: NotRequired[
        "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The encoding of the audio chunk. This is the same as the encoding configure in the <code>contentType</code> field of the <code>ConfigurationEvent</code>.</p>"""
    event_id: NotRequired["capo_lex_runtime_v2.types.event_id.EventId"]
    """<p>A unique identifier of the event sent by Amazon Lex V2. The identifier is in the form <code>RESPONSE-N</code>, where N is a number starting with one and incremented for each event sent by Amazon Lex V2 in the current session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioResponseEvent) -> dict:
    out: dict = {}
    if "audio_chunk" in value:
        import capo_lex_runtime_v2.types.audio_chunk

        out["audioChunk"] = capo_lex_runtime_v2.types.audio_chunk.serialize_json(
            value["audio_chunk"]
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> AudioResponseEvent:
    out: AudioResponseEvent = {}  # type: ignore[typeddict-item]
    if data.get("audioChunk") is not None:
        import capo_lex_runtime_v2.types.audio_chunk

        out["audio_chunk"] = capo_lex_runtime_v2.types.audio_chunk.deserialize_json(
            data["audioChunk"]
        )
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    return out


def serialize_event_json(value: AudioResponseEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "AudioResponseEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AudioResponseEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AudioResponseEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
