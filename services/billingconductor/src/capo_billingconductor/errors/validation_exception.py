"""Generated from Smithy shape ``com.amazonaws.billingconductor#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import ServiceError

if TYPE_CHECKING:
    import capo_billingconductor.types.string
    import capo_billingconductor.types.validation_exception_field_list
    import capo_billingconductor.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_billingconductor.types.string.String"
    reason: NotRequired[
        "capo_billingconductor.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason the request's validation failed. </p>"""
    fields: NotRequired[
        "capo_billingconductor.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The fields that caused the error, if applicable. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_billingconductor.types.validation_exception_reason

        out["Reason"] = (
            capo_billingconductor.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_billingconductor.types.validation_exception_field_list

        out["Fields"] = (
            capo_billingconductor.types.validation_exception_field_list.serialize_json(
                value["fields"]
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
        import capo_billingconductor.types.validation_exception_reason

        out["reason"] = (
            capo_billingconductor.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    if data.get("Fields") is not None:
        import capo_billingconductor.types.validation_exception_field_list

        out["fields"] = (
            capo_billingconductor.types.validation_exception_field_list.deserialize_json(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billingconductor#ValidationException``."""

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
