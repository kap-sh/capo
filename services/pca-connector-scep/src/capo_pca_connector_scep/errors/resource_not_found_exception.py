"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ResourceNotFoundException``."""

import zapros
from typing_extensions import TypedDict

from capo_pca_connector_scep.errors import ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    resource_id: "str"
    """<p>The identifier of the Amazon Web Services resource.</p>"""
    resource_type: "str"
    """<p>The resource type, which can be either <code>Connector</code> or <code>Challenge</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pcaconnectorscep#ResourceNotFoundException``."""

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
