"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeInputStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_connecthealth._iter import AnyIterator
from capo_connecthealth._protocol.eventstream import Message
from capo_connecthealth.errors import (
    UnknownServiceError,
)
from capo_connecthealth.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_scribe_audio_event
    import capo_connecthealth.types.medical_scribe_binary_audio_event
    import capo_connecthealth.types.medical_scribe_configuration_event
    import capo_connecthealth.types.medical_scribe_session_control_event


class _MedicalScribeInputStream_audioEvent(TypedDict, closed=True):
    audioEvent: (
        "capo_connecthealth.types.medical_scribe_audio_event.MedicalScribeAudioEvent"
    )


class _MedicalScribeInputStream_binaryAudioEvent(TypedDict, closed=True):
    binaryAudioEvent: "capo_connecthealth.types.medical_scribe_binary_audio_event.MedicalScribeBinaryAudioEvent"


class _MedicalScribeInputStream_sessionControlEvent(TypedDict, closed=True):
    sessionControlEvent: "capo_connecthealth.types.medical_scribe_session_control_event.MedicalScribeSessionControlEvent"


class _MedicalScribeInputStream_configurationEvent(TypedDict, closed=True):
    configurationEvent: "capo_connecthealth.types.medical_scribe_configuration_event.MedicalScribeConfigurationEvent"


_MedicalScribeInputStream: TypeAlias = (
    _MedicalScribeInputStream_audioEvent
    | _MedicalScribeInputStream_binaryAudioEvent
    | _MedicalScribeInputStream_sessionControlEvent
    | _MedicalScribeInputStream_configurationEvent
    | UnknownEvent
)
MedicalScribeInputStream: TypeAlias = AnyIterator[_MedicalScribeInputStream]


def serialize_event_json(value: _MedicalScribeInputStream) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"MedicalScribeInputStream: cannot serialize unknown event {name!r}"
            )
        case {"audioEvent": payload}:
            import capo_connecthealth.types.medical_scribe_audio_event

            return capo_connecthealth.types.medical_scribe_audio_event.serialize_event_json(
                payload
            )
        case {"binaryAudioEvent": payload}:
            import capo_connecthealth.types.medical_scribe_binary_audio_event

            return capo_connecthealth.types.medical_scribe_binary_audio_event.serialize_event_json(
                payload
            )
        case {"sessionControlEvent": payload}:
            import capo_connecthealth.types.medical_scribe_session_control_event

            return capo_connecthealth.types.medical_scribe_session_control_event.serialize_event_json(
                payload
            )
        case {"configurationEvent": payload}:
            import capo_connecthealth.types.medical_scribe_configuration_event

            return capo_connecthealth.types.medical_scribe_configuration_event.serialize_event_json(
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
        case "audioEvent":
            import capo_connecthealth.types.medical_scribe_audio_event

            return {
                "audioEvent": capo_connecthealth.types.medical_scribe_audio_event.deserialize_event_json(
                    message
                )
            }
        case "binaryAudioEvent":
            import capo_connecthealth.types.medical_scribe_binary_audio_event

            return {
                "binaryAudioEvent": capo_connecthealth.types.medical_scribe_binary_audio_event.deserialize_event_json(
                    message
                )
            }
        case "sessionControlEvent":
            import capo_connecthealth.types.medical_scribe_session_control_event

            return {
                "sessionControlEvent": capo_connecthealth.types.medical_scribe_session_control_event.deserialize_event_json(
                    message
                )
            }
        case "configurationEvent":
            import capo_connecthealth.types.medical_scribe_configuration_event

            return {
                "configurationEvent": capo_connecthealth.types.medical_scribe_configuration_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(
                f"MedicalScribeInputStream: unrecognized event-type {event_type!r}"
            )
