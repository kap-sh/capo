"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.validation_error_list
    import capo_partnercentral_account.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_account.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason for the validation failure.</p>"""
    error_details: NotRequired[
        "capo_partnercentral_account.types.validation_error_list.ValidationErrorList"
    ]
    """<p>A list of detailed validation errors that occurred during request processing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_account.types.validation_exception_reason

    out["Reason"] = (
        capo_partnercentral_account.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "error_details" in value:
        import capo_partnercentral_account.types.validation_error_list

        out["ErrorDetails"] = (
            capo_partnercentral_account.types.validation_error_list.serialize_aws_json_1_0(
                value["error_details"]
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
        import capo_partnercentral_account.types.validation_exception_reason

        out["reason"] = (
            capo_partnercentral_account.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if data.get("ErrorDetails") is not None:
        import capo_partnercentral_account.types.validation_error_list

        out["error_details"] = (
            capo_partnercentral_account.types.validation_error_list.deserialize_aws_json_1_0(
                data["ErrorDetails"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#ValidationException``."""

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
