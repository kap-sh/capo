"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ManagedLoginBrandingExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class ManagedLoginBrandingExistsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedLoginBrandingExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedLoginBrandingExistsException_:
    out: ManagedLoginBrandingExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ManagedLoginBrandingExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#ManagedLoginBrandingExistsException``."""

    code: str | None = "ManagedLoginBrandingExistsException"

    def __init__(
        self,
        data: ManagedLoginBrandingExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ManagedLoginBrandingExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ManagedLoginBrandingExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
