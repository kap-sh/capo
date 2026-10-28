"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageEvents``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_devops_agent._iter import AnyIterator
from capo_devops_agent._protocol.eventstream import Message
from capo_devops_agent.errors import (
    UnknownServiceError,
)
from capo_devops_agent.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_devops_agent.types.send_message_content_block_delta_event
    import capo_devops_agent.types.send_message_content_block_start_event
    import capo_devops_agent.types.send_message_content_block_stop_event
    import capo_devops_agent.types.send_message_heartbeat_event
    import capo_devops_agent.types.send_message_response_completed_event
    import capo_devops_agent.types.send_message_response_created_event
    import capo_devops_agent.types.send_message_response_failed_event
    import capo_devops_agent.types.send_message_response_in_progress_event
    import capo_devops_agent.types.send_message_summary_event


class SendMessageEventsResponseCreatedMember(TypedDict, closed=True):
    responseCreated: "capo_devops_agent.types.send_message_response_created_event.SendMessageResponseCreatedEvent"


class SendMessageEventsResponseInProgressMember(TypedDict, closed=True):
    responseInProgress: "capo_devops_agent.types.send_message_response_in_progress_event.SendMessageResponseInProgressEvent"


class SendMessageEventsResponseCompletedMember(TypedDict, closed=True):
    responseCompleted: "capo_devops_agent.types.send_message_response_completed_event.SendMessageResponseCompletedEvent"


class SendMessageEventsResponseFailedMember(TypedDict, closed=True):
    responseFailed: "capo_devops_agent.types.send_message_response_failed_event.SendMessageResponseFailedEvent"


class SendMessageEventsSummaryMember(TypedDict, closed=True):
    summary: (
        "capo_devops_agent.types.send_message_summary_event.SendMessageSummaryEvent"
    )


class SendMessageEventsHeartbeatMember(TypedDict, closed=True):
    heartbeat: (
        "capo_devops_agent.types.send_message_heartbeat_event.SendMessageHeartbeatEvent"
    )


class SendMessageEventsContentBlockStartMember(TypedDict, closed=True):
    contentBlockStart: "capo_devops_agent.types.send_message_content_block_start_event.SendMessageContentBlockStartEvent"


class SendMessageEventsContentBlockDeltaMember(TypedDict, closed=True):
    contentBlockDelta: "capo_devops_agent.types.send_message_content_block_delta_event.SendMessageContentBlockDeltaEvent"


class SendMessageEventsContentBlockStopMember(TypedDict, closed=True):
    contentBlockStop: "capo_devops_agent.types.send_message_content_block_stop_event.SendMessageContentBlockStopEvent"


_SendMessageEvents: TypeAlias = (
    SendMessageEventsResponseCreatedMember
    | SendMessageEventsResponseInProgressMember
    | SendMessageEventsResponseCompletedMember
    | SendMessageEventsResponseFailedMember
    | SendMessageEventsSummaryMember
    | SendMessageEventsHeartbeatMember
    | SendMessageEventsContentBlockStartMember
    | SendMessageEventsContentBlockDeltaMember
    | SendMessageEventsContentBlockStopMember
    | UnknownEvent
)
SendMessageEvents: TypeAlias = AnyIterator[_SendMessageEvents]


def serialize_event_json(value: _SendMessageEvents) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"SendMessageEvents: cannot serialize unknown event {name!r}"
            )
        case {"responseCreated": payload}:
            import capo_devops_agent.types.send_message_response_created_event

            return capo_devops_agent.types.send_message_response_created_event.serialize_event_json(
                payload
            )
        case {"responseInProgress": payload}:
            import capo_devops_agent.types.send_message_response_in_progress_event

            return capo_devops_agent.types.send_message_response_in_progress_event.serialize_event_json(
                payload
            )
        case {"responseCompleted": payload}:
            import capo_devops_agent.types.send_message_response_completed_event

            return capo_devops_agent.types.send_message_response_completed_event.serialize_event_json(
                payload
            )
        case {"responseFailed": payload}:
            import capo_devops_agent.types.send_message_response_failed_event

            return capo_devops_agent.types.send_message_response_failed_event.serialize_event_json(
                payload
            )
        case {"summary": payload}:
            import capo_devops_agent.types.send_message_summary_event

            return (
                capo_devops_agent.types.send_message_summary_event.serialize_event_json(
                    payload
                )
            )
        case {"heartbeat": payload}:
            import capo_devops_agent.types.send_message_heartbeat_event

            return capo_devops_agent.types.send_message_heartbeat_event.serialize_event_json(
                payload
            )
        case {"contentBlockStart": payload}:
            import capo_devops_agent.types.send_message_content_block_start_event

            return capo_devops_agent.types.send_message_content_block_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockDelta": payload}:
            import capo_devops_agent.types.send_message_content_block_delta_event

            return capo_devops_agent.types.send_message_content_block_delta_event.serialize_event_json(
                payload
            )
        case {"contentBlockStop": payload}:
            import capo_devops_agent.types.send_message_content_block_stop_event

            return capo_devops_agent.types.send_message_content_block_stop_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"SendMessageEvents: unrecognized variant {value!r}")


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _SendMessageEvents:
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
        case "responseCreated":
            import capo_devops_agent.types.send_message_response_created_event

            return {
                "responseCreated": capo_devops_agent.types.send_message_response_created_event.deserialize_event_json(
                    message
                )
            }
        case "responseInProgress":
            import capo_devops_agent.types.send_message_response_in_progress_event

            return {
                "responseInProgress": capo_devops_agent.types.send_message_response_in_progress_event.deserialize_event_json(
                    message
                )
            }
        case "responseCompleted":
            import capo_devops_agent.types.send_message_response_completed_event

            return {
                "responseCompleted": capo_devops_agent.types.send_message_response_completed_event.deserialize_event_json(
                    message
                )
            }
        case "responseFailed":
            import capo_devops_agent.types.send_message_response_failed_event

            return {
                "responseFailed": capo_devops_agent.types.send_message_response_failed_event.deserialize_event_json(
                    message
                )
            }
        case "summary":
            import capo_devops_agent.types.send_message_summary_event

            return {
                "summary": capo_devops_agent.types.send_message_summary_event.deserialize_event_json(
                    message
                )
            }
        case "heartbeat":
            import capo_devops_agent.types.send_message_heartbeat_event

            return {
                "heartbeat": capo_devops_agent.types.send_message_heartbeat_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStart":
            import capo_devops_agent.types.send_message_content_block_start_event

            return {
                "contentBlockStart": capo_devops_agent.types.send_message_content_block_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockDelta":
            import capo_devops_agent.types.send_message_content_block_delta_event

            return {
                "contentBlockDelta": capo_devops_agent.types.send_message_content_block_delta_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStop":
            import capo_devops_agent.types.send_message_content_block_stop_event

            return {
                "contentBlockStop": capo_devops_agent.types.send_message_content_block_stop_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(
                f"SendMessageEvents: unrecognized event-type {event_type!r}"
            )
