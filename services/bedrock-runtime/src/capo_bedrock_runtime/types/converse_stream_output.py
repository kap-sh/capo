"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_bedrock_runtime._iter import AnyIterator
from capo_bedrock_runtime._protocol.eventstream import Message
from capo_bedrock_runtime.errors import (
    UnknownServiceError,
)
from capo_bedrock_runtime.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_bedrock_runtime.errors.internal_server_exception
    import capo_bedrock_runtime.errors.model_stream_error_exception
    import capo_bedrock_runtime.errors.service_unavailable_exception
    import capo_bedrock_runtime.errors.throttling_exception
    import capo_bedrock_runtime.errors.validation_exception
    import capo_bedrock_runtime.types.content_block_delta_event
    import capo_bedrock_runtime.types.content_block_start_event
    import capo_bedrock_runtime.types.content_block_stop_event
    import capo_bedrock_runtime.types.converse_stream_metadata_event
    import capo_bedrock_runtime.types.message_start_event
    import capo_bedrock_runtime.types.message_stop_event


class ConverseStreamOutputMessageStartMember(TypedDict, closed=True):
    messageStart: "capo_bedrock_runtime.types.message_start_event.MessageStartEvent"


class ConverseStreamOutputContentBlockStartMember(TypedDict, closed=True):
    contentBlockStart: (
        "capo_bedrock_runtime.types.content_block_start_event.ContentBlockStartEvent"
    )


class ConverseStreamOutputContentBlockDeltaMember(TypedDict, closed=True):
    contentBlockDelta: (
        "capo_bedrock_runtime.types.content_block_delta_event.ContentBlockDeltaEvent"
    )


class ConverseStreamOutputContentBlockStopMember(TypedDict, closed=True):
    contentBlockStop: (
        "capo_bedrock_runtime.types.content_block_stop_event.ContentBlockStopEvent"
    )


class ConverseStreamOutputMessageStopMember(TypedDict, closed=True):
    messageStop: "capo_bedrock_runtime.types.message_stop_event.MessageStopEvent"


class ConverseStreamOutputMetadataMember(TypedDict, closed=True):
    metadata: "capo_bedrock_runtime.types.converse_stream_metadata_event.ConverseStreamMetadataEvent"


class ConverseStreamOutputInternalServerExceptionMember(TypedDict, closed=True):
    internalServerException: (
        "capo_bedrock_runtime.errors.internal_server_exception.InternalServerException_"
    )


class ConverseStreamOutputModelStreamErrorExceptionMember(TypedDict, closed=True):
    modelStreamErrorException: "capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class ConverseStreamOutputValidationExceptionMember(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class ConverseStreamOutputThrottlingExceptionMember(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class ConverseStreamOutputServiceUnavailableExceptionMember(TypedDict, closed=True):
    serviceUnavailableException: "capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


_ConverseStreamOutput: TypeAlias = (
    ConverseStreamOutputMessageStartMember
    | ConverseStreamOutputContentBlockStartMember
    | ConverseStreamOutputContentBlockDeltaMember
    | ConverseStreamOutputContentBlockStopMember
    | ConverseStreamOutputMessageStopMember
    | ConverseStreamOutputMetadataMember
    | ConverseStreamOutputInternalServerExceptionMember
    | ConverseStreamOutputModelStreamErrorExceptionMember
    | ConverseStreamOutputValidationExceptionMember
    | ConverseStreamOutputThrottlingExceptionMember
    | ConverseStreamOutputServiceUnavailableExceptionMember
    | UnknownEvent
)
ConverseStreamOutput: TypeAlias = AnyIterator[_ConverseStreamOutput]


