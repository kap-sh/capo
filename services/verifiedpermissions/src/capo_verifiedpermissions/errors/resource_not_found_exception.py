"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    resource_id: "str"
    """<p>The unique ID of the resource referenced in the failed request.</p>"""
    resource_type: "capo_verifiedpermissions.types.resource_type.ResourceType"
    """<p>The resource type of the resource referenced in the failed request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    import capo_verifiedpermissions.types.resource_type

    out["resourceType"] = (
        capo_verifiedpermissions.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceNotFoundException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_id required")
    if data.get("resourceType") is not None:
        import capo_verifiedpermissions.types.resource_type

        out["resource_type"] = (
            capo_verifiedpermissions.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("ResourceNotFoundException_.resource_type required")
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.verifiedpermissions#ResourceNotFoundException``."""

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
