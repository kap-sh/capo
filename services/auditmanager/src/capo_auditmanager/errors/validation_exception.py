"""Generated from Smithy shape ``com.amazonaws.auditmanager#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_auditmanager.errors import ServiceError

if TYPE_CHECKING:
    import capo_auditmanager.types.string
    import capo_auditmanager.types.validation_exception_field_list
    import capo_auditmanager.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_auditmanager.types.string.String"
    reason: NotRequired[
        "capo_auditmanager.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p> The reason the request failed validation. </p>"""
    fields: NotRequired[
        "capo_auditmanager.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p> The fields that caused the error, if applicable. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        import capo_auditmanager.types.validation_exception_reason

        out["reason"] = (
            capo_auditmanager.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_auditmanager.types.validation_exception_field_list

        out["fields"] = (
            capo_auditmanager.types.validation_exception_field_list.serialize_json(
                value["fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        import capo_auditmanager.types.validation_exception_reason

        out["reason"] = (
            capo_auditmanager.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    if data.get("fields") is not None:
        import capo_auditmanager.types.validation_exception_field_list

        out["fields"] = (
            capo_auditmanager.types.validation_exception_field_list.deserialize_json(
                data["fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.auditmanager#ValidationException``."""

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
