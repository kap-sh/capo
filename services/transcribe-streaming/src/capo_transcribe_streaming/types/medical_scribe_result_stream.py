"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeResultStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transcribe_streaming._iter import AnyIterator
from capo_transcribe_streaming._protocol.eventstream import Message
from capo_transcribe_streaming.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_transcribe_streaming.errors.bad_request_exception
    import capo_transcribe_streaming.errors.conflict_exception
    import capo_transcribe_streaming.errors.internal_failure_exception
    import capo_transcribe_streaming.errors.limit_exceeded_exception
    import capo_transcribe_streaming.errors.service_unavailable_exception
    import capo_transcribe_streaming.types.medical_scribe_transcript_event


class _MedicalScribeResultStream_TranscriptEvent(TypedDict, closed=True):
    TranscriptEvent: "capo_transcribe_streaming.types.medical_scribe_transcript_event.MedicalScribeTranscriptEvent"


class _MedicalScribeResultStream_BadRequestException(TypedDict, closed=True):
    BadRequestException: (
        "capo_transcribe_streaming.errors.bad_request_exception.BadRequestException_"
    )


class _MedicalScribeResultStream_LimitExceededException(TypedDict, closed=True):
    LimitExceededException: "capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException_"


class _MedicalScribeResultStream_InternalFailureException(TypedDict, closed=True):
    InternalFailureException: "capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException_"


class _MedicalScribeResultStream_ConflictException(TypedDict, closed=True):
    ConflictException: (
        "capo_transcribe_streaming.errors.conflict_exception.ConflictException_"
    )


class _MedicalScribeResultStream_ServiceUnavailableException(TypedDict, closed=True):
    ServiceUnavailableException: "capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException_"


_MedicalScribeResultStream: TypeAlias = (
    _MedicalScribeResultStream_TranscriptEvent
    | _MedicalScribeResultStream_BadRequestException
    | _MedicalScribeResultStream_LimitExceededException
    | _MedicalScribeResultStream_InternalFailureException
    | _MedicalScribeResultStream_ConflictException
    | _MedicalScribeResultStream_ServiceUnavailableException
)
MedicalScribeResultStream: TypeAlias = AnyIterator[_MedicalScribeResultStream]


def serialize_event_json(value: _MedicalScribeResultStream) -> bytes:
    match value:
        case {"TranscriptEvent": payload}:
            import capo_transcribe_streaming.types.medical_scribe_transcript_event

            return capo_transcribe_streaming.types.medical_scribe_transcript_event.serialize_event_json(
                payload
            )
        case {"BadRequestException": payload}:
            import capo_transcribe_streaming.errors.bad_request_exception

            return capo_transcribe_streaming.errors.bad_request_exception.serialize_event_json(
                payload
            )
        case {"LimitExceededException": payload}:
            import capo_transcribe_streaming.errors.limit_exceeded_exception

            return capo_transcribe_streaming.errors.limit_exceeded_exception.serialize_event_json(
                payload
            )
        case {"InternalFailureException": payload}:
            import capo_transcribe_streaming.errors.internal_failure_exception

            return capo_transcribe_streaming.errors.internal_failure_exception.serialize_event_json(
                payload
            )
        case {"ConflictException": payload}:
            import capo_transcribe_streaming.errors.conflict_exception

            return capo_transcribe_streaming.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"ServiceUnavailableException": payload}:
            import capo_transcribe_streaming.errors.service_unavailable_exception

            return capo_transcribe_streaming.errors.service_unavailable_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"MedicalScribeResultStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _MedicalScribeResultStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "BadRequestException":
                import capo_transcribe_streaming.errors.bad_request_exception

                data = capo_transcribe_streaming.errors.bad_request_exception.deserialize_event_json(
                    message
                )
                raise capo_transcribe_streaming.errors.bad_request_exception.BadRequestException(
                    data, message=data.get("message")
                )
            case "LimitExceededException":
                import capo_transcribe_streaming.errors.limit_exceeded_exception

                data = capo_transcribe_streaming.errors.limit_exceeded_exception.deserialize_event_json(
                    message
                )
                raise capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException(
                    data, message=data.get("message")
                )
            case "InternalFailureException":
                import capo_transcribe_streaming.errors.internal_failure_exception

                data = capo_transcribe_streaming.errors.internal_failure_exception.deserialize_event_json(
                    message
                )
                raise capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException(
                    data, message=data.get("message")
                )
            case "ConflictException":
                import capo_transcribe_streaming.errors.conflict_exception

                data = capo_transcribe_streaming.errors.conflict_exception.deserialize_event_json(
                    message
                )
                raise capo_transcribe_streaming.errors.conflict_exception.ConflictException(
                    data, message=data.get("message")
                )
            case "ServiceUnavailableException":
                import capo_transcribe_streaming.errors.service_unavailable_exception

                data = capo_transcribe_streaming.errors.service_unavailable_exception.deserialize_event_json(
                    message
                )
                raise capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException(
                    data, message=data.get("message")
                )
        raise UnknownServiceError(
            code=str(exception_type), message=None, response=message
        )
    if message_type == "error":
        error_code = headers.get(":error-code")
        error_message = headers.get(":error-message")
        raise UnknownServiceError(
            code=None if error_code is None else str(error_code),
            message=None if error_message is None else str(error_message),
            response=message,
        )
    event_type = headers.get(":event-type")
    match event_type:
        case "TranscriptEvent":
            import capo_transcribe_streaming.types.medical_scribe_transcript_event

            return {
                "TranscriptEvent": capo_transcribe_streaming.types.medical_scribe_transcript_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"MedicalScribeResultStream: unrecognized event-type {event_type!r}"
            )
