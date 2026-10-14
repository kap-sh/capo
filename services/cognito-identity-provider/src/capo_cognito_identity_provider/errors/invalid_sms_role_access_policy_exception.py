"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidSmsRoleAccessPolicyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class InvalidSmsRoleAccessPolicyException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the invalid SMS role access policy exception is thrown.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidSmsRoleAccessPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidSmsRoleAccessPolicyException_:
    out: InvalidSmsRoleAccessPolicyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidSmsRoleAccessPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#InvalidSmsRoleAccessPolicyException``."""

    code: str | None = "InvalidSmsRoleAccessPolicyException"

    def __init__(
        self,
        data: InvalidSmsRoleAccessPolicyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidSmsRoleAccessPolicyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidSmsRoleAccessPolicyException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
