"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connectparticipant.errors import ServiceError

if TYPE_CHECKING:
    import capo_connectparticipant.types.message
    import capo_connectparticipant.types.resource_id
    import capo_connectparticipant.types.resource_type


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_connectparticipant.types.message.Message"]
    resource_id: NotRequired["capo_connectparticipant.types.resource_id.ResourceId"]
    """<p>The identifier of the resource.</p>"""
    resource_type: NotRequired[
        "capo_connectparticipant.types.resource_type.ResourceType"
    ]
    """<p>The type of Connect Customer resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        import capo_connectparticipant.types.resource_type

        out["ResourceType"] = (
            capo_connectparticipant.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        import capo_connectparticipant.types.resource_type

        out["resource_type"] = (
            capo_connectparticipant.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectparticipant#ResourceNotFoundException``."""

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
