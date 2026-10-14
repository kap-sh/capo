"""Generated from Smithy shape ``com.amazonaws.shield#InvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import ServiceError

if TYPE_CHECKING:
    import capo_shield.types.error_message
    import capo_shield.types.validation_exception_field_list
    import capo_shield.types.validation_exception_reason


class InvalidParameterException_(TypedDict, closed=True):
    message: NotRequired["capo_shield.types.error_message.errorMessage"]
    reason: NotRequired[
        "capo_shield.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>Additional information about the exception.</p>"""
    fields: NotRequired[
        "capo_shield.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>Fields that caused the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_shield.types.validation_exception_reason

        out["reason"] = (
            capo_shield.types.validation_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    if "fields" in value:
        import capo_shield.types.validation_exception_field_list

        out["fields"] = (
            capo_shield.types.validation_exception_field_list.serialize_aws_json_1_1(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        import capo_shield.types.validation_exception_reason

        out["reason"] = (
            capo_shield.types.validation_exception_reason.deserialize_aws_json_1_1(
                data["reason"]
            )
        )
    if data.get("fields") is not None:
        import capo_shield.types.validation_exception_field_list

        out["fields"] = (
            capo_shield.types.validation_exception_field_list.deserialize_aws_json_1_1(
                data["fields"]
            )
        )
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(
        self,
        data: InvalidParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParameterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
