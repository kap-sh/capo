"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DuplicateProviderException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class DuplicateProviderException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateProviderException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateProviderException_:
    out: DuplicateProviderException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DuplicateProviderException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#DuplicateProviderException``."""

    code: str | None = "DuplicateProviderException"

    def __init__(
        self,
        data: DuplicateProviderException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateProviderException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateProviderException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
