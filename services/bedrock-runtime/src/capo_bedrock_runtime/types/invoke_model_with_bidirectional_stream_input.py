"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime._iter import AnyIterator
from capo_bedrock_runtime._protocol.eventstream import Message
from capo_bedrock_runtime.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.bidirectional_input_payload_part


class _InvokeModelWithBidirectionalStreamInput_chunk(TypedDict, closed=True):
    chunk: "capo_bedrock_runtime.types.bidirectional_input_payload_part.BidirectionalInputPayloadPart"


_InvokeModelWithBidirectionalStreamInput: TypeAlias = (
    _InvokeModelWithBidirectionalStreamInput_chunk
)
InvokeModelWithBidirectionalStreamInput: TypeAlias = AnyIterator[
    _InvokeModelWithBidirectionalStreamInput
]


def serialize_event_json(value: _InvokeModelWithBidirectionalStreamInput) -> bytes:
    match value:
        case {"chunk": payload}:
            import capo_bedrock_runtime.types.bidirectional_input_payload_part

            return capo_bedrock_runtime.types.bidirectional_input_payload_part.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamInput: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message,
) -> _InvokeModelWithBidirectionalStreamInput:
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
        case "chunk":
            import capo_bedrock_runtime.types.bidirectional_input_payload_part

            return {
                "chunk": capo_bedrock_runtime.types.bidirectional_input_payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamInput: unrecognized event-type {event_type!r}"
            )
