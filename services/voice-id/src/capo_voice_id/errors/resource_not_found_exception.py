"""Generated from Smithy shape ``com.amazonaws.voiceid#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import ServiceError

if TYPE_CHECKING:
    import capo_voice_id.types.resource_type
    import capo_voice_id.types.string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_voice_id.types.string.String"]
    resource_type: NotRequired["capo_voice_id.types.resource_type.ResourceType"]
    """<p>The type of resource which cannot not be found. Possible types are <code>BATCH_JOB</code>, <code>COMPLIANCE_CONSENT</code>, <code>DOMAIN</code>, <code>FRAUDSTER</code>, <code>SESSION</code> and <code>SPEAKER</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.voiceid#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(
        self,
        data: ResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
