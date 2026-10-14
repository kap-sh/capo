"""Generated from Smithy shape ``com.amazonaws.iotevents#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_events.types.error_message
    import capo_iot_events.types.resource_arn
    import capo_iot_events.types.resource_id


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_events.types.error_message.errorMessage"]
    """<p>The message for the exception.</p>"""
    resource_id: NotRequired["capo_iot_events.types.resource_id.resourceId"]
    """<p>The ID of the resource.</p>"""
    resource_arn: NotRequired["capo_iot_events.types.resource_arn.resourceArn"]
    """<p>The ARN of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotevents#ResourceAlreadyExistsException``."""

    code: str | None = "ResourceAlreadyExistsException"

    def __init__(
        self,
        data: ResourceAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceAlreadyExistsException":
        return cls(deserialize_json(data), message, response=response)
