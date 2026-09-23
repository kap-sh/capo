"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime._iter import AnyIterator
from capo_bedrock_agent_runtime._protocol.eventstream import Message
from capo_bedrock_agent_runtime.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.errors.access_denied_exception
    import capo_bedrock_agent_runtime.errors.bad_gateway_exception
    import capo_bedrock_agent_runtime.errors.conflict_exception
    import capo_bedrock_agent_runtime.errors.dependency_failed_exception
    import capo_bedrock_agent_runtime.errors.internal_server_exception
    import capo_bedrock_agent_runtime.errors.resource_not_found_exception
    import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception
    import capo_bedrock_agent_runtime.errors.throttling_exception
    import capo_bedrock_agent_runtime.errors.validation_exception
    import capo_bedrock_agent_runtime.types.inline_agent_file_part
    import capo_bedrock_agent_runtime.types.inline_agent_payload_part
    import capo_bedrock_agent_runtime.types.inline_agent_return_control_payload
    import capo_bedrock_agent_runtime.types.inline_agent_trace_part


class _InlineAgentResponseStream_chunk(TypedDict, closed=True):
    chunk: "capo_bedrock_agent_runtime.types.inline_agent_payload_part.InlineAgentPayloadPart"


class _InlineAgentResponseStream_trace(TypedDict, closed=True):
    trace: (
        "capo_bedrock_agent_runtime.types.inline_agent_trace_part.InlineAgentTracePart"
    )


class _InlineAgentResponseStream_returnControl(TypedDict, closed=True):
    returnControl: "capo_bedrock_agent_runtime.types.inline_agent_return_control_payload.InlineAgentReturnControlPayload"


