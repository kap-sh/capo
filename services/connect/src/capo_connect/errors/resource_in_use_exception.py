"""Generated from Smithy shape ``com.amazonaws.connect#ResourceInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.message
    import capo_connect.types.resource_type


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]
    resource_type: NotRequired["capo_connect.types.resource_type.ResourceType"]
    """<p>The type of resource.</p>"""
    resource_id: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The identifier for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        import capo_connect.types.resource_type

        out["ResourceType"] = capo_connect.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceType") is not None:
        import capo_connect.types.resource_type

        out["resource_type"] = capo_connect.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(
        self,
        data: ResourceInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceInUseException":
        return cls(deserialize_json(data), message, response=response)
