"""Generated from Smithy shape ``com.amazonaws.drs#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import ServiceError

if TYPE_CHECKING:
    import capo_drs.types.large_bounded_string


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    resource_id: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>The type of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.drs#ResourceNotFoundException``."""

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
