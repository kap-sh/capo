"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_jobs_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.error_message
    import capo_iot_jobs_data_plane.types.resource_id


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_jobs_data_plane.types.error_message.errorMessage"]
    resource_id: NotRequired["capo_iot_jobs_data_plane.types.resource_id.resourceId"]
    """<p>A conflict occurred while performing the API request on the resource ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotjobsdataplane#ConflictException``."""

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
