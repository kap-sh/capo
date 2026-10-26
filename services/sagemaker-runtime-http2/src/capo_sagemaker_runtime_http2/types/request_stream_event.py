"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#RequestStreamEvent``."""

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
    import capo_sagemaker_runtime_http2.types.request_payload_part


class _RequestStreamEvent_PayloadPart(TypedDict, closed=True):
    PayloadPart: (
        "capo_sagemaker_runtime_http2.types.request_payload_part.RequestPayloadPart"
    )


_RequestStreamEvent: TypeAlias = _RequestStreamEvent_PayloadPart | UnknownEvent
RequestStreamEvent: TypeAlias = AnyIterator[_RequestStreamEvent]


def serialize_event_json(value: _RequestStreamEvent) -> bytes:
    match value:
        case {"$unknown": {"name": name}}:
            raise ValueError(
                f"RequestStreamEvent: cannot serialize unknown event {name!r}"
            )
        case {"PayloadPart": payload}:
            import capo_sagemaker_runtime_http2.types.request_payload_part

            return capo_sagemaker_runtime_http2.types.request_payload_part.serialize_event_json(
                payload
            )
        case _:
            raise ValueError(f"RequestStreamEvent: unrecognized variant {value!r}")


def deserialize_event_json(
    message: Message, *, response: zapros.Response
) -> _RequestStreamEvent:
    headers = message.headers
    message_type = headers.get(":message-type", "event")
    if message_type == "exception":
        exception_type = headers.get(":exception-type")
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
            import capo_sagemaker_runtime_http2.types.request_payload_part

            return {
                "PayloadPart": capo_sagemaker_runtime_http2.types.request_payload_part.deserialize_event_json(
                    message
                )
            }
        case str():
            return {"$unknown": {"name": event_type, "message": message}}
        case _:
            raise ValueError(
                f"RequestStreamEvent: unrecognized event-type {event_type!r}"
            )
