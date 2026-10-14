"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolAddOnNotEnabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class UserPoolAddOnNotEnabledException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolAddOnNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolAddOnNotEnabledException_:
    out: UserPoolAddOnNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UserPoolAddOnNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolAddOnNotEnabledException``."""

    code: str | None = "UserPoolAddOnNotEnabledException"

    def __init__(
        self,
        data: UserPoolAddOnNotEnabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserPoolAddOnNotEnabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UserPoolAddOnNotEnabledException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
