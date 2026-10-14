"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeOutputStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_connecthealth._iter import AnyIterator
from capo_connecthealth._protocol.eventstream import Message
from capo_connecthealth.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_connecthealth.errors.internal_server_exception
    import capo_connecthealth.errors.validation_exception
    import capo_connecthealth.types.medical_scribe_transcript_event


class _MedicalScribeOutputStream_transcriptEvent(TypedDict, closed=True):
    transcriptEvent: "capo_connecthealth.types.medical_scribe_transcript_event.MedicalScribeTranscriptEvent"


class _MedicalScribeOutputStream_internalFailureException(TypedDict, closed=True):
    internalFailureException: (
        "capo_connecthealth.errors.internal_server_exception.InternalServerException_"
    )


class _MedicalScribeOutputStream_validationException(TypedDict, closed=True):
    validationException: (
        "capo_connecthealth.errors.validation_exception.ValidationException_"
    )


_MedicalScribeOutputStream: TypeAlias = (
    _MedicalScribeOutputStream_transcriptEvent
    | _MedicalScribeOutputStream_internalFailureException
    | _MedicalScribeOutputStream_validationException
)
MedicalScribeOutputStream: TypeAlias = AnyIterator[_MedicalScribeOutputStream]


def serialize_event_json(value: _MedicalScribeOutputStream) -> bytes:
    match value:
        case {"transcriptEvent": payload}:
            import capo_connecthealth.types.medical_scribe_transcript_event

            return capo_connecthealth.types.medical_scribe_transcript_event.serialize_event_json(
                payload
            )
        case {"internalFailureException": payload}:
            import capo_connecthealth.errors.internal_server_exception

            return capo_connecthealth.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_connecthealth.errors.validation_exception

            return capo_connecthealth.errors.validation_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"MedicalScribeOutputStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _MedicalScribeOutputStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "internalFailureException":
                import capo_connecthealth.errors.internal_server_exception

                data = capo_connecthealth.errors.internal_server_exception.deserialize_event_json(
                    message
                )
                raise capo_connecthealth.errors.internal_server_exception.InternalServerException(
                    data, message=data.get("message"), response=response
                )
            case "validationException":
                import capo_connecthealth.errors.validation_exception

                data = capo_connecthealth.errors.validation_exception.deserialize_event_json(
                    message
                )
                raise capo_connecthealth.errors.validation_exception.ValidationException(
                    data, message=data.get("message"), response=response
                )
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
        case "transcriptEvent":
            import capo_connecthealth.types.medical_scribe_transcript_event

            return {
                "transcriptEvent": capo_connecthealth.types.medical_scribe_transcript_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"MedicalScribeOutputStream: unrecognized event-type {event_type!r}"
            )
