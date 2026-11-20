"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connectscheduling.errors import ServiceError

if TYPE_CHECKING:
    import capo_connectscheduling.types.message
    import capo_connectscheduling.types.validation_exception_field_list
    import capo_connectscheduling.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_connectscheduling.types.message.Message"
    reason: NotRequired[
        "capo_connectscheduling.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason the input failed validation. Branch on this value rather than on the message wording.</p>"""
    field_list: NotRequired[
        "capo_connectscheduling.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The specific input fields that failed validation, when <code>Reason</code> is <code>FIELD_VALIDATION_FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_connectscheduling.types.validation_exception_reason

        out["Reason"] = (
            capo_connectscheduling.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "field_list" in value:
        import capo_connectscheduling.types.validation_exception_field_list

        out["FieldList"] = (
            capo_connectscheduling.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_connectscheduling.types.validation_exception_reason

        out["reason"] = (
            capo_connectscheduling.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    if data.get("FieldList") is not None:
        import capo_connectscheduling.types.validation_exception_field_list

        out["field_list"] = (
            capo_connectscheduling.types.validation_exception_field_list.deserialize_json(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectscheduling#ValidationException``."""

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
