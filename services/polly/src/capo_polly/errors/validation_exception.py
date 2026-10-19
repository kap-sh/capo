"""Generated from Smithy shape ``com.amazonaws.polly#ValidationException``."""

import json
from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_polly._protocol.eventstream import HeaderValue, Message
from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message
    import capo_polly.types.validation_exception_field_list
    import capo_polly.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_polly.types.error_message.ErrorMessage"
    reason: "capo_polly.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason the request failed validation.</p>"""
    fields: NotRequired[
        "capo_polly.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The fields that caused the validation error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_polly.types.validation_exception_reason

    out["reason"] = capo_polly.types.validation_exception_reason.serialize_json(
        value["reason"]
    )
    if "fields" in value:
        import capo_polly.types.validation_exception_field_list

        out["fields"] = capo_polly.types.validation_exception_field_list.serialize_json(
            value["fields"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_polly.types.validation_exception_reason

        out["reason"] = capo_polly.types.validation_exception_reason.deserialize_json(
            data["reason"]
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_polly.types.validation_exception_reason.ValidationExceptionReason", ""
        )
    if data.get("fields") is not None:
        import capo_polly.types.validation_exception_field_list

        out["fields"] = (
            capo_polly.types.validation_exception_field_list.deserialize_json(
                data["fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(
        self,
        data: ValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_json(data), message, response=response)


def serialize_event_json(value: ValidationException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ValidationException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ValidationException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
