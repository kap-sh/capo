"""Generated from Smithy shape ``com.amazonaws.mgn#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import ServiceError

if TYPE_CHECKING:
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.strictly_positive_integer


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    resource_id: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Exceeded the service quota resource ID.</p>"""
    resource_type: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Exceeded the service quota resource type.</p>"""
    service_code: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Exceeded the service quota service code.</p>"""
    quota_code: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Exceeded the service quota code.</p>"""
    quota_value: NotRequired[
        "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Exceeded the service quota value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "quota_value" in value:
        out["quotaValue"] = value["quota_value"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    if data.get("quotaValue") is not None:
        out["quota_value"] = data["quotaValue"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self,
        data: ServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
