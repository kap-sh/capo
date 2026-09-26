"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ServiceQuotaExceededException``."""

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError, ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    quota_code: NotRequired["str"]
    """<p>The code that identifies the service quota that was exceeded.</p>"""
    service_code: NotRequired["str"]
    """<p>The code for the AWS service that owns the quota that was exceeded.</p>"""
    resource_id: NotRequired["str"]
    """<p>The ID of the resource associated with the quota that was exceeded.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource associated with the quota that was exceeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networksecuritymanager#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self, data: ServiceQuotaExceededException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data), message)
