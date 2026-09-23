"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime._iter import AnyIterator
from capo_bedrock_runtime._protocol.eventstream import Message
from capo_bedrock_runtime.errors import (
    UnknownServiceError,
)

if TYPE_CHECKING:
    import capo_bedrock_runtime.errors.internal_server_exception
    import capo_bedrock_runtime.errors.model_stream_error_exception
    import capo_bedrock_runtime.errors.model_timeout_exception
    import capo_bedrock_runtime.errors.service_unavailable_exception
    import capo_bedrock_runtime.errors.throttling_exception
    import capo_bedrock_runtime.errors.validation_exception
    import capo_bedrock_runtime.types.bidirectional_output_payload_part


class _InvokeModelWithBidirectionalStreamOutput_chunk(TypedDict, closed=True):
    chunk: "capo_bedrock_runtime.types.bidirectional_output_payload_part.BidirectionalOutputPayloadPart"


class _InvokeModelWithBidirectionalStreamOutput_internalServerException(
    TypedDict, closed=True
):
    internalServerException: (
        "capo_bedrock_runtime.errors.internal_server_exception.InternalServerException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_modelStreamErrorException(
    TypedDict, closed=True
):
    modelStreamErrorException: "capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _InvokeModelWithBidirectionalStreamOutput_validationException(
    TypedDict, closed=True
):
    validationException: (
        "capo_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_throttlingException(
    TypedDict, closed=True
):
    throttlingException: (
        "capo_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_modelTimeoutException(
    TypedDict, closed=True
):
    modelTimeoutException: (
        "capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException_"
    )


class _InvokeModelWithBidirectionalStreamOutput_serviceUnavailableException(
    TypedDict, closed=True
):
    serviceUnavailableException: "capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


_InvokeModelWithBidirectionalStreamOutput: TypeAlias = (
    _InvokeModelWithBidirectionalStreamOutput_chunk
    | _InvokeModelWithBidirectionalStreamOutput_internalServerException
    | _InvokeModelWithBidirectionalStreamOutput_modelStreamErrorException
    | _InvokeModelWithBidirectionalStreamOutput_validationException
    | _InvokeModelWithBidirectionalStreamOutput_throttlingException
    | _InvokeModelWithBidirectionalStreamOutput_modelTimeoutException
    | _InvokeModelWithBidirectionalStreamOutput_serviceUnavailableException
)
InvokeModelWithBidirectionalStreamOutput: TypeAlias = AnyIterator[
    _InvokeModelWithBidirectionalStreamOutput
]


def serialize_event_json(value: _InvokeModelWithBidirectionalStreamOutput) -> bytes:
    match value:
        case {"chunk": payload}:
            import capo_bedrock_runtime.types.bidirectional_output_payload_part

            return capo_bedrock_runtime.types.bidirectional_output_payload_part.serialize_event_json(
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
        case {"modelTimeoutException": payload}:
            import capo_bedrock_runtime.errors.model_timeout_exception

            return capo_bedrock_runtime.errors.model_timeout_exception.serialize_event_json(
                payload
            )
        case {"serviceUnavailableException": payload}:
            import capo_bedrock_runtime.errors.service_unavailable_exception

            return capo_bedrock_runtime.errors.service_unavailable_exception.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamOutput: unrecognized variant {value!r}"
            )


def deserialize_event_json(
    message: Message,
) -> _InvokeModelWithBidirectionalStreamOutput:
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
                    data, message=data.get("message")
                )
            case "modelStreamErrorException":
                import capo_bedrock_runtime.errors.model_stream_error_exception

                data = capo_bedrock_runtime.errors.model_stream_error_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException(
                    data, message=data.get("message")
                )
            case "validationException":
                import capo_bedrock_runtime.errors.validation_exception

                data = capo_bedrock_runtime.errors.validation_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.validation_exception.ValidationException(
                    data, message=data.get("message")
                )
            case "throttlingException":
                import capo_bedrock_runtime.errors.throttling_exception

                data = capo_bedrock_runtime.errors.throttling_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.throttling_exception.ThrottlingException(
                    data, message=data.get("message")
                )
            case "modelTimeoutException":
                import capo_bedrock_runtime.errors.model_timeout_exception

                data = capo_bedrock_runtime.errors.model_timeout_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException(
                    data, message=data.get("message")
                )
            case "serviceUnavailableException":
                import capo_bedrock_runtime.errors.service_unavailable_exception

                data = capo_bedrock_runtime.errors.service_unavailable_exception.deserialize_event_json(
                    message
                )
                raise capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException(
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
            import capo_bedrock_runtime.types.bidirectional_output_payload_part

            return {
                "chunk": capo_bedrock_runtime.types.bidirectional_output_payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(
                f"InvokeModelWithBidirectionalStreamOutput: unrecognized event-type {event_type!r}"
            )
