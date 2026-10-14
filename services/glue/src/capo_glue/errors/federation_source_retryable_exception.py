"""Generated from Smithy shape ``com.amazonaws.glue#FederationSourceRetryableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class FederationSourceRetryableException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationSourceRetryableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederationSourceRetryableException_:
    out: FederationSourceRetryableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class FederationSourceRetryableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#FederationSourceRetryableException``."""

    code: str | None = "FederationSourceRetryableException"

    def __init__(
        self,
        data: FederationSourceRetryableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FederationSourceRetryableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FederationSourceRetryableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
