"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordHistoryPolicyViolationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class PasswordHistoryPolicyViolationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PasswordHistoryPolicyViolationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PasswordHistoryPolicyViolationException_:
    out: PasswordHistoryPolicyViolationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class PasswordHistoryPolicyViolationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#PasswordHistoryPolicyViolationException``."""

    code: str | None = "PasswordHistoryPolicyViolationException"

    def __init__(
        self,
        data: PasswordHistoryPolicyViolationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PasswordHistoryPolicyViolationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PasswordHistoryPolicyViolationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
