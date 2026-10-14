"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ExternalServiceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity.types.string


class ExternalServiceException_(TypedDict, closed=True):
    message: NotRequired["capo_cognito_identity.types.string.String"]
    """<p>The message returned by an ExternalServiceException</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalServiceException_:
    out: ExternalServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ExternalServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentity#ExternalServiceException``."""

    code: str | None = "ExternalServiceException"

    def __init__(
        self,
        data: ExternalServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExternalServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExternalServiceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
