"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowResponseStream``."""

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
    import capo_bedrock_agent_runtime.types.flow_completion_event
    import capo_bedrock_agent_runtime.types.flow_multi_turn_input_request_event
    import capo_bedrock_agent_runtime.types.flow_output_event
    import capo_bedrock_agent_runtime.types.flow_trace_event


class _FlowResponseStream_flowOutputEvent(TypedDict, closed=True):
    flowOutputEvent: (
        "capo_bedrock_agent_runtime.types.flow_output_event.FlowOutputEvent"
    )


class _FlowResponseStream_flowCompletionEvent(TypedDict, closed=True):
    flowCompletionEvent: (
        "capo_bedrock_agent_runtime.types.flow_completion_event.FlowCompletionEvent"
    )


class _FlowResponseStream_flowTraceEvent(TypedDict, closed=True):
    flowTraceEvent: "capo_bedrock_agent_runtime.types.flow_trace_event.FlowTraceEvent"


class _FlowResponseStream_internalServerException(TypedDict, closed=True):
    internalServerException: "capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _FlowResponseStream_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _FlowResponseStream_resourceNotFoundException(TypedDict, closed=True):
    resourceNotFoundException: "capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException_"


class _FlowResponseStream_serviceQuotaExceededException(TypedDict, closed=True):
    serviceQuotaExceededException: "capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException_"


class _FlowResponseStream_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _FlowResponseStream_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: "capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _FlowResponseStream_conflictException(TypedDict, closed=True):
    conflictException: (
        "capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException_"
    )


class _FlowResponseStream_dependencyFailedException(TypedDict, closed=True):
    dependencyFailedException: "capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _FlowResponseStream_badGatewayException(TypedDict, closed=True):
    badGatewayException: (
        "capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"
    )


class _FlowResponseStream_flowMultiTurnInputRequestEvent(TypedDict, closed=True):
    flowMultiTurnInputRequestEvent: "capo_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.FlowMultiTurnInputRequestEvent"


_FlowResponseStream: TypeAlias = (
    _FlowResponseStream_flowOutputEvent
    | _FlowResponseStream_flowCompletionEvent
    | _FlowResponseStream_flowTraceEvent
    | _FlowResponseStream_internalServerException
    | _FlowResponseStream_validationException
    | _FlowResponseStream_resourceNotFoundException
    | _FlowResponseStream_serviceQuotaExceededException
    | _FlowResponseStream_throttlingException
    | _FlowResponseStream_accessDeniedException
    | _FlowResponseStream_conflictException
    | _FlowResponseStream_dependencyFailedException
    | _FlowResponseStream_badGatewayException
    | _FlowResponseStream_flowMultiTurnInputRequestEvent
)
FlowResponseStream: TypeAlias = AnyIterator[_FlowResponseStream]


def serialize_event_json(value: _FlowResponseStream) -> bytes:
    match value:
        case {"flowOutputEvent": payload}:
            import capo_bedrock_agent_runtime.types.flow_output_event

            return (
                capo_bedrock_agent_runtime.types.flow_output_event.serialize_event_json(
                    payload
                )
            )
        case {"flowCompletionEvent": payload}:
            import capo_bedrock_agent_runtime.types.flow_completion_event

            return capo_bedrock_agent_runtime.types.flow_completion_event.serialize_event_json(
                payload
            )
        case {"flowTraceEvent": payload}:
            import capo_bedrock_agent_runtime.types.flow_trace_event

            return (
                capo_bedrock_agent_runtime.types.flow_trace_event.serialize_event_json(
                    payload
                )
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
        case {"flowMultiTurnInputRequestEvent": payload}:
            import capo_bedrock_agent_runtime.types.flow_multi_turn_input_request_event

            return capo_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"FlowResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _FlowResponseStream:
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
        case "flowOutputEvent":
            import capo_bedrock_agent_runtime.types.flow_output_event

            return {
                "flowOutputEvent": capo_bedrock_agent_runtime.types.flow_output_event.deserialize_event_json(
                    message
                )
            }
        case "flowCompletionEvent":
            import capo_bedrock_agent_runtime.types.flow_completion_event

            return {
                "flowCompletionEvent": capo_bedrock_agent_runtime.types.flow_completion_event.deserialize_event_json(
                    message
                )
            }
        case "flowTraceEvent":
            import capo_bedrock_agent_runtime.types.flow_trace_event

            return {
                "flowTraceEvent": capo_bedrock_agent_runtime.types.flow_trace_event.deserialize_event_json(
                    message
                )
            }
        case "flowMultiTurnInputRequestEvent":
            import capo_bedrock_agent_runtime.types.flow_multi_turn_input_request_event

            return {
                "flowMultiTurnInputRequestEvent": capo_bedrock_agent_runtime.types.flow_multi_turn_input_request_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"FlowResponseStream: unrecognized event-type {event_type!r}"
            )
