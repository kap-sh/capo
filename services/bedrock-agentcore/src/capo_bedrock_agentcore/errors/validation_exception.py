"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ValidationException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agentcore.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.validation_exception_field_list
    import capo_bedrock_agentcore.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_bedrock_agentcore.types.validation_exception_reason.ValidationExceptionReason"
    field_list: NotRequired[
        "capo_bedrock_agentcore.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_bedrock_agentcore.types.validation_exception_reason

    out["reason"] = (
        capo_bedrock_agentcore.types.validation_exception_reason.serialize_json(
            value["reason"]
        )
    )
    if "field_list" in value:
        import capo_bedrock_agentcore.types.validation_exception_field_list

        out["fieldList"] = (
            capo_bedrock_agentcore.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("reason") is not None:
        import capo_bedrock_agentcore.types.validation_exception_reason

        out["reason"] = (
            capo_bedrock_agentcore.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if data.get("fieldList") is not None:
        import capo_bedrock_agentcore.types.validation_exception_field_list

        out["field_list"] = (
            capo_bedrock_agentcore.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ValidationException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: ValidationException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "validationException",
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
