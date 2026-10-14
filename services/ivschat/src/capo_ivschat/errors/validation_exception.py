"""Generated from Smithy shape ``com.amazonaws.ivschat#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ivschat.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ivschat.types.error_message
    import capo_ivschat.types.validation_exception_field_list
    import capo_ivschat.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_ivschat.types.error_message.ErrorMessage"
    reason: "capo_ivschat.types.validation_exception_reason.ValidationExceptionReason"
    """<p/>"""
    field_list: NotRequired[
        "capo_ivschat.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["reason"] = value["reason"]
    if "field_list" in value:
        import capo_ivschat.types.validation_exception_field_list

        out["fieldList"] = (
            capo_ivschat.types.validation_exception_field_list.serialize_json(
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
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("ValidationException_.reason required")
    if data.get("fieldList") is not None:
        import capo_ivschat.types.validation_exception_field_list

        out["field_list"] = (
            capo_ivschat.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivschat#ValidationException``."""

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
