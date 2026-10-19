"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatOutputStream``."""

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
    import capo_qbusiness.types.action_review_event
    import capo_qbusiness.types.auth_challenge_request_event
    import capo_qbusiness.types.failed_attachment_event
    import capo_qbusiness.types.metadata_event
    import capo_qbusiness.types.text_output_event


class _ChatOutputStream_textEvent(TypedDict, closed=True):
    textEvent: "capo_qbusiness.types.text_output_event.TextOutputEvent"


class _ChatOutputStream_metadataEvent(TypedDict, closed=True):
    metadataEvent: "capo_qbusiness.types.metadata_event.MetadataEvent"


class _ChatOutputStream_actionReviewEvent(TypedDict, closed=True):
    actionReviewEvent: "capo_qbusiness.types.action_review_event.ActionReviewEvent"


class _ChatOutputStream_failedAttachmentEvent(TypedDict, closed=True):
    failedAttachmentEvent: (
        "capo_qbusiness.types.failed_attachment_event.FailedAttachmentEvent"
    )


class _ChatOutputStream_authChallengeRequestEvent(TypedDict, closed=True):
    authChallengeRequestEvent: (
        "capo_qbusiness.types.auth_challenge_request_event.AuthChallengeRequestEvent"
    )


_ChatOutputStream: TypeAlias = (
    _ChatOutputStream_textEvent
    | _ChatOutputStream_metadataEvent
    | _ChatOutputStream_actionReviewEvent
    | _ChatOutputStream_failedAttachmentEvent
    | _ChatOutputStream_authChallengeRequestEvent
    | UnknownEvent
)
ChatOutputStream: TypeAlias = AnyIterator[_ChatOutputStream]


def serialize_event_json(value: _ChatOutputStream) -> bytes:
    if isinstance(value, UnknownEvent):
        raise ValueError(
            f"ChatOutputStream: cannot serialize unknown event {value.event_type!r}"
        )
    match value:
        case {"textEvent": payload}:
            import capo_qbusiness.types.text_output_event

            return capo_qbusiness.types.text_output_event.serialize_event_json(payload)
        case {"metadataEvent": payload}:
            import capo_qbusiness.types.metadata_event

            return capo_qbusiness.types.metadata_event.serialize_event_json(payload)
        case {"actionReviewEvent": payload}:
            import capo_qbusiness.types.action_review_event

            return capo_qbusiness.types.action_review_event.serialize_event_json(
                payload
            )
        case {"failedAttachmentEvent": payload}:
            import capo_qbusiness.types.failed_attachment_event

            return capo_qbusiness.types.failed_attachment_event.serialize_event_json(
                payload
            )
        case {"authChallengeRequestEvent": payload}:
            import capo_qbusiness.types.auth_challenge_request_event

            return (
                capo_qbusiness.types.auth_challenge_request_event.serialize_event_json(
                    payload
                )
            )
        case _:
            raise ValueError(f"ChatOutputStream: unrecognized variant {value!r}")


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _ChatOutputStream:
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
        case "textEvent":
            import capo_qbusiness.types.text_output_event

            return {
                "textEvent": capo_qbusiness.types.text_output_event.deserialize_event_json(
                    message
                )
            }
        case "metadataEvent":
            import capo_qbusiness.types.metadata_event

            return {
                "metadataEvent": capo_qbusiness.types.metadata_event.deserialize_event_json(
                    message
                )
            }
        case "actionReviewEvent":
            import capo_qbusiness.types.action_review_event

            return {
                "actionReviewEvent": capo_qbusiness.types.action_review_event.deserialize_event_json(
                    message
                )
            }
        case "failedAttachmentEvent":
            import capo_qbusiness.types.failed_attachment_event

            return {
                "failedAttachmentEvent": capo_qbusiness.types.failed_attachment_event.deserialize_event_json(
                    message
                )
            }
        case "authChallengeRequestEvent":
            import capo_qbusiness.types.auth_challenge_request_event

            return {
                "authChallengeRequestEvent": capo_qbusiness.types.auth_challenge_request_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return UnknownEvent(event_type, message)
        case _:
            raise ValueError(
                f"ChatOutputStream: unrecognized event-type {event_type!r}"
            )
