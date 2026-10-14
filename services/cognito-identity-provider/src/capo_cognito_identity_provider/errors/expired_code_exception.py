"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ExpiredCodeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class ExpiredCodeException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the expired code exception is thrown.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpiredCodeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpiredCodeException_:
    out: ExpiredCodeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ExpiredCodeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#ExpiredCodeException``."""

    code: str | None = "ExpiredCodeException"

    def __init__(
        self,
        data: ExpiredCodeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredCodeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExpiredCodeException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
