"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.validation_exception_field_list
    import capo_pinpoint_sms_voice_v2.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""
    fields: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The field that failed validation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "fields" in value:
        import capo_pinpoint_sms_voice_v2.types.validation_exception_field_list

        out["Fields"] = (
            capo_pinpoint_sms_voice_v2.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["fields"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("Fields") is not None:
        import capo_pinpoint_sms_voice_v2.types.validation_exception_field_list

        out["fields"] = (
            capo_pinpoint_sms_voice_v2.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ValidationException``."""

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
