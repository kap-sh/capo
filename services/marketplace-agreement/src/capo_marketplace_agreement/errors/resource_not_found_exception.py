"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.exception_message
    import capo_marketplace_agreement.types.request_id
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    request_id: NotRequired["capo_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "capo_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""
    resource_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier for the resource.</p>"""
    resource_type: NotRequired[
        "capo_marketplace_agreement.types.resource_type.ResourceType"
    ]
    """<p>The type of resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_marketplace_agreement.types.resource_type

        out["resourceType"] = (
            capo_marketplace_agreement.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        import capo_marketplace_agreement.types.resource_type

        out["resource_type"] = (
            capo_marketplace_agreement.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#ResourceNotFoundException``."""

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
