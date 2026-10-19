"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.string
    import capo_ssm_contacts.types.validation_exception_field_list
    import capo_ssm_contacts.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_ssm_contacts.types.string.String"
    reason: NotRequired[
        "capo_ssm_contacts.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """Reason the request failed validation"""
    fields: NotRequired[
        "capo_ssm_contacts.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """The fields that caused the error"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_ssm_contacts.types.validation_exception_reason

        out["Reason"] = (
            capo_ssm_contacts.types.validation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_ssm_contacts.types.validation_exception_field_list

        out["Fields"] = (
            capo_ssm_contacts.types.validation_exception_field_list.serialize_aws_json_1_1(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_ssm_contacts.types.validation_exception_reason

        out["reason"] = (
            capo_ssm_contacts.types.validation_exception_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    if data.get("Fields") is not None:
        import capo_ssm_contacts.types.validation_exception_field_list

        out["fields"] = (
            capo_ssm_contacts.types.validation_exception_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#ValidationException``."""

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
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ValidationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
