"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch_logs._iter import AnyIterator
from capo_cloudwatch_logs._protocol.eventstream import Message
from capo_cloudwatch_logs.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_cloudwatch_logs.errors.internal_streaming_exception
    import capo_cloudwatch_logs.types.fields_data


class _GetLogObjectResponseStream_fields(TypedDict, closed=True):
    fields: "capo_cloudwatch_logs.types.fields_data.FieldsData"


class _GetLogObjectResponseStream_InternalStreamingException(TypedDict, closed=True):
    InternalStreamingException: "capo_cloudwatch_logs.errors.internal_streaming_exception.InternalStreamingException_"


_GetLogObjectResponseStream: TypeAlias = (
    _GetLogObjectResponseStream_fields
    | _GetLogObjectResponseStream_InternalStreamingException
)
GetLogObjectResponseStream: TypeAlias = AnyIterator[_GetLogObjectResponseStream]


def serialize_event_aws_json_1_1(value: _GetLogObjectResponseStream) -> bytes:
    match value:
        case {"fields": payload}:
            import capo_cloudwatch_logs.types.fields_data

            return capo_cloudwatch_logs.types.fields_data.serialize_event_aws_json_1_1(
                payload
            )
        case {"InternalStreamingException": payload}:
            import capo_cloudwatch_logs.errors.internal_streaming_exception

            return capo_cloudwatch_logs.errors.internal_streaming_exception.serialize_event_aws_json_1_1(
                payload
            )
        case _:
            raise ValueError(
                f"GetLogObjectResponseStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_1(message: Message) -> _GetLogObjectResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "InternalStreamingException":
                import capo_cloudwatch_logs.errors.internal_streaming_exception

                data = capo_cloudwatch_logs.errors.internal_streaming_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_cloudwatch_logs.errors.internal_streaming_exception.InternalStreamingException(
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
        case "fields":
            import capo_cloudwatch_logs.types.fields_data

            return {
                "fields": capo_cloudwatch_logs.types.fields_data.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case _:
            raise ValueError(
                f"GetLogObjectResponseStream: unrecognized event-type {event_type!r}"
            )
