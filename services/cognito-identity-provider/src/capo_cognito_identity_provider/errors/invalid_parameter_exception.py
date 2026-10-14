"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.invalid_parameter_exception_reason_code_type
    import capo_cognito_identity_provider.types.message_type


class InvalidParameterException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the Amazon Cognito service throws an invalid parameter exception.</p>"""
    reason_code: NotRequired[
        "capo_cognito_identity_provider.types.invalid_parameter_exception_reason_code_type.InvalidParameterExceptionReasonCodeType"
    ]
    """<p>The reason code of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason_code" in value:
        out["reasonCode"] = value["reason_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reasonCode") is not None:
        out["reason_code"] = data["reasonCode"]
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidParameterException``."""

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
