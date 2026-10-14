"""Generated from Smithy shape ``com.amazonaws.billing#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_billing.types.error_message
    import capo_billing.types.validation_exception_field_list
    import capo_billing.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_billing.types.error_message.ErrorMessage"
    reason: "capo_billing.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>"""
    field_list: NotRequired[
        "capo_billing.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_billing.types.validation_exception_reason

    out["reason"] = (
        capo_billing.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "field_list" in value:
        import capo_billing.types.validation_exception_field_list

        out["fieldList"] = (
            capo_billing.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["field_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("reason") is not None:
        import capo_billing.types.validation_exception_reason

        out["reason"] = (
            capo_billing.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if data.get("fieldList") is not None:
        import capo_billing.types.validation_exception_field_list

        out["field_list"] = (
            capo_billing.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billing#ValidationException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
