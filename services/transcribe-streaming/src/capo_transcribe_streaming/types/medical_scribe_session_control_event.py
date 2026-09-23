"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeSessionControlEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message
from capo_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_session_control_event_type


class MedicalScribeSessionControlEvent(TypedDict, closed=True):
    type: "capo_transcribe_streaming.types.medical_scribe_session_control_event_type.MedicalScribeSessionControlEventType"
    r"""<p>The type of <code>MedicalScribeSessionControlEvent</code>. </p> <p>Possible Values:</p> <ul> <li> <p> <code>END_OF_SESSION</code> - Indicates the audio streaming is complete. After you send an END_OF_SESSION event, Amazon Web Services HealthScribe starts the post-stream analytics. The session can't be resumed after this event is sent. After Amazon Web Services HealthScribe processes the event, the real-time <code>StreamStatus</code> is <code>COMPLETED</code>. You get the <code>StreamStatus</code> and other stream details with the <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_GetMedicalScribeStream.html\">GetMedicalScribeStream</a> API operation. For more information about different streaming statuses, see the <code>StreamStatus</code> description in the <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeStreamDetails.html\">MedicalScribeStreamDetails</a>. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeSessionControlEvent) -> dict:
    out: dict = {}
    import capo_transcribe_streaming.types.medical_scribe_session_control_event_type

    out["Type"] = (
        capo_transcribe_streaming.types.medical_scribe_session_control_event_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeSessionControlEvent:
    out: MedicalScribeSessionControlEvent = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_transcribe_streaming.types.medical_scribe_session_control_event_type

        out["type"] = (
            capo_transcribe_streaming.types.medical_scribe_session_control_event_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("MedicalScribeSessionControlEvent.type required")
    return out


def serialize_event_json(value: MedicalScribeSessionControlEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "SessionControlEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeSessionControlEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeSessionControlEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
