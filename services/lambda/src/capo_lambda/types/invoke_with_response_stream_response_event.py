"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamResponseEvent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda._iter import AnyIterator
from capo_lambda._protocol.eventstream import Message
from capo_lambda.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_lambda.types.invoke_response_stream_update
    import capo_lambda.types.invoke_with_response_stream_complete_event


class _InvokeWithResponseStreamResponseEvent_PayloadChunk(TypedDict, closed=True):
    PayloadChunk: (
        "capo_lambda.types.invoke_response_stream_update.InvokeResponseStreamUpdate"
    )


class _InvokeWithResponseStreamResponseEvent_InvokeComplete(TypedDict, closed=True):
    InvokeComplete: "capo_lambda.types.invoke_with_response_stream_complete_event.InvokeWithResponseStreamCompleteEvent"


_InvokeWithResponseStreamResponseEvent: TypeAlias = (
    _InvokeWithResponseStreamResponseEvent_PayloadChunk
    | _InvokeWithResponseStreamResponseEvent_InvokeComplete
)
InvokeWithResponseStreamResponseEvent: TypeAlias = AnyIterator[
    _InvokeWithResponseStreamResponseEvent
]


def serialize_event_json(value: _InvokeWithResponseStreamResponseEvent) -> bytes:
    match value:
        case {"PayloadChunk": payload}:
            import capo_lambda.types.invoke_response_stream_update

            return capo_lambda.types.invoke_response_stream_update.serialize_event_json(
                payload
            )
        case {"InvokeComplete": payload}:
            import capo_lambda.types.invoke_with_response_stream_complete_event

            return capo_lambda.types.invoke_with_response_stream_complete_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeWithResponseStreamResponseEvent: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _InvokeWithResponseStreamResponseEvent:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
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
        case "PayloadChunk":
            import capo_lambda.types.invoke_response_stream_update

            return {
                "PayloadChunk": capo_lambda.types.invoke_response_stream_update.deserialize_event_json(
                    message
                )
            }
        case "InvokeComplete":
            import capo_lambda.types.invoke_with_response_stream_complete_event

            return {
                "InvokeComplete": capo_lambda.types.invoke_with_response_stream_complete_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeWithResponseStreamResponseEvent: unrecognized event-type {event_type!r}"
            )
