"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentOutputMessageStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_healthlake._iter import AnyIterator
from capo_healthlake._protocol.eventstream import Message
from capo_healthlake.errors import (
    UnknownServiceError,
)
from capo_healthlake.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_healthlake.types.end_of_output_event
    import capo_healthlake.types.error_event
    import capo_healthlake.types.heartbeat_event
    import capo_healthlake.types.progress_event
    import capo_healthlake.types.text_message_event


class _AgentOutputMessageStream_TextMessageEvent(TypedDict, closed=True):
    TextMessageEvent: "capo_healthlake.types.text_message_event.TextMessageEvent"


class _AgentOutputMessageStream_ProgressEvent(TypedDict, closed=True):
    ProgressEvent: "capo_healthlake.types.progress_event.ProgressEvent"


class _AgentOutputMessageStream_HeartbeatEvent(TypedDict, closed=True):
    HeartbeatEvent: "capo_healthlake.types.heartbeat_event.HeartbeatEvent"


class _AgentOutputMessageStream_ErrorEvent(TypedDict, closed=True):
    ErrorEvent: "capo_healthlake.types.error_event.ErrorEvent"


class _AgentOutputMessageStream_EndOfOutputEvent(TypedDict, closed=True):
    EndOfOutputEvent: "capo_healthlake.types.end_of_output_event.EndOfOutputEvent"


_AgentOutputMessageStream: TypeAlias = (
    _AgentOutputMessageStream_TextMessageEvent
    | _AgentOutputMessageStream_ProgressEvent
    | _AgentOutputMessageStream_HeartbeatEvent
    | _AgentOutputMessageStream_ErrorEvent
    | _AgentOutputMessageStream_EndOfOutputEvent
    | UnknownEvent
)
AgentOutputMessageStream: TypeAlias = AnyIterator[_AgentOutputMessageStream]


def serialize_event_aws_json_1_0(value: _AgentOutputMessageStream) -> bytes:
    if isinstance(value, UnknownEvent):
        raise ValueError(
            f"AgentOutputMessageStream: cannot serialize unknown event {value.event_type!r}"
        )
    match value:
        case {"TextMessageEvent": payload}:
            import capo_healthlake.types.text_message_event

            return (
                capo_healthlake.types.text_message_event.serialize_event_aws_json_1_0(
                    payload
                )
            )
        case {"ProgressEvent": payload}:
            import capo_healthlake.types.progress_event

            return capo_healthlake.types.progress_event.serialize_event_aws_json_1_0(
                payload
            )
        case {"HeartbeatEvent": payload}:
            import capo_healthlake.types.heartbeat_event

            return capo_healthlake.types.heartbeat_event.serialize_event_aws_json_1_0(
                payload
            )
        case {"ErrorEvent": payload}:
            import capo_healthlake.types.error_event

            return capo_healthlake.types.error_event.serialize_event_aws_json_1_0(
                payload
            )
        case {"EndOfOutputEvent": payload}:
            import capo_healthlake.types.end_of_output_event

            return (
                capo_healthlake.types.end_of_output_event.serialize_event_aws_json_1_0(
                    payload
                )
            )
        case _:
            raise ValueError(
                f"AgentOutputMessageStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_0(
    message: Message, *, response: zapros.Response
) -> _AgentOutputMessageStream:
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
        case "TextMessageEvent":
            import capo_healthlake.types.text_message_event

            return {
                "TextMessageEvent": capo_healthlake.types.text_message_event.deserialize_event_aws_json_1_0(
                    message
                )
            }
        case "ProgressEvent":
            import capo_healthlake.types.progress_event

            return {
                "ProgressEvent": capo_healthlake.types.progress_event.deserialize_event_aws_json_1_0(
                    message
                )
            }
        case "HeartbeatEvent":
            import capo_healthlake.types.heartbeat_event

            return {
                "HeartbeatEvent": capo_healthlake.types.heartbeat_event.deserialize_event_aws_json_1_0(
                    message
                )
            }
        case "ErrorEvent":
            import capo_healthlake.types.error_event

            return {
                "ErrorEvent": capo_healthlake.types.error_event.deserialize_event_aws_json_1_0(
                    message
                )
            }
        case "EndOfOutputEvent":
            import capo_healthlake.types.end_of_output_event

            return {
                "EndOfOutputEvent": capo_healthlake.types.end_of_output_event.deserialize_event_aws_json_1_0(
                    message
                )
            }
        case str():
            return UnknownEvent(event_type, message)
        case _:
            raise ValueError(
                f"AgentOutputMessageStream: unrecognized event-type {event_type!r}"
            )