def serialize_event_json(value: _ConverseStreamOutput) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"ConverseStreamOutput: cannot serialize unknown event {name!r}"
            )
        case {"messageStart": payload}:
            import capo_bedrock_runtime.types.message_start_event

            return capo_bedrock_runtime.types.message_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockStart": payload}:
            import capo_bedrock_runtime.types.content_block_start_event

            return capo_bedrock_runtime.types.content_block_start_event.serialize_event_json(
                payload
            )
        case {"contentBlockDelta": payload}:
            import capo_bedrock_runtime.types.content_block_delta_event

            return capo_bedrock_runtime.types.content_block_delta_event.serialize_event_json(
                payload
            )
        case {"contentBlockStop": payload}:
            import capo_bedrock_runtime.types.content_block_stop_event

            return capo_bedrock_runtime.types.content_block_stop_event.serialize_event_json(
                payload
            )
        case {"messageStop": payload}:
            import capo_bedrock_runtime.types.message_stop_event

            return capo_bedrock_runtime.types.message_stop_event.serialize_event_json(
                payload
            )
        case {"metadata": payload}:
            import capo_bedrock_runtime.types.converse_stream_metadata_event

            return capo_bedrock_runtime.types.converse_stream_metadata_event.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import capo_bedrock_runtime.errors.internal_server_exception

            return capo_bedrock_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"modelStreamErrorException": payload}:
            import capo_bedrock_runtime.errors.model_stream_error_exception

            return capo_bedrock_runtime.errors.model_stream_error_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_bedrock_runtime.errors.validation_exception

            return (
                capo_bedrock_runtime.errors.validation_exception.serialize_event_json(
                    payload
                )
            )
        case {"throttlingException": payload}:
            import capo_bedrock_runtime.errors.throttling_exception

            return (
                capo_bedrock_runtime.errors.throttling_exception.serialize_event_json(
                    payload
                )
            )
        case {"serviceUnavailableException": payload}:
            import capo_bedrock_runtime.errors.service_unavailable_exception

            return capo_bedrock_runtime.errors.service_unavailable_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ConverseStreamOutput: unrecognized variant {value!r}")


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _ConverseStreamOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "internalServerException":
                import capo_bedrock_runtime.errors.internal_server_exception

                data = capo_bedrock_runtime.errors.internal_server_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.internal_server_exception.InternalServerException(
                    data, message=data.get("message"), response=response
                )
            case "modelStreamErrorException":
                import capo_bedrock_runtime.errors.model_stream_error_exception

                data = capo_bedrock_runtime.errors.model_stream_error_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException(
                    data, message=data.get("message"), response=response
                )
            case "validationException":
                import capo_bedrock_runtime.errors.validation_exception

                data = capo_bedrock_runtime.errors.validation_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.validation_exception.ValidationException(
                    data, message=data.get("message"), response=response
                )
            case "throttlingException":
                import capo_bedrock_runtime.errors.throttling_exception

                data = capo_bedrock_runtime.errors.throttling_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.throttling_exception.ThrottlingException(
                    data, message=data.get("message"), response=response
                )
            case "serviceUnavailableException":
                import capo_bedrock_runtime.errors.service_unavailable_exception

                data = capo_bedrock_runtime.errors.service_unavailable_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException(
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
            import capo_bedrock_runtime.types.message_start_event

            return {
                "messageStart": capo_bedrock_runtime.types.message_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStart":
            import capo_bedrock_runtime.types.content_block_start_event

            return {
                "contentBlockStart": capo_bedrock_runtime.types.content_block_start_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockDelta":
            import capo_bedrock_runtime.types.content_block_delta_event

            return {
                "contentBlockDelta": capo_bedrock_runtime.types.content_block_delta_event.deserialize_event_json(
                    message
                )
            }
        case "contentBlockStop":
            import capo_bedrock_runtime.types.content_block_stop_event

            return {
                "contentBlockStop": capo_bedrock_runtime.types.content_block_stop_event.deserialize_event_json(
                    message
                )
            }
        case "messageStop":
            import capo_bedrock_runtime.types.message_stop_event

            return {
                "messageStop": capo_bedrock_runtime.types.message_stop_event.deserialize_event_json(
                    message
                )
            }
        case "metadata":
            import capo_bedrock_runtime.types.converse_stream_metadata_event

            return {
                "metadata": capo_bedrock_runtime.types.converse_stream_metadata_event.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(
                f"ConverseStreamOutput: unrecognized event-type {event_type!r}"
            )
