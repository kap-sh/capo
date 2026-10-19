"""Generated from Smithy shape ``com.amazonaws.polly#StartSpeechSynthesisStreamActionStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_polly._iter import AnyIterator
from capo_polly._protocol.eventstream import Message
from capo_polly.errors import (
    UnknownServiceError,
)
from capo_polly.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_polly.types.close_stream_event
    import capo_polly.types.text_event


class _StartSpeechSynthesisStreamActionStream_TextEvent(TypedDict, closed=True):
    TextEvent: "capo_polly.types.text_event.TextEvent"


class _StartSpeechSynthesisStreamActionStream_CloseStreamEvent(TypedDict, closed=True):
    CloseStreamEvent: "capo_polly.types.close_stream_event.CloseStreamEvent"


_StartSpeechSynthesisStreamActionStream: TypeAlias = (
    _StartSpeechSynthesisStreamActionStream_TextEvent
    | _StartSpeechSynthesisStreamActionStream_CloseStreamEvent
    | UnknownEvent
)
StartSpeechSynthesisStreamActionStream: TypeAlias = AnyIterator[
    _StartSpeechSynthesisStreamActionStream
]


def serialize_event_json(value: _StartSpeechSynthesisStreamActionStream) -> bytes:
    if isinstance(value, UnknownEvent):
        raise ValueError(
            f"StartSpeechSynthesisStreamActionStream: cannot serialize unknown event {value.event_type!r}"
        )
    match value:
        case {"TextEvent": payload}:
            import capo_polly.types.text_event

            return capo_polly.types.text_event.serialize_event_json(payload)
        case {"CloseStreamEvent": payload}:
            import capo_polly.types.close_stream_event

            return capo_polly.types.close_stream_event.serialize_event_json(payload)
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamActionStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _StartSpeechSynthesisStreamActionStream:
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
        case "TextEvent":
            import capo_polly.types.text_event

            return {
                "TextEvent": capo_polly.types.text_event.deserialize_event_json(message)
            }
        case "CloseStreamEvent":
            import capo_polly.types.close_stream_event

            return {
                "CloseStreamEvent": capo_polly.types.close_stream_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return UnknownEvent(event_type, message)
        case _:
            raise ValueError(
                f"StartSpeechSynthesisStreamActionStream: unrecognized event-type {event_type!r}"
            )
