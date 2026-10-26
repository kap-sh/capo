"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_bedrock_agentcore._iter import AnyIterator
from capo_bedrock_agentcore._protocol.eventstream import Message
from capo_bedrock_agentcore.errors import (
    UnknownServiceError,
)
from capo_bedrock_agentcore.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_bedrock_agentcore.errors.internal_server_exception
    import capo_bedrock_agentcore.errors.runtime_client_error
    import capo_bedrock_agentcore.errors.validation_exception
    import capo_bedrock_agentcore.types.harness_content_block_delta_event
    import capo_bedrock_agentcore.types.harness_content_block_start_event
    import capo_bedrock_agentcore.types.harness_content_block_stop_event
    import capo_bedrock_agentcore.types.harness_hook_event
    import capo_bedrock_agentcore.types.harness_message_start_event
    import capo_bedrock_agentcore.types.harness_message_stop_event
    import capo_bedrock_agentcore.types.harness_metadata_event


class _InvokeHarnessStreamOutput_messageStart(TypedDict, closed=True):
    messageStart: "capo_bedrock_agentcore.types.harness_message_start_event.HarnessMessageStartEvent"


class _InvokeHarnessStreamOutput_contentBlockStart(TypedDict, closed=True):
    contentBlockStart: "capo_bedrock_agentcore.types.harness_content_block_start_event.HarnessContentBlockStartEvent"


class _InvokeHarnessStreamOutput_contentBlockDelta(TypedDict, closed=True):
    contentBlockDelta: "capo_bedrock_agentcore.types.harness_content_block_delta_event.HarnessContentBlockDeltaEvent"


class _InvokeHarnessStreamOutput_contentBlockStop(TypedDict, closed=True):
    contentBlockStop: "capo_bedrock_agentcore.types.harness_content_block_stop_event.HarnessContentBlockStopEvent"


class _InvokeHarnessStreamOutput_messageStop(TypedDict, closed=True):
    messageStop: "capo_bedrock_agentcore.types.harness_message_stop_event.HarnessMessageStopEvent"


class _InvokeHarnessStreamOutput_metadata(TypedDict, closed=True):
    metadata: "capo_bedrock_agentcore.types.harness_metadata_event.HarnessMetadataEvent"


class _InvokeHarnessStreamOutput_internalServerException(TypedDict, closed=True):
    internalServerException: "capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _InvokeHarnessStreamOutput_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


class _InvokeHarnessStreamOutput_runtimeClientError(TypedDict, closed=True):
    runtimeClientError: (
        "capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError_"
    )


class _InvokeHarnessStreamOutput_hookEvent(TypedDict, closed=True):
    hookEvent: "capo_bedrock_agentcore.types.harness_hook_event.HarnessHookEvent"


_InvokeHarnessStreamOutput: TypeAlias = (
    _InvokeHarnessStreamOutput_messageStart
    | _InvokeHarnessStreamOutput_contentBlockStart
    | _InvokeHarnessStreamOutput_contentBlockDelta
    | _InvokeHarnessStreamOutput_contentBlockStop
    | _InvokeHarnessStreamOutput_messageStop
    | _InvokeHarnessStreamOutput_metadata
    | _InvokeHarnessStreamOutput_internalServerException
    | _InvokeHarnessStreamOutput_validationException
    | _InvokeHarnessStreamOutput_runtimeClientError
    | _InvokeHarnessStreamOutput_hookEvent
    | UnknownEvent
)
InvokeHarnessStreamOutput: TypeAlias = AnyIterator[_InvokeHarnessStreamOutput]


def serialize_event_json(value: _InvokeHarnessStreamOutput) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"InvokeHarnessStreamOutput: cannot serialize unknown event {name!r}"
            )
        case {"messageStart": payload}:
            import capo_bedrock_agentcore.types.harness_message_start_event

            return capo_bedrock_agentcore.types.harness_message_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockStart": payload}:
            import capo_bedrock_agentcore.types.harness_content_block_start_event

            return capo_bedrock_agentcore.types.harness_content_block_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockDelta": payload}:
            import capo_bedrock_agentcore.types.harness_content_block_delta_event

            return capo_bedrock_agentcore.types.harness_content_block_delta_event.serialize_event_json(
                payload
            )
        case {"contentBlockStop": payload}:
            import capo_bedrock_agentcore.types.harness_content_block_stop_event

            return capo_bedrock_agentcore.types.harness_content_block_stop_event.serialize_event_json(
                payload
            )
        case {"messageStop": payload}:
            import capo_bedrock_agentcore.types.harness_message_stop_event

            return capo_bedrock_agentcore.types.harness_message_stop_event.serialize_event_json(
                payload
            )
        case {"metadata": payload}:
            import capo_bedrock_agentcore.types.harness_metadata_event

            return capo_bedrock_agentcore.types.harness_metadata_event.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agentcore.errors.internal_server_exception

            return capo_bedrock_agentcore.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_bedrock_agentcore.errors.validation_exception

            return (
                capo_bedrock_agentcore.errors.validation_exception.serialize_event_json(
                    payload
                )
            )
        case {"runtimeClientError": payload}:
            import capo_bedrock_agentcore.errors.runtime_client_error

            return (
                capo_bedrock_agentcore.errors.runtime_client_error.serialize_event_json(
                    payload
                )
            )
        case {"hookEvent": payload}:
            import capo_bedrock_agentcore.types.harness_hook_event

            return capo_bedrock_agentcore.types.harness_hook_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeHarnessStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _InvokeHarnessStreamOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "internalServerException":
                import capo_bedrock_agentcore.errors.internal_server_exception

                data = capo_bedrock_agentcore.errors.internal_server_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException(
                    data, message=data.get("message"), response=response
                )
            case "validationException":
                import capo_bedrock_agentcore.errors.validation_exception

                data = capo_bedrock_agentcore.errors.validation_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.validation_exception.ValidationException(
                    data, message=data.get("message"), response=response
                )
            case "runtimeClientError":
                import capo_bedrock_agentcore.errors.runtime_client_error

                data = capo_bedrock_agentcore.errors.runtime_client_error.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError(
                    data, message=data.get("message"), response=response
                )
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
        case "messageStart":
            import capo_bedrock_agentcore.types.harness_message_start_event

            return {
                "messageStart": capo_bedrock_agentcore.types.harness_message_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStart":
            import capo_bedrock_agentcore.types.harness_content_block_start_event

            return {
                "contentBlockStart": capo_bedrock_agentcore.types.harness_content_block_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockDelta":
            import capo_bedrock_agentcore.types.harness_content_block_delta_event

            return {
                "contentBlockDelta": capo_bedrock_agentcore.types.harness_content_block_delta_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStop":
            import capo_bedrock_agentcore.types.harness_content_block_stop_event

            return {
                "contentBlockStop": capo_bedrock_agentcore.types.harness_content_block_stop_event.deserialize_event_json(
                    message
                )
            }
        case "messageStop":
            import capo_bedrock_agentcore.types.harness_message_stop_event

            return {
                "messageStop": capo_bedrock_agentcore.types.harness_message_stop_event.deserialize_event_json(
                    message
                )
            }
        case "metadata":
            import capo_bedrock_agentcore.types.harness_metadata_event

            return {
                "metadata": capo_bedrock_agentcore.types.harness_metadata_event.deserialize_event_json(
                    message
                )
            }
        case "hookEvent":
            import capo_bedrock_agentcore.types.harness_hook_event

            return {
                "hookEvent": capo_bedrock_agentcore.types.harness_hook_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(
                f"InvokeHarnessStreamOutput: unrecognized event-type {event_type!r}"
            )
