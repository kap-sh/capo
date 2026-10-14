"""Generated from Smithy shape ``com.amazonaws.ivschat#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ivschat.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ivschat.types.error_message
    import capo_ivschat.types.limit
    import capo_ivschat.types.resource_id
    import capo_ivschat.types.resource_type


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_ivschat.types.error_message.ErrorMessage"
    resource_id: "capo_ivschat.types.resource_id.ResourceId"
    """<p/>"""
    resource_type: "capo_ivschat.types.resource_type.ResourceType"
    """<p/>"""
    limit: "capo_ivschat.types.limit.Limit"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    out["limit"] = value.get("limit", 0)
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ThrottlingException_.resource_id required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ThrottlingException_.resource_type required")
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivschat#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
