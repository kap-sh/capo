"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ResourceNotFoundException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import ServiceError


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_id: NotRequired["str"]
    """<p> The identifier of the resource which could not be found. </p>"""
    resource_type: NotRequired["str"]
    """<p> The type of the resource which could not be found. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.observabilityadmin#ResourceNotFoundException``."""

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
