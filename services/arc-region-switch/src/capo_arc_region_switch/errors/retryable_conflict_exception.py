"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RetryableConflictException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import ServiceError


class RetryableConflictException_(TypedDict, closed=True):
    message: "str"
    resource_id: NotRequired["str"]
    """<p>The identifier of the resource involved in the concurrent modification.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource involved in the concurrent modification.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetryableConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RetryableConflictException_:
    out: RetryableConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out


class RetryableConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arcregionswitch#RetryableConflictException``."""

    code: str | None = "RetryableConflictException"

    def __init__(
        self,
        data: RetryableConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RetryableConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RetryableConflictException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
