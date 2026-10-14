"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_type_not_found


class ResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_type_not_found: NotRequired[
        "capo_mediapackagev2.types.resource_type_not_found.ResourceTypeNotFound"
    ]
    """<p>The specified resource type wasn't found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type_not_found" in value:
        import capo_mediapackagev2.types.resource_type_not_found

        out["ResourceTypeNotFound"] = (
            capo_mediapackagev2.types.resource_type_not_found.serialize_json(
                value["resource_type_not_found"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceTypeNotFound") is not None:
        import capo_mediapackagev2.types.resource_type_not_found

        out["resource_type_not_found"] = (
            capo_mediapackagev2.types.resource_type_not_found.deserialize_json(
                data["ResourceTypeNotFound"]
            )
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediapackagev2#ResourceNotFoundException``."""

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
