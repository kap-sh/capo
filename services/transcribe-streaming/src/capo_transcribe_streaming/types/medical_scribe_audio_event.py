"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeAudioEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.audio_chunk


class MedicalScribeAudioEvent(TypedDict, closed=True):
    audio_chunk: "capo_transcribe_streaming.types.audio_chunk.AudioChunk"
    r"""<p> An audio blob containing the next segment of audio from your application, with a maximum duration of 1 second. The maximum size in bytes varies based on audio properties. </p> <p>Find recommended size in <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#best-practices\">Transcribing streaming best practices</a>. </p> <p> Size calculation: <code>Duration (s) * Sample Rate (Hz) * Number of Channels * 2 (Bytes per Sample)</code> </p> <p> For example, a 1-second chunk of 16 kHz, 2-channel, 16-bit audio would be <code>1 * 16000 * 2 * 2 = 64000 bytes</code>. </p> <p> For 8 kHz, 1-channel, 16-bit audio, a 1-second chunk would be <code>1 * 8000 * 1 * 2 = 16000 bytes</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeAudioEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> MedicalScribeAudioEvent:
    out: MedicalScribeAudioEvent = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: MedicalScribeAudioEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "AudioEvent",
        ":content-type": "application/octet-stream",
    }
    payload = b""
    payload = value["audio_chunk"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeAudioEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeAudioEvent = {}  # type: ignore[typeddict-item]
    out["audio_chunk"] = payload
    return out
