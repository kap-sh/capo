"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPromptStream``."""

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
    import capo_bedrock_agent_runtime.errors.dependency_failed_exception
    import capo_bedrock_agent_runtime.errors.internal_server_exception
    import capo_bedrock_agent_runtime.errors.throttling_exception
    import capo_bedrock_agent_runtime.errors.validation_exception
    import capo_bedrock_agent_runtime.types.analyze_prompt_event
    import capo_bedrock_agent_runtime.types.optimized_prompt_event


class _OptimizedPromptStream_optimizedPromptEvent(TypedDict, closed=True):
    optimizedPromptEvent: (
        "capo_bedrock_agent_runtime.types.optimized_prompt_event.OptimizedPromptEvent"
    )


class _OptimizedPromptStream_analyzePromptEvent(TypedDict, closed=True):
    analyzePromptEvent: (
        "capo_bedrock_agent_runtime.types.analyze_prompt_event.AnalyzePromptEvent"
    )


class _OptimizedPromptStream_internalServerException(TypedDict, closed=True):
    internalServerException: "capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException_"


class _OptimizedPromptStream_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _OptimizedPromptStream_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_agent_runtime.errors.validation_exception.ValidationException_"
    )


class _OptimizedPromptStream_dependencyFailedException(TypedDict, closed=True):
    dependencyFailedException: "capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException_"


class _OptimizedPromptStream_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: "capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException_"


class _OptimizedPromptStream_badGatewayException(TypedDict, closed=True):
    badGatewayException: (
        "capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException_"
    )


_OptimizedPromptStream: TypeAlias = (
    _OptimizedPromptStream_optimizedPromptEvent
    | _OptimizedPromptStream_analyzePromptEvent
    | _OptimizedPromptStream_internalServerException
    | _OptimizedPromptStream_throttlingException
    | _OptimizedPromptStream_validationException
    | _OptimizedPromptStream_dependencyFailedException
    | _OptimizedPromptStream_accessDeniedException
    | _OptimizedPromptStream_badGatewayException
)
OptimizedPromptStream: TypeAlias = AnyIterator[_OptimizedPromptStream]


def serialize_event_json(value: _OptimizedPromptStream) -> bytes:
    match value:
        case {"optimizedPromptEvent": payload}:
            import capo_bedrock_agent_runtime.types.optimized_prompt_event

            return capo_bedrock_agent_runtime.types.optimized_prompt_event.serialize_event_json(
                payload
            )
        case {"analyzePromptEvent": payload}:
            import capo_bedrock_agent_runtime.types.analyze_prompt_event

            return capo_bedrock_agent_runtime.types.analyze_prompt_event.serialize_event_json(
                payload
            )
        case {"internalServerException": payload}:
            import capo_bedrock_agent_runtime.errors.internal_server_exception

            return capo_bedrock_agent_runtime.errors.internal_server_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_bedrock_agent_runtime.errors.throttling_exception

            return capo_bedrock_agent_runtime.errors.throttling_exception.serialize_event_json(
                payload
            )
        case {"validationException": payload}:
            import capo_bedrock_agent_runtime.errors.validation_exception

            return capo_bedrock_agent_runtime.errors.validation_exception.serialize_event_json(
                payload
            )
        case {"dependencyFailedException": payload}:
            import capo_bedrock_agent_runtime.errors.dependency_failed_exception

            return capo_bedrock_agent_runtime.errors.dependency_failed_exception.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_bedrock_agent_runtime.errors.access_denied_exception

            return capo_bedrock_agent_runtime.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"badGatewayException": payload}:
            import capo_bedrock_agent_runtime.errors.bad_gateway_exception

            return capo_bedrock_agent_runtime.errors.bad_gateway_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"OptimizedPromptStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _OptimizedPromptStream:
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
            case "throttlingException":
                import capo_bedrock_agent_runtime.errors.throttling_exception

                data = capo_bedrock_agent_runtime.errors.throttling_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException(
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
            case "dependencyFailedException":
                import capo_bedrock_agent_runtime.errors.dependency_failed_exception

                data = capo_bedrock_agent_runtime.errors.dependency_failed_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException(
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
        case "optimizedPromptEvent":
            import capo_bedrock_agent_runtime.types.optimized_prompt_event

            return {
                "optimizedPromptEvent": capo_bedrock_agent_runtime.types.optimized_prompt_event.deserialize_event_json(
                    message
                )
            }
        case "analyzePromptEvent":
            import capo_bedrock_agent_runtime.types.analyze_prompt_event

            return {
                "analyzePromptEvent": capo_bedrock_agent_runtime.types.analyze_prompt_event.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"OptimizedPromptStream: unrecognized event-type {event_type!r}"
            )
