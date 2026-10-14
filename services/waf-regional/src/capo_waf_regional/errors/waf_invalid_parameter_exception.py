"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFInvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf_regional.types.parameter_exception_field
    import capo_waf_regional.types.parameter_exception_parameter
    import capo_waf_regional.types.parameter_exception_reason


class WAFInvalidParameterException_(TypedDict, closed=True):
    field: NotRequired[
        "capo_waf_regional.types.parameter_exception_field.ParameterExceptionField"
    ]
    parameter: NotRequired[
        "capo_waf_regional.types.parameter_exception_parameter.ParameterExceptionParameter"
    ]
    reason: NotRequired[
        "capo_waf_regional.types.parameter_exception_reason.ParameterExceptionReason"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidParameterException_) -> dict:
    out: dict = {}
    if "field" in value:
        import capo_waf_regional.types.parameter_exception_field

        out["field"] = (
            capo_waf_regional.types.parameter_exception_field.serialize_aws_json_1_1(
                value["field"]
            )
        )
    if "parameter" in value:
        out["parameter"] = value["parameter"]
    if "reason" in value:
        import capo_waf_regional.types.parameter_exception_reason

        out["reason"] = (
            capo_waf_regional.types.parameter_exception_reason.serialize_aws_json_1_1(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidParameterException_:
    out: WAFInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        import capo_waf_regional.types.parameter_exception_field

        out["field"] = (
            capo_waf_regional.types.parameter_exception_field.deserialize_aws_json_1_1(
                data["field"]
            )
        )
    if data.get("parameter") is not None:
        out["parameter"] = data["parameter"]
    if data.get("reason") is not None:
        import capo_waf_regional.types.parameter_exception_reason

        out["reason"] = (
            capo_waf_regional.types.parameter_exception_reason.deserialize_aws_json_1_1(
                data["reason"]
            )
        )
    return out


class WAFInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFInvalidParameterException``."""

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
