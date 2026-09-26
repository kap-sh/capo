"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResponseStream``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotsitewise._iter import AnyIterator
from capo_iotsitewise._protocol.eventstream import Message
from capo_iotsitewise.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_iotsitewise.errors.access_denied_exception
    import capo_iotsitewise.errors.conflicting_operation_exception
    import capo_iotsitewise.errors.internal_failure_exception
    import capo_iotsitewise.errors.invalid_request_exception
    import capo_iotsitewise.errors.limit_exceeded_exception
    import capo_iotsitewise.errors.resource_not_found_exception
    import capo_iotsitewise.errors.throttling_exception
    import capo_iotsitewise.types.invocation_output
    import capo_iotsitewise.types.trace


class _ResponseStream_trace(TypedDict, closed=True):
    trace: "capo_iotsitewise.types.trace.Trace"


class _ResponseStream_output(TypedDict, closed=True):
    output: "capo_iotsitewise.types.invocation_output.InvocationOutput"


class _ResponseStream_accessDeniedException(TypedDict, closed=True):
    accessDeniedException: (
        "capo_iotsitewise.errors.access_denied_exception.AccessDeniedException_"
    )


class _ResponseStream_conflictingOperationException(TypedDict, closed=True):
    conflictingOperationException: "capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException_"


class _ResponseStream_internalFailureException(TypedDict, closed=True):
    internalFailureException: (
        "capo_iotsitewise.errors.internal_failure_exception.InternalFailureException_"
    )


class _ResponseStream_invalidRequestException(TypedDict, closed=True):
    invalidRequestException: (
        "capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException_"
    )


class _ResponseStream_limitExceededException(TypedDict, closed=True):
    limitExceededException: (
        "capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException_"
    )


class _ResponseStream_resourceNotFoundException(TypedDict, closed=True):
    resourceNotFoundException: "capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException_"


class _ResponseStream_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_iotsitewise.errors.throttling_exception.ThrottlingException_"
    )


_ResponseStream: TypeAlias = (
    _ResponseStream_trace
    | _ResponseStream_output
    | _ResponseStream_accessDeniedException
    | _ResponseStream_conflictingOperationException
    | _ResponseStream_internalFailureException
    | _ResponseStream_invalidRequestException
    | _ResponseStream_limitExceededException
    | _ResponseStream_resourceNotFoundException
    | _ResponseStream_throttlingException
)
ResponseStream: TypeAlias = AnyIterator[_ResponseStream]


def serialize_event_json(value: _ResponseStream) -> bytes:
    match value:
        case {"trace": payload}:
            import capo_iotsitewise.types.trace

            return capo_iotsitewise.types.trace.serialize_event_json(payload)
        case {"output": payload}:
            import capo_iotsitewise.types.invocation_output

            return capo_iotsitewise.types.invocation_output.serialize_event_json(
                payload
            )
        case {"accessDeniedException": payload}:
            import capo_iotsitewise.errors.access_denied_exception

            return capo_iotsitewise.errors.access_denied_exception.serialize_event_json(
                payload
            )
        case {"conflictingOperationException": payload}:
            import capo_iotsitewise.errors.conflicting_operation_exception

            return capo_iotsitewise.errors.conflicting_operation_exception.serialize_event_json(
                payload
            )
        case {"internalFailureException": payload}:
            import capo_iotsitewise.errors.internal_failure_exception

            return (
                capo_iotsitewise.errors.internal_failure_exception.serialize_event_json(
                    payload
                )
            )
        case {"invalidRequestException": payload}:
            import capo_iotsitewise.errors.invalid_request_exception

            return (
                capo_iotsitewise.errors.invalid_request_exception.serialize_event_json(
                    payload
                )
            )
        case {"limitExceededException": payload}:
            import capo_iotsitewise.errors.limit_exceeded_exception

            return (
                capo_iotsitewise.errors.limit_exceeded_exception.serialize_event_json(
                    payload
                )
            )
        case {"resourceNotFoundException": payload}:
            import capo_iotsitewise.errors.resource_not_found_exception

            return capo_iotsitewise.errors.resource_not_found_exception.serialize_event_json(
                payload
            )
        case {"throttlingException": payload}:
            import capo_iotsitewise.errors.throttling_exception

            return capo_iotsitewise.errors.throttling_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ResponseStream:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "accessDeniedException":
                import capo_iotsitewise.errors.access_denied_exception

                data = capo_iotsitewise.errors.access_denied_exception.deserialize_event_json(
                    message
                )
                raise capo_iotsitewise.errors.access_denied_exception.AccessDeniedException(
                    data, message=data.get("message")
                )
            case "conflictingOperationException":
                import capo_iotsitewise.errors.conflicting_operation_exception

                data = capo_iotsitewise.errors.conflicting_operation_exception.deserialize_event_json(
                    message
                )
                raise capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException(
                    data, message=data.get("message")
                )
            case "internalFailureException":
                import capo_iotsitewise.errors.internal_failure_exception

                data = capo_iotsitewise.errors.internal_failure_exception.deserialize_event_json(
                    message
                )
                raise capo_iotsitewise.errors.internal_failure_exception.InternalFailureException(
                    data, message=data.get("message")
                )
            case "invalidRequestException":
                import capo_iotsitewise.errors.invalid_request_exception

                data = capo_iotsitewise.errors.invalid_request_exception.deserialize_event_json(
                    message
                )
                raise capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException(
                    data, message=data.get("message")
                )
            case "limitExceededException":
                import capo_iotsitewise.errors.limit_exceeded_exception

                data = capo_iotsitewise.errors.limit_exceeded_exception.deserialize_event_json(
                    message
                )
                raise capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException(
                    data, message=data.get("message")
                )
            case "resourceNotFoundException":
                import capo_iotsitewise.errors.resource_not_found_exception

                data = capo_iotsitewise.errors.resource_not_found_exception.deserialize_event_json(
                    message
                )
                raise capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException(
                    data, message=data.get("message")
                )
            case "throttlingException":
                import capo_iotsitewise.errors.throttling_exception

                data = (
                    capo_iotsitewise.errors.throttling_exception.deserialize_event_json(
                        message
                    )
                )
                raise capo_iotsitewise.errors.throttling_exception.ThrottlingException(
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
        case "trace":
            import capo_iotsitewise.types.trace

            return {
                "trace": capo_iotsitewise.types.trace.deserialize_event_json(message)
            }
        case "output":
            import capo_iotsitewise.types.invocation_output

            return {
                "output": capo_iotsitewise.types.invocation_output.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
