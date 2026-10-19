"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ConflictException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import ServiceError


class ConflictException_(TypedDict, closed=True):
    message: "str"
    """A human-readable description of the conflict."""
    conflict_type: NotRequired["str"]
    """The type of conflict that caused the request to fail. Not always present."""
    resource_id: NotRequired["str"]
    """The identifier of the resource that is in conflict. Not always present."""
    resource_type: NotRequired["str"]
    """The type of the resource that is in conflict. Not always present."""
    error_code: NotRequired["str"]
    """The error code associated with the conflict. Not always present."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "conflict_type" in value:
        out["conflictType"] = value["conflict_type"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_cbor(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("conflictType") is not None:
        out["conflict_type"] = data["conflictType"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudwatchomni#ConflictException``."""

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
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_cbor(data), message, response=response)
