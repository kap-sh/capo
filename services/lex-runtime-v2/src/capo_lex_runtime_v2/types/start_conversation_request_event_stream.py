"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationRequestEventStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_lex_runtime_v2._iter import AnyIterator
from capo_lex_runtime_v2._protocol.eventstream import Message
from capo_lex_runtime_v2.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.audio_input_event
    import capo_lex_runtime_v2.types.configuration_event
    import capo_lex_runtime_v2.types.disconnection_event
    import capo_lex_runtime_v2.types.dtmf_input_event
    import capo_lex_runtime_v2.types.playback_completion_event
    import capo_lex_runtime_v2.types.text_input_event


class _StartConversationRequestEventStream_ConfigurationEvent(TypedDict, closed=True):
    ConfigurationEvent: (
        "capo_lex_runtime_v2.types.configuration_event.ConfigurationEvent"
    )


class _StartConversationRequestEventStream_AudioInputEvent(TypedDict, closed=True):
    AudioInputEvent: "capo_lex_runtime_v2.types.audio_input_event.AudioInputEvent"


class _StartConversationRequestEventStream_DTMFInputEvent(TypedDict, closed=True):
    DTMFInputEvent: "capo_lex_runtime_v2.types.dtmf_input_event.DTMFInputEvent"


class _StartConversationRequestEventStream_TextInputEvent(TypedDict, closed=True):
    TextInputEvent: "capo_lex_runtime_v2.types.text_input_event.TextInputEvent"


class _StartConversationRequestEventStream_PlaybackCompletionEvent(
    TypedDict, closed=True
):
    PlaybackCompletionEvent: (
        "capo_lex_runtime_v2.types.playback_completion_event.PlaybackCompletionEvent"
    )


class _StartConversationRequestEventStream_DisconnectionEvent(TypedDict, closed=True):
    DisconnectionEvent: (
        "capo_lex_runtime_v2.types.disconnection_event.DisconnectionEvent"
    )


_StartConversationRequestEventStream: TypeAlias = (
    _StartConversationRequestEventStream_ConfigurationEvent
    | _StartConversationRequestEventStream_AudioInputEvent
    | _StartConversationRequestEventStream_DTMFInputEvent
    | _StartConversationRequestEventStream_TextInputEvent
    | _StartConversationRequestEventStream_PlaybackCompletionEvent
    | _StartConversationRequestEventStream_DisconnectionEvent
)
StartConversationRequestEventStream: TypeAlias = AnyIterator[
    _StartConversationRequestEventStream
]


def serialize_event_json(value: _StartConversationRequestEventStream) -> bytes:
    match value:
        case {"ConfigurationEvent": payload}:
            import capo_lex_runtime_v2.types.configuration_event

            return capo_lex_runtime_v2.types.configuration_event.serialize_event_json(
                payload
            )
        case {"AudioInputEvent": payload}:
            import capo_lex_runtime_v2.types.audio_input_event

            return capo_lex_runtime_v2.types.audio_input_event.serialize_event_json(
                payload
            )
        case {"DTMFInputEvent": payload}:
            import capo_lex_runtime_v2.types.dtmf_input_event

            return capo_lex_runtime_v2.types.dtmf_input_event.serialize_event_json(
                payload
            )
        case {"TextInputEvent": payload}:
            import capo_lex_runtime_v2.types.text_input_event

            return capo_lex_runtime_v2.types.text_input_event.serialize_event_json(
                payload
            )
        case {"PlaybackCompletionEvent": payload}:
            import capo_lex_runtime_v2.types.playback_completion_event

            return capo_lex_runtime_v2.types.playback_completion_event.serialize_event_json(
                payload
            )
        case {"DisconnectionEvent": payload}:
            import capo_lex_runtime_v2.types.disconnection_event

            return capo_lex_runtime_v2.types.disconnection_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"StartConversationRequestEventStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _StartConversationRequestEventStream:
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
        case "ConfigurationEvent":
            import capo_lex_runtime_v2.types.configuration_event

            return {
                "ConfigurationEvent": capo_lex_runtime_v2.types.configuration_event.deserialize_event_json(
                    message
                )
            }
        case "AudioInputEvent":
            import capo_lex_runtime_v2.types.audio_input_event

            return {
                "AudioInputEvent": capo_lex_runtime_v2.types.audio_input_event.deserialize_event_json(
                    message
                )
            }
        case "DTMFInputEvent":
            import capo_lex_runtime_v2.types.dtmf_input_event

            return {
                "DTMFInputEvent": capo_lex_runtime_v2.types.dtmf_input_event.deserialize_event_json(
                    message
                )
            }
        case "TextInputEvent":
            import capo_lex_runtime_v2.types.text_input_event

            return {
                "TextInputEvent": capo_lex_runtime_v2.types.text_input_event.deserialize_event_json(
                    message
                )
            }
        case "PlaybackCompletionEvent":
            import capo_lex_runtime_v2.types.playback_completion_event

            return {
                "PlaybackCompletionEvent": capo_lex_runtime_v2.types.playback_completion_event.deserialize_event_json(
                    message
                )
            }
        case "DisconnectionEvent":
            import capo_lex_runtime_v2.types.disconnection_event

            return {
                "DisconnectionEvent": capo_lex_runtime_v2.types.disconnection_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartConversationRequestEventStream: unrecognized event-type {event_type!r}"
            )
