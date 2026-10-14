"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserImportInProgressException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class UserImportInProgressException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when the user pool has an import job running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserImportInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserImportInProgressException_:
    out: UserImportInProgressException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UserImportInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#UserImportInProgressException``."""

    code: str | None = "UserImportInProgressException"

    def __init__(
        self,
        data: UserImportInProgressException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UserImportInProgressException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UserImportInProgressException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
