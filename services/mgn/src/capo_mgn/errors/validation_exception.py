"""Generated from Smithy shape ``com.amazonaws.mgn#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import ServiceError

if TYPE_CHECKING:
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.validation_exception_field_list
    import capo_mgn.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    reason: NotRequired[
        "capo_mgn.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>Validate exception reason.</p>"""
    field_list: NotRequired[
        "capo_mgn.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>Validate exception field list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "field_list" in value:
        import capo_mgn.types.validation_exception_field_list

        out["fieldList"] = (
            capo_mgn.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("fieldList") is not None:
        import capo_mgn.types.validation_exception_field_list

        out["field_list"] = (
            capo_mgn.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#ValidationException``."""

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
