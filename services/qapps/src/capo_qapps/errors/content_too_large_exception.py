"""Generated from Smithy shape ``com.amazonaws.qapps#ContentTooLargeException``."""

import zapros
from typing_extensions import TypedDict

from capo_qapps.errors import DeserializationError, ServiceError


class ContentTooLargeException_(TypedDict, closed=True):
    message: "str"
    resource_id: "str"
    """<p>The unique identifier of the resource</p>"""
    resource_type: "str"
    """<p>The type of the resource</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentTooLargeException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ContentTooLargeException_:
    out: ContentTooLargeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ContentTooLargeException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ContentTooLargeException_.resource_id required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ContentTooLargeException_.resource_type required")
    return out


class ContentTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qapps#ContentTooLargeException``."""

    code: str | None = "ContentTooLargeException"

    def __init__(
        self,
        data: ContentTooLargeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContentTooLargeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ContentTooLargeException":
        return cls(deserialize_json(data), message, response=response)
