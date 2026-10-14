"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.validation_exception_error_list
    import capo_partnercentral_selling.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_selling.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The primary reason for this validation exception to occur.</p> <ul> <li> <p> <i>REQUEST_VALIDATION_FAILED:</i> The request format is not valid.</p> <p>Fix: Verify your request payload includes all required fields, uses correct data types and string formats.</p> </li> <li> <p> <i>BUSINESS_VALIDATION_FAILED:</i> The requested change doesn't pass the business validation rules.</p> <p>Fix: Check that your change aligns with the business rules defined by AWS Partner Central.</p> </li> </ul>"""
    error_list: NotRequired[
        "capo_partnercentral_selling.types.validation_exception_error_list.ValidationExceptionErrorList"
    ]
    """<p>A list of issues that were discovered in the submitted request or the resource state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_selling.types.validation_exception_reason

    out["Reason"] = (
        capo_partnercentral_selling.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "error_list" in value:
        import capo_partnercentral_selling.types.validation_exception_error_list

        out["ErrorList"] = (
            capo_partnercentral_selling.types.validation_exception_error_list.serialize_aws_json_1_0(
                value["error_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if data.get("Reason") is not None:
        import capo_partnercentral_selling.types.validation_exception_reason

        out["reason"] = (
            capo_partnercentral_selling.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if data.get("ErrorList") is not None:
        import capo_partnercentral_selling.types.validation_exception_error_list

        out["error_list"] = (
            capo_partnercentral_selling.types.validation_exception_error_list.deserialize_aws_json_1_0(
                data["ErrorList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralselling#ValidationException``."""

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
