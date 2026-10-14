"""Generated from Smithy shape ``com.amazonaws.transfer#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_transfer.types.message
    import capo_transfer.types.resource
    import capo_transfer.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_transfer.types.message.Message"
    resource: "capo_transfer.types.resource.Resource"
    resource_type: "capo_transfer.types.resource_type.ResourceType"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["Resource"] = value["resource"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource required")
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transfer#ResourceNotFoundException``."""

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
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
