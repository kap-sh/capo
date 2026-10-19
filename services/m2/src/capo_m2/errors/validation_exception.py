"""Generated from Smithy shape ``com.amazonaws.m2#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import ServiceError

if TYPE_CHECKING:
    import capo_m2.types.validation_exception_field_list
    import capo_m2.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: NotRequired[
        "capo_m2.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason why it failed service validation.</p>"""
    field_list: NotRequired[
        "capo_m2.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The list of fields that failed service validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "field_list" in value:
        import capo_m2.types.validation_exception_field_list

        out["fieldList"] = capo_m2.types.validation_exception_field_list.serialize_json(
            value["field_list"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("fieldList") is not None:
        import capo_m2.types.validation_exception_field_list

        out["field_list"] = (
            capo_m2.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.m2#ValidationException``."""

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
