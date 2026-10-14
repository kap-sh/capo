"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mwaa_serverless.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.error_message
    import capo_mwaa_serverless.types.validation_exception_fields
    import capo_mwaa_serverless.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "capo_mwaa_serverless.types.error_message.ErrorMessage"
    reason: "capo_mwaa_serverless.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason the request failed validation.</p>"""
    field_list: NotRequired[
        "capo_mwaa_serverless.types.validation_exception_fields.ValidationExceptionFields"
    ]
    """<p>The fields that failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_mwaa_serverless.types.validation_exception_reason

    out["Reason"] = (
        capo_mwaa_serverless.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "field_list" in value:
        import capo_mwaa_serverless.types.validation_exception_fields

        out["FieldList"] = (
            capo_mwaa_serverless.types.validation_exception_fields.serialize_aws_json_1_0(
                value["field_list"]
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
        import capo_mwaa_serverless.types.validation_exception_reason

        out["reason"] = (
            capo_mwaa_serverless.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if data.get("FieldList") is not None:
        import capo_mwaa_serverless.types.validation_exception_fields

        out["field_list"] = (
            capo_mwaa_serverless.types.validation_exception_fields.deserialize_aws_json_1_0(
                data["FieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mwaaserverless#ValidationException``."""

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
