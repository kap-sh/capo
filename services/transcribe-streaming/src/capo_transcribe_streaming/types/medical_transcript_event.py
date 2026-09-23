"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalTranscriptEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_transcript


class MedicalTranscriptEvent(TypedDict, closed=True):
    transcript: NotRequired[
        "capo_transcribe_streaming.types.medical_transcript.MedicalTranscript"
    ]
    """<p>Contains <code>Results</code>, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalTranscriptEvent) -> dict:
    out: dict = {}
    if "transcript" in value:
        import capo_transcribe_streaming.types.medical_transcript

        out["Transcript"] = (
            capo_transcribe_streaming.types.medical_transcript.serialize_json(
                value["transcript"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalTranscriptEvent:
    out: MedicalTranscriptEvent = {}  # type: ignore[typeddict-item]
    if data.get("Transcript") is not None:
        import capo_transcribe_streaming.types.medical_transcript

        out["transcript"] = (
            capo_transcribe_streaming.types.medical_transcript.deserialize_json(
                data["Transcript"]
            )
        )
    return out


def serialize_event_json(value: MedicalTranscriptEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "TranscriptEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalTranscriptEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalTranscriptEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
