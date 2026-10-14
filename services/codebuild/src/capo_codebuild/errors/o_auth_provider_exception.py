"""Generated from Smithy shape ``com.amazonaws.codebuild#OAuthProviderException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import ServiceError

if TYPE_CHECKING:
    import capo_codebuild.types.string


class OAuthProviderException_(TypedDict, closed=True):
    message: NotRequired["capo_codebuild.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuthProviderException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OAuthProviderException_:
    out: OAuthProviderException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class OAuthProviderException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codebuild#OAuthProviderException``."""

    code: str | None = "OAuthProviderException"

    def __init__(
        self,
        data: OAuthProviderException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OAuthProviderException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OAuthProviderException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
