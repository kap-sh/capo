"""Generated from Smithy shape ``com.amazonaws.glue#FederatedResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.glue_resource_arn
    import capo_glue.types.message_string


class FederatedResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>The message describing the problem.</p>"""
    associated_glue_resource: NotRequired[
        "capo_glue.types.glue_resource_arn.GlueResourceArn"
    ]
    """<p>The associated Glue resource already exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederatedResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "associated_glue_resource" in value:
        out["AssociatedGlueResource"] = value["associated_glue_resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FederatedResourceAlreadyExistsException_:
    out: FederatedResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("AssociatedGlueResource") is not None:
        out["associated_glue_resource"] = data["AssociatedGlueResource"]
    return out


class FederatedResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#FederatedResourceAlreadyExistsException``."""

    code: str | None = "FederatedResourceAlreadyExistsException"

    def __init__(
        self,
        data: FederatedResourceAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FederatedResourceAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FederatedResourceAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
