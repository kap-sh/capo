"""Generated from Smithy shape ``com.amazonaws.invoicing#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import ServiceError

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.invoice_unit_arn_string
    import capo_invoicing.types.validation_exception_field_list
    import capo_invoicing.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    resource_name: NotRequired[
        "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    ]
    """<p>You don't have sufficient access to perform this action. </p>"""
    reason: NotRequired[
        "capo_invoicing.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>You don't have sufficient access to perform this action. </p>"""
    field_list: NotRequired[
        "capo_invoicing.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p> The input fails to satisfy the constraints specified by an Amazon Web Services service. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "reason" in value:
        import capo_invoicing.types.validation_exception_reason

        out["reason"] = (
            capo_invoicing.types.validation_exception_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    if "field_list" in value:
        import capo_invoicing.types.validation_exception_field_list

        out["fieldList"] = (
            capo_invoicing.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["field_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("reason") is not None:
        import capo_invoicing.types.validation_exception_reason

        out["reason"] = (
            capo_invoicing.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    if data.get("fieldList") is not None:
        import capo_invoicing.types.validation_exception_field_list

        out["field_list"] = (
            capo_invoicing.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.invoicing#ValidationException``."""

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
