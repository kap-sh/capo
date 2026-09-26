"""Generated from Smithy shape ``com.amazonaws.agentregistry#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_agent_registry.types.validation_exception_field_list
    import capo_agent_registry.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_agent_registry.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason the request failed validation.</p>"""
    field_list: NotRequired[
        "capo_agent_registry.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of input fields that failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_agent_registry.types.validation_exception_reason

    out["reason"] = (
        capo_agent_registry.types.validation_exception_reason.serialize_json(
            value.get("reason", "FieldValidationFailed")
        )
    )
    if "field_list" in value:
        import capo_agent_registry.types.validation_exception_field_list

        out["fieldList"] = (
            capo_agent_registry.types.validation_exception_field_list.serialize_json(
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
        import capo_agent_registry.types.validation_exception_reason

        out["reason"] = (
            capo_agent_registry.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        out["reason"] = "FieldValidationFailed"
    if data.get("fieldList") is not None:
        import capo_agent_registry.types.validation_exception_field_list

        out["field_list"] = (
            capo_agent_registry.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.agentregistry#ValidationException``."""

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
