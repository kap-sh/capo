"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#DeveloperUserAlreadyRegisteredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity.types.string


class DeveloperUserAlreadyRegisteredException_(TypedDict, closed=True):
    message: NotRequired["capo_cognito_identity.types.string.String"]
    """<p>This developer user identifier is already registered with Cognito.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeveloperUserAlreadyRegisteredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeveloperUserAlreadyRegisteredException_:
    out: DeveloperUserAlreadyRegisteredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DeveloperUserAlreadyRegisteredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentity#DeveloperUserAlreadyRegisteredException``."""

    code: str | None = "DeveloperUserAlreadyRegisteredException"

    def __init__(
        self,
        data: DeveloperUserAlreadyRegisteredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeveloperUserAlreadyRegisteredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DeveloperUserAlreadyRegisteredException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
