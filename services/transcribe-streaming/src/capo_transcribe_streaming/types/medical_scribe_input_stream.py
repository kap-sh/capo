"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeInputStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_transcribe_streaming._iter import AnyIterator
from capo_transcribe_streaming._protocol.eventstream import Message
from capo_transcribe_streaming.errors import (
    UnknownServiceError,
)
from capo_transcribe_streaming.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_audio_event
    import capo_transcribe_streaming.types.medical_scribe_configuration_event
    import capo_transcribe_streaming.types.medical_scribe_session_control_event


class _MedicalScribeInputStream_AudioEvent(TypedDict, closed=True):
    AudioEvent: "capo_transcribe_streaming.types.medical_scribe_audio_event.MedicalScribeAudioEvent"


class _MedicalScribeInputStream_SessionControlEvent(TypedDict, closed=True):
    SessionControlEvent: "capo_transcribe_streaming.types.medical_scribe_session_control_event.MedicalScribeSessionControlEvent"


class _MedicalScribeInputStream_ConfigurationEvent(TypedDict, closed=True):
    ConfigurationEvent: "capo_transcribe_streaming.types.medical_scribe_configuration_event.MedicalScribeConfigurationEvent"


_MedicalScribeInputStream: TypeAlias = (
    _MedicalScribeInputStream_AudioEvent
    | _MedicalScribeInputStream_SessionControlEvent
    | _MedicalScribeInputStream_ConfigurationEvent
    | UnknownEvent
)
MedicalScribeInputStream: TypeAlias = AnyIterator[_MedicalScribeInputStream]


def serialize_event_json(value: _MedicalScribeInputStream) -> bytes:
    if isinstance(value, UnknownEvent):
        raise ValueError(
            f"MedicalScribeInputStream: cannot serialize unknown event {value.event_type!r}"
        )
    match value:
        case {"AudioEvent": payload}:
            import capo_transcribe_streaming.types.medical_scribe_audio_event

            return capo_transcribe_streaming.types.medical_scribe_audio_event.serialize_event_json(
                payload
            )
        case {"SessionControlEvent": payload}:
            import capo_transcribe_streaming.types.medical_scribe_session_control_event

            return capo_transcribe_streaming.types.medical_scribe_session_control_event.serialize_event_json(
                payload
            )
        case {"ConfigurationEvent": payload}:
            import capo_transcribe_streaming.types.medical_scribe_configuration_event

            return capo_transcribe_streaming.types.medical_scribe_configuration_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"MedicalScribeInputStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _MedicalScribeInputStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        raise UnknownServiceError(
            code=str(exception_type), message=None, response=response
        )
    if message_type == "error":
        error_code = headers.get(":error-code")
        error_message = headers.get(":error-message")
        raise UnknownServiceError(
            code=None if error_code is None else str(error_code),
            message=None if error_message is None else str(error_message),
            response=response,
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "AudioEvent":
            import capo_transcribe_streaming.types.medical_scribe_audio_event

            return {
                "AudioEvent": capo_transcribe_streaming.types.medical_scribe_audio_event.deserialize_event_json(
                    message
                )
            }
        case "SessionControlEvent":
            import capo_transcribe_streaming.types.medical_scribe_session_control_event

            return {
                "SessionControlEvent": capo_transcribe_streaming.types.medical_scribe_session_control_event.deserialize_event_json(
                    message
                )
            }
        case "ConfigurationEvent":
            import capo_transcribe_streaming.types.medical_scribe_configuration_event

            return {
                "ConfigurationEvent": capo_transcribe_streaming.types.medical_scribe_configuration_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return UnknownEvent(event_type, message)
        case _:
            raise ValueError(
                f"MedicalScribeInputStream: unrecognized event-type {event_type!r}"
            )
