"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ResponseStream``."""

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
    import capo_bedrock_runtime.types.payload_part


class _ResponseStream_chunk(TypedDict, closed=True):
    chunk: "capo_bedrock_runtime.types.payload_part.PayloadPart"


class _ResponseStream_internalServerException(TypedDict, closed=True):
    internalServerException: (
        "capo_bedrock_runtime.errors.internal_server_exception.InternalServerException_"
    )


class _ResponseStream_modelStreamErrorException(TypedDict, closed=True):
    modelStreamErrorException: "capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException_"


class _ResponseStream_validationException(TypedDict, closed=True):
    validationException: (
        "capo_bedrock_runtime.errors.validation_exception.ValidationException_"
    )


class _ResponseStream_throttlingException(TypedDict, closed=True):
    throttlingException: (
        "capo_bedrock_runtime.errors.throttling_exception.ThrottlingException_"
    )


class _ResponseStream_modelTimeoutException(TypedDict, closed=True):
    modelTimeoutException: (
        "capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException_"
    )


class _ResponseStream_serviceUnavailableException(TypedDict, closed=True):
    serviceUnavailableException: "capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException_"


_ResponseStream: TypeAlias = (
    _ResponseStream_chunk
    | _ResponseStream_internalServerException
    | _ResponseStream_modelStreamErrorException
    | _ResponseStream_validationException
    | _ResponseStream_throttlingException
    | _ResponseStream_modelTimeoutException
    | _ResponseStream_serviceUnavailableException
)
ResponseStream: TypeAlias = AnyIterator[_ResponseStream]


def serialize_event_json(value: _ResponseStream) -> bytes:
    match value:
        case {"chunk": payload}:
            import capo_bedrock_runtime.types.payload_part

            return capo_bedrock_runtime.types.payload_part.serialize_event_json(payload)
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
            raise ValueError(f"ResponseStream: unrecognized variant {value!r}")


def deserialize_event_json(message: Message) -> _ResponseStream:
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
            import capo_bedrock_runtime.types.payload_part

            return {
                "chunk": capo_bedrock_runtime.types.payload_part.deserialize_event_json(
                    message
                )
            }
        case _:
            raise ValueError(f"ResponseStream: unrecognized event-type {event_type!r}")