class _InlineAgentResponseStream_internalServerException(TypedDict, closed=True):
    internalServerException: "capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _InlineAgentResponseStream_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _InlineAgentResponseStream_resourceNotFoundException(TypedDict, closed=True):
    resourceNotFoundException: "capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _InlineAgentResponseStream_serviceQuotaExceededException(TypedDict, closed=True):
    serviceQuotaExceededException: "capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _InlineAgentResponseStream_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _InlineAgentResponseStream_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: "capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _InlineAgentResponseStream_conflictException(TypedDict, closed=True):
    conflictException: (
        "capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _InlineAgentResponseStream_dependencyFailedException(TypedDict, closed=True):
    dependencyFailedException: "capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _InlineAgentResponseStream_badGatewayException(TypedDict, closed=True):
    badGatewayException: (
        "capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"
    )


class _InlineAgentResponseStream_files(TypedDict, closed=True):
    files: "capo_bedrock_agent_runtime.types.inline_agent_file_part.InlineAgentFilePart"


_InlineAgentResponseStream: TypeAlias = (
    _InlineAgentResponseStream_chunk
    | _InlineAgentResponseStream_trace
    | _InlineAgentResponseStream_returnControl
    | _InlineAgentResponseStream_internalServerException
    | _InlineAgentResponseStream_validationException
    | _InlineAgentResponseStream_resourceNotFoundException
    | _InlineAgentResponseStream_serviceQuotaExceededException
    | _InlineAgentResponseStream_throttlingException
    | _InlineAgentResponseStream_accessDeniedException
    | _InlineAgentResponseStream_conflictException
    | _InlineAgentResponseStream_dependencyFailedException
    | _InlineAgentResponseStream_badGatewayException
    | _InlineAgentResponseStream_files
)
InlineAgentResponseStream: TypeAlias = AnyIterator[_InlineAgentResponseStream]


def serialize_event_json(value: _InlineAgentResponseStream) -> bytes:
    match value:
        case {"chunk": payload}:
            import capo_bedrock_agent_runtime.types.inline_agent_payload_part

            return capo_bedrock_agent_runtime.types.inline_agent_payload_part.serialize_event_json(
                payload
            )
        case {"trace": payload}:
            import capo_bedrock_agent_runtime.types.inline_agent_trace_part

            return capo_bedrock_agent_runtime.types.inline_agent_trace_part.serialize_event_json(
                payload
            )
        case {"returnControl": payload}:
            import capo_bedrock_agent_runtime.types.inline_agent_return_control_payload

            return capo_bedrock_agent_runtime.types.inline_agent_return_control_payload.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agent_runtime.errors.internal_server_exception

            return capo_bedrock_agent_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_bedrock_agent_runtime.errors.validation_exception

            return capo_bedrock_agent_runtime.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import capo_bedrock_agent_runtime.errors.resource_not_found_exception

            return capo_bedrock_agent_runtime.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception

            return capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_bedrock_agent_runtime.errors.throttling_exception

            return capo_bedrock_agent_runtime.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_bedrock_agent_runtime.errors.access_denied_exception

            return capo_bedrock_agent_runtime.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictException": payload}:
            import capo_bedrock_agent_runtime.errors.conflict_exception

            return capo_bedrock_agent_runtime.errors.conflict_exception.serialize_event_json(
                payload
            )
        case {"dependencyFailedException": payload}:
            import capo_bedrock_agent_runtime.errors.dependency_failed_exception

            return capo_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"badGatewayException": payload}:
            import capo_bedrock_agent_runtime.errors.bad_gateway_exception

            return capo_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_event_json(
                payload
            )
        case {"files": payload}:
            import capo_bedrock_agent_runtime.types.inline_agent_file_part

            return capo_bedrock_agent_runtime.types.inline_agent_file_part.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InlineAgentResponseStream: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _InlineAgentResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "internalServerException":
                import capo_bedrock_agent_runtime.errors.internal_server_exception

                data = capo_bedrock_agent_runtime.errors.internal_server_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException(
                    data, message=data.get("message")
                )
            case "validationException":
                import capo_bedrock_agent_runtime.errors.validation_exception

                data = capo_bedrock_agent_runtime.errors.validation_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.validation_exception.ValidationException(
                    data, message=data.get("message")
                )
            case "resourceNotFoundException":
                import capo_bedrock_agent_runtime.errors.resource_not_found_exception

                data = capo_bedrock_agent_runtime.errors.resource_not_found_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException(
                    data, message=data.get("message")
                )
            case "serviceQuotaExceededException":
                import capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception

                data = capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    data, message=data.get("message")
                )
            case "throttlingException":
                import capo_bedrock_agent_runtime.errors.throttling_exception

                data = capo_bedrock_agent_runtime.errors.throttling_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException(
                    data, message=data.get("message")
                )
            case "accessDeniedException":
                import capo_bedrock_agent_runtime.errors.access_denied_exception

                data = capo_bedrock_agent_runtime.errors.access_denied_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException(
                    data, message=data.get("message")
                )
            case "conflictException":
                import capo_bedrock_agent_runtime.errors.conflict_exception

                data = capo_bedrock_agent_runtime.errors.conflict_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException(
                    data, message=data.get("message")
                )
            case "dependencyFailedException":
                import capo_bedrock_agent_runtime.errors.dependency_failed_exception

                data = capo_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException(
                    data, message=data.get("message")
                )
            case "badGatewayException":
                import capo_bedrock_agent_runtime.errors.bad_gateway_exception

                data = capo_bedrock_agent_runtime.errors.bad_gateway_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException(
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
        case "chunk":
            import capo_bedrock_agent_runtime.types.inline_agent_payload_part

            return {
                "chunk": capo_bedrock_agent_runtime.types.inline_agent_payload_part.deserialize_event_json(
                    message
                )
            }
        case "trace":
            import capo_bedrock_agent_runtime.types.inline_agent_trace_part

            return {
                "trace": capo_bedrock_agent_runtime.types.inline_agent_trace_part.deserialize_event_json(
                    message
                )
            }
        case "returnControl":
            import capo_bedrock_agent_runtime.types.inline_agent_return_control_payload

            return {
                "returnControl": capo_bedrock_agent_runtime.types.inline_agent_return_control_payload.deserialize_event_json(
                    message
                )
            }
        case "files":
            import capo_bedrock_agent_runtime.types.inline_agent_file_part

            return {
                "files": capo_bedrock_agent_runtime.types.inline_agent_file_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InlineAgentResponseStream: unrecognized event-type {event_type!r}"
            )
