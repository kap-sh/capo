"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#ResourceConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity.types.string


class ResourceConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_cognito_identity.types.string.String"]
    """<p>The message returned by a ResourceConflictException.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceConflictException_:
    out: ResourceConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentity#ResourceConflictException``."""

    code: str | None = "ResourceConflictException"

    def __init__(
        self,
        data: ResourceConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceConflictException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
