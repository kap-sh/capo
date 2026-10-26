"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatInputStream``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_qbusiness._iter import AnyIterator
from capo_qbusiness._protocol.eventstream import Message
from capo_qbusiness.errors import (
    UnknownServiceError,
)
from capo_qbusiness.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution_event
    import capo_qbusiness.types.attachment_input_event
    import capo_qbusiness.types.auth_challenge_response_event
    import capo_qbusiness.types.configuration_event
    import capo_qbusiness.types.end_of_input_event
    import capo_qbusiness.types.text_input_event


class _ChatInputStream_configurationEvent(TypedDict, closed=True):
    configurationEvent: "capo_qbusiness.types.configuration_event.ConfigurationEvent"


class _ChatInputStream_textEvent(TypedDict, closed=True):
    textEvent: "capo_qbusiness.types.text_input_event.TextInputEvent"


class _ChatInputStream_attachmentEvent(TypedDict, closed=True):
    attachmentEvent: "capo_qbusiness.types.attachment_input_event.AttachmentInputEvent"


class _ChatInputStream_actionExecutionEvent(TypedDict, closed=True):
    actionExecutionEvent: (
        "capo_qbusiness.types.action_execution_event.ActionExecutionEvent"
    )


class _ChatInputStream_endOfInputEvent(TypedDict, closed=True):
    endOfInputEvent: "capo_qbusiness.types.end_of_input_event.EndOfInputEvent"


class _ChatInputStream_authChallengeResponseEvent(TypedDict, closed=True):
    authChallengeResponseEvent: (
        "capo_qbusiness.types.auth_challenge_response_event.AuthChallengeResponseEvent"
    )


_ChatInputStream: TypeAlias = (
    _ChatInputStream_configurationEvent
    | _ChatInputStream_textEvent
    | _ChatInputStream_attachmentEvent
    | _ChatInputStream_actionExecutionEvent
    | _ChatInputStream_endOfInputEvent
    | _ChatInputStream_authChallengeResponseEvent
    | UnknownEvent
)
ChatInputStream: TypeAlias = AnyIterator[_ChatInputStream]


def serialize_event_json(value: _ChatInputStream) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"ChatInputStream: cannot serialize unknown event {name!r}"
            )
        case {"configurationEvent": payload}:
            import capo_qbusiness.types.configuration_event

            return capo_qbusiness.types.configuration_event.serialize_event_json(
                payload
            )
        case {"textEvent": payload}:
            import capo_qbusiness.types.text_input_event

            return capo_qbusiness.types.text_input_event.serialize_event_json(payload)
        case {"attachmentEvent": payload}:
            import capo_qbusiness.types.attachment_input_event

            return capo_qbusiness.types.attachment_input_event.serialize_event_json(
                payload
            )
        case {"actionExecutionEvent": payload}:
            import capo_qbusiness.types.action_execution_event

            return capo_qbusiness.types.action_execution_event.serialize_event_json(
                payload
            )
        case {"endOfInputEvent": payload}:
            import capo_qbusiness.types.end_of_input_event

            return capo_qbusiness.types.end_of_input_event.serialize_event_json(payload)
        case {"authChallengeResponseEvent": payload}:
            import capo_qbusiness.types.auth_challenge_response_event

            return (
                capo_qbusiness.types.auth_challenge_response_event.serialize_event_json(
                    payload
                )
            )
        case _:
            raise ValueError(f"ChatInputStream: unrecognized variant {value!r}")


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _ChatInputStream:
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
        case "configurationEvent":
            import capo_qbusiness.types.configuration_event

            return {
                "configurationEvent": capo_qbusiness.types.configuration_event.deserialize_event_json(
                    message
                )
            }
        case "textEvent":
            import capo_qbusiness.types.text_input_event

            return {
                "textEvent": capo_qbusiness.types.text_input_event.deserialize_event_json(
                    message
                )
            }
        case "attachmentEvent":
            import capo_qbusiness.types.attachment_input_event

            return {
                "attachmentEvent": capo_qbusiness.types.attachment_input_event.deserialize_event_json(
                    message
                )
            }
        case "actionExecutionEvent":
            import capo_qbusiness.types.action_execution_event

            return {
                "actionExecutionEvent": capo_qbusiness.types.action_execution_event.deserialize_event_json(
                    message
                )
            }
        case "endOfInputEvent":
            import capo_qbusiness.types.end_of_input_event

            return {
                "endOfInputEvent": capo_qbusiness.types.end_of_input_event.deserialize_event_json(
                    message
                )
            }
        case "authChallengeResponseEvent":
            import capo_qbusiness.types.auth_challenge_response_event

            return {
                "authChallengeResponseEvent": capo_qbusiness.types.auth_challenge_response_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(f"ChatInputStream: unrecognized event-type {event_type!r}")
