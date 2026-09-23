"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch_logs._iter import AnyIterator
from capo_cloudwatch_logs._protocol.eventstream import Message
from capo_cloudwatch_logs.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_cloudwatch_logs.errors.session_streaming_exception
    import capo_cloudwatch_logs.errors.session_timeout_exception
    import capo_cloudwatch_logs.types.live_tail_session_start
    import capo_cloudwatch_logs.types.live_tail_session_update


class _StartLiveTailResponseStream_sessionStart(TypedDict, closed=True):
    sessionStart: (
        "capo_cloudwatch_logs.types.live_tail_session_start.LiveTailSessionStart"
    )


class _StartLiveTailResponseStream_sessionUpdate(TypedDict, closed=True):
    sessionUpdate: (
        "capo_cloudwatch_logs.types.live_tail_session_update.LiveTailSessionUpdate"
    )


class _StartLiveTailResponseStream_SessionTimeoutException(TypedDict, closed=True):
    SessionTimeoutException: (
        "capo_cloudwatch_logs.errors.session_timeout_exception.SessionTimeoutException_"
    )


class _StartLiveTailResponseStream_SessionStreamingException(TypedDict, closed=True):
    SessionStreamingException: "capo_cloudwatch_logs.errors.session_streaming_exception.SessionStreamingException_"


_StartLiveTailResponseStream: TypeAlias = (
    _StartLiveTailResponseStream_sessionStart
    | _StartLiveTailResponseStream_sessionUpdate
    | _StartLiveTailResponseStream_SessionTimeoutException
    | _StartLiveTailResponseStream_SessionStreamingException
)
StartLiveTailResponseStream: TypeAlias = AnyIterator[_StartLiveTailResponseStream]


def serialize_event_aws_json_1_1(value: _StartLiveTailResponseStream) -> bytes:
    match value:
        case {"sessionStart": payload}:
            import capo_cloudwatch_logs.types.live_tail_session_start

            return capo_cloudwatch_logs.types.live_tail_session_start.serialize_event_aws_json_1_1(
                payload
            )
        case {"sessionUpdate": payload}:
            import capo_cloudwatch_logs.types.live_tail_session_update

            return capo_cloudwatch_logs.types.live_tail_session_update.serialize_event_aws_json_1_1(
                payload
            )
        case {"SessionTimeoutException": payload}:
            import capo_cloudwatch_logs.errors.session_timeout_exception

            return capo_cloudwatch_logs.errors.session_timeout_exception.serialize_event_aws_json_1_1(
                payload
            )
        case {"SessionStreamingException": payload}:
            import capo_cloudwatch_logs.errors.session_streaming_exception

            return capo_cloudwatch_logs.errors.session_streaming_exception.serialize_event_aws_json_1_1(
                payload
            )
        case _:
            raise ValueError(
                f"StartLiveTailResponseStream: unrecognized variant {value!r}"
            )


def deserialize_event_aws_json_1_1(message: Message) -> _StartLiveTailResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "SessionTimeoutException":
                import capo_cloudwatch_logs.errors.session_timeout_exception

                data = capo_cloudwatch_logs.errors.session_timeout_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_cloudwatch_logs.errors.session_timeout_exception.SessionTimeoutException(
                    data, message=data.get("message")
                )
            case "SessionStreamingException":
                import capo_cloudwatch_logs.errors.session_streaming_exception

                data = capo_cloudwatch_logs.errors.session_streaming_exception.deserialize_event_aws_json_1_1(
                    message
                )
                raise capo_cloudwatch_logs.errors.session_streaming_exception.SessionStreamingException(
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
        case "sessionStart":
            import capo_cloudwatch_logs.types.live_tail_session_start

            return {
                "sessionStart": capo_cloudwatch_logs.types.live_tail_session_start.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case "sessionUpdate":
            import capo_cloudwatch_logs.types.live_tail_session_update

            return {
                "sessionUpdate": capo_cloudwatch_logs.types.live_tail_session_update.deserialize_event_aws_json_1_1(
                    message
                )
            }
        case _:
            raise ValueError(
                f"StartLiveTailResponseStream: unrecognized event-type {event_type!r}"
            )
