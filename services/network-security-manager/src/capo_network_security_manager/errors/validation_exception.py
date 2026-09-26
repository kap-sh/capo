"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_network_security_manager.types.validation_exception_field_list
    import capo_network_security_manager.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: NotRequired[
        "capo_network_security_manager.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason that the request failed validation.</p>"""
    field_list: NotRequired[
        "capo_network_security_manager.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of request fields that failed validation, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import capo_network_security_manager.types.validation_exception_reason

        out["reason"] = (
            capo_network_security_manager.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "field_list" in value:
        import capo_network_security_manager.types.validation_exception_field_list

        out["fieldList"] = (
            capo_network_security_manager.types.validation_exception_field_list.serialize_json(
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
        import capo_network_security_manager.types.validation_exception_reason

        out["reason"] = (
            capo_network_security_manager.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    if data.get("fieldList") is not None:
        import capo_network_security_manager.types.validation_exception_field_list

        out["field_list"] = (
            capo_network_security_manager.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networksecuritymanager#ValidationException``."""

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
