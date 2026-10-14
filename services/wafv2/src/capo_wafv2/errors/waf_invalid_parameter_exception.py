"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFInvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_wafv2.types.error_message
    import capo_wafv2.types.error_reason
    import capo_wafv2.types.parameter_exception_field
    import capo_wafv2.types.parameter_exception_parameter


class WAFInvalidParameterException_(TypedDict, closed=True):
    message: NotRequired["capo_wafv2.types.error_message.ErrorMessage"]
    field: NotRequired[
        "capo_wafv2.types.parameter_exception_field.ParameterExceptionField"
    ]
    """<p>The settings where the invalid parameter was found. </p>"""
    parameter: NotRequired[
        "capo_wafv2.types.parameter_exception_parameter.ParameterExceptionParameter"
    ]
    """<p>The invalid parameter that resulted in the exception. </p>"""
    reason: NotRequired["capo_wafv2.types.error_reason.ErrorReason"]
    """<p>Additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "field" in value:
        import capo_wafv2.types.parameter_exception_field

        out["Field"] = (
            capo_wafv2.types.parameter_exception_field.serialize_aws_json_1_1(
                value["field"]
            )
        )
    if "parameter" in value:
        out["Parameter"] = value["parameter"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidParameterException_:
    out: WAFInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("Field") is not None:
        import capo_wafv2.types.parameter_exception_field

        out["field"] = (
            capo_wafv2.types.parameter_exception_field.deserialize_aws_json_1_1(
                data["Field"]
            )
        )
    if data.get("Parameter") is not None:
        out["parameter"] = data["Parameter"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out


class WAFInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFInvalidParameterException``."""

    code: str | None = "WAFInvalidParameterException"

    def __init__(
        self,
        data: WAFInvalidParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInvalidParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFInvalidParameterException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
