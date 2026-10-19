"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_application_signals.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_signals.types.fault_description
    import capo_application_signals.types.resource_id
    import capo_application_signals.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    resource_type: "capo_application_signals.types.resource_type.ResourceType"
    """<p>The resource type is not valid.</p>"""
    resource_id: "capo_application_signals.types.resource_id.ResourceId"
    """<p>Can't find the resource id.</p>"""
    message: "capo_application_signals.types.fault_description.FaultDescription"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    out["ResourceId"] = value["resource_id"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationsignals#ResourceNotFoundException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_json(data), message, response=response)
