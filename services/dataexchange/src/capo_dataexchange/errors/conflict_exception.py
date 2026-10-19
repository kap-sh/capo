"""Generated from Smithy shape ``com.amazonaws.dataexchange#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import ServiceError

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: "capo_dataexchange.types.__string.__string"
    """<p>The request couldn't be completed because it conflicted with the current state of the resource.</p>"""
    resource_id: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The unique identifier for the resource with the conflict.</p>"""
    resource_type: NotRequired["capo_dataexchange.types.resource_type.ResourceType"]
    """<p>The type of the resource with the conflict.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dataexchange#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
