"""Generated from Smithy shape ``com.amazonaws.route53profiles#ResourceExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53profiles.errors import ServiceError

if TYPE_CHECKING:
    import capo_route53profiles.types.string


class ResourceExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_route53profiles.types.string.String"]
    resource_type: NotRequired["capo_route53profiles.types.string.String"]
    """<p> The resource type that caused the resource exists exception. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceExistsException_:
    out: ResourceExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53profiles#ResourceExistsException``."""

    code: str | None = "ResourceExistsException"

    def __init__(
        self,
        data: ResourceExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceExistsException":
        return cls(deserialize_json(data), message, response=response)
