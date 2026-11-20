"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.error_message


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    resource_id: NotRequired["str"]
    """The affected resource identifier."""
    resource_type: NotRequired["str"]
    """The affected resource type."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_cbor(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#ResourceNotFoundException``."""

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
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_cbor(data), message, response=response)
