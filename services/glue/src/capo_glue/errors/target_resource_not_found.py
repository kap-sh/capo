"""Generated from Smithy shape ``com.amazonaws.glue#TargetResourceNotFound``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.integration_error_message


class TargetResourceNotFound_(TypedDict, closed=True):
    message: NotRequired[
        "capo_glue.types.integration_error_message.IntegrationErrorMessage"
    ]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetResourceNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetResourceNotFound_:
    out: TargetResourceNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TargetResourceNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#TargetResourceNotFound``."""

    code: str | None = "TargetResourceNotFound"

    def __init__(
        self,
        data: TargetResourceNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TargetResourceNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TargetResourceNotFound":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
