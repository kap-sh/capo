"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#ResponseStreamEvent``."""

from typing import TYPE_CHECKING, TypeAlias

import zapros
from typing_extensions import TypedDict

from capo_sagemaker_runtime_http2._iter import AnyIterator
from capo_sagemaker_runtime_http2._protocol.eventstream import Message
from capo_sagemaker_runtime_http2.errors import (
    UnknownServiceError,
)
from capo_sagemaker_runtime_http2.types._unknown import UnknownEvent

if TYPE_CHECKING:
    import capo_sagemaker_runtime_http2.errors.internal_stream_failure
    import capo_sagemaker_runtime_http2.errors.model_stream_error
    import capo_sagemaker_runtime_http2.types.response_payload_part


class ResponseStreamEventPayloadPartMember(TypedDict, closed=True):
    PayloadPart: (
        "capo_sagemaker_runtime_http2.types.response_payload_part.ResponsePayloadPart"
    )


class ResponseStreamEventModelStreamErrorMember(TypedDict, closed=True):
    ModelStreamError: (
        "capo_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError_"
    )


class ResponseStreamEventInternalStreamFailureMember(TypedDict, closed=True):
    InternalStreamFailure: "capo_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure_"


_ResponseStreamEvent: TypeAlias = (
    ResponseStreamEventPayloadPartMember
    | ResponseStreamEventModelStreamErrorMember
    | ResponseStreamEventInternalStreamFailureMember
    | UnknownEvent
)
ResponseStreamEvent: TypeAlias = AnyIterator[_ResponseStreamEvent]


def serialize_event_json(value: _ResponseStreamEvent) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"ResponseStreamEvent: cannot serialize unknown event {name!r}"
            )
        case {"PayloadPart": payload}:
            import capo_sagemaker_runtime_http2.types.response_payload_part

            return capo_sagemaker_runtime_http2.types.response_payload_part.serialize_event_json(
                payload
            )
        case {"ModelStreamError": payload}:
            import capo_sagemaker_runtime_http2.errors.model_stream_error

            return capo_sagemaker_runtime_http2.errors.model_stream_error.serialize_event_json(
                payload
            )
        case {"InternalStreamFailure": payload}:
            import capo_sagemaker_runtime_http2.errors.internal_stream_failure

            return capo_sagemaker_runtime_http2.errors.internal_stream_failure.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"ResponseStreamEvent: unrecognized variant {value!r}")


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _ResponseStreamEvent:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
        match exception_type:
            case "ModelStreamError":
                import capo_sagemaker_runtime_http2.errors.model_stream_error

                data = capo_sagemaker_runtime_http2.errors.model_stream_error.deserialize_event_json(
                    message
                )
                raise capo_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError(
                    data, message=data.get("message"), response=response
                )
            case "InternalStreamFailure":
                import capo_sagemaker_runtime_http2.errors.internal_stream_failure

                data = capo_sagemaker_runtime_http2.errors.internal_stream_failure.deserialize_event_json(
                    message
                )
                raise capo_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure(
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
        case "PayloadPart":
            import capo_sagemaker_runtime_http2.types.response_payload_part

            return {
                "PayloadPart": capo_sagemaker_runtime_http2.types.response_payload_part.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(
                f"ResponseStreamEvent: unrecognized event-type {event_type!r}"
            )
