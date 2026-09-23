"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommandStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore._iter import AnyIterator
from capo_bedrock_agentcore._protocol.eventstream import Message
from capo_bedrock_agentcore.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.errors.access_denied_exception
    import capo_bedrock_agentcore.errors.internal_server_exception
    import capo_bedrock_agentcore.errors.resource_not_found_exception
    import capo_bedrock_agentcore.errors.runtime_client_error
    import capo_bedrock_agentcore.errors.service_quota_exceeded_exception
    import capo_bedrock_agentcore.errors.throttling_exception
    import capo_bedrock_agentcore.errors.validation_exception
    import capo_bedrock_agentcore.types.response_chunk


class _InvokeAgentRuntimeCommandStreamOutput_chunk(TypedDict, closed=True):
    chunk: "capo_bedrock_agentcore.types.response_chunk.ResponseChunk"


class _InvokeAgentRuntimeCommandStreamOutput_accessDeniedException(
    TypedDict, closed=True
):
    accessDeniedException: (
        "capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_internalServerException(
    TypedDict, closed=True
):
    internalServerException: "capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException_"


class _InvokeAgentRuntimeCommandStreamOutput_resourceNotFoundException(
    TypedDict, closed=True
):
    resourceNotFoundException: "capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException_"


class _InvokeAgentRuntimeCommandStreamOutput_serviceQuotaExceededException(
    TypedDict, closed=True
):
    serviceQuotaExceededException: "capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _InvokeAgentRuntimeCommandStreamOutput_throttlingException(
    TypedDict, closed=True
):
    throttlingException: (
        "capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_validationException(
    TypedDict, closed=True
):
    validationException: (
        "capo_bedrock_agentcore.errors.validation_exception.ValidationException_"
    )


class _InvokeAgentRuntimeCommandStreamOutput_runtimeClientError(TypedDict, closed=True):
    runtimeClientError: (
        "capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError_"
    )


_InvokeAgentRuntimeCommandStreamOutput: TypeAlias = (
    _InvokeAgentRuntimeCommandStreamOutput_chunk
    | _InvokeAgentRuntimeCommandStreamOutput_accessDeniedException
    | _InvokeAgentRuntimeCommandStreamOutput_internalServerException
    | _InvokeAgentRuntimeCommandStreamOutput_resourceNotFoundException
    | _InvokeAgentRuntimeCommandStreamOutput_serviceQuotaExceededException
    | _InvokeAgentRuntimeCommandStreamOutput_throttlingException
    | _InvokeAgentRuntimeCommandStreamOutput_validationException
    | _InvokeAgentRuntimeCommandStreamOutput_runtimeClientError
)
InvokeAgentRuntimeCommandStreamOutput: TypeAlias = AnyIterator[
    _InvokeAgentRuntimeCommandStreamOutput
]


def serialize_event_json(value: _InvokeAgentRuntimeCommandStreamOutput) -> bytes:
    match value:
        case {"chunk": payload}:
            import capo_bedrock_agentcore.types.response_chunk

            return capo_bedrock_agentcore.types.response_chunk.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_bedrock_agentcore.errors.access_denied_exception

            return capo_bedrock_agentcore.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agentcore.errors.internal_server_exception

            return capo_bedrock_agentcore.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"resourceNotFoundException": payload}:
            import capo_bedrock_agentcore.errors.resource_not_found_exception

            return capo_bedrock_agentcore.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"serviceQuotaExceededException": payload}:
            import capo_bedrock_agentcore.errors.service_quota_exceeded_exception

            return capo_bedrock_agentcore.errors.service_quota_exceeded_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_bedrock_agentcore.errors.throttling_exception

            return (
                capo_bedrock_agentcore.errors.throttling_exception.serialize_event_json(
                    payload
                )
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
        case _:
            raise ValueError(
                f"InvokeAgentRuntimeCommandStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(message: Message) -> _InvokeAgentRuntimeCommandStreamOutput:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "accessDeniedException":
                import capo_bedrock_agentcore.errors.access_denied_exception

                data = capo_bedrock_agentcore.errors.access_denied_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException(
                    data, message=data.get("message")
                )
            case "internalServerException":
                import capo_bedrock_agentcore.errors.internal_server_exception

                data = capo_bedrock_agentcore.errors.internal_server_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException(
                    data, message=data.get("message")
                )
            case "resourceNotFoundException":
                import capo_bedrock_agentcore.errors.resource_not_found_exception

                data = capo_bedrock_agentcore.errors.resource_not_found_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException(
                    data, message=data.get("message")
                )
            case "serviceQuotaExceededException":
                import capo_bedrock_agentcore.errors.service_quota_exceeded_exception

                data = capo_bedrock_agentcore.errors.service_quota_exceeded_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException(
                    data, message=data.get("message")
                )
            case "throttlingException":
                import capo_bedrock_agentcore.errors.throttling_exception

                data = capo_bedrock_agentcore.errors.throttling_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException(
                    data, message=data.get("message")
                )
            case "validationException":
                import capo_bedrock_agentcore.errors.validation_exception

                data = capo_bedrock_agentcore.errors.validation_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.validation_exception.ValidationException(
                    data, message=data.get("message")
                )
            case "runtimeClientError":
                import capo_bedrock_agentcore.errors.runtime_client_error

                data = capo_bedrock_agentcore.errors.runtime_client_error.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError(
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
            import capo_bedrock_agentcore.types.response_chunk

            return {
                "chunk": capo_bedrock_agentcore.types.response_chunk.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeAgentRuntimeCommandStreamOutput: unrecognized event-type {event_type!r}"
            )
