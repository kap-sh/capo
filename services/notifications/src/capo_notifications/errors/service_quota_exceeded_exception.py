"""Generated from Smithy shape ``com.amazonaws.notifications#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_notifications.types.error_message
    import capo_notifications.types.quota_code
    import capo_notifications.types.resource_id
    import capo_notifications.types.resource_type
    import capo_notifications.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_notifications.types.error_message.ErrorMessage"
    resource_type: "capo_notifications.types.resource_type.ResourceType"
    """<p>The type of the resource that exceeds the service quota.</p>"""
    resource_id: NotRequired["capo_notifications.types.resource_id.ResourceId"]
    """<p>The ID of the resource that exceeds the service quota.</p>"""
    service_code: NotRequired["capo_notifications.types.service_code.ServiceCode"]
    """<p>The code for the service quota exceeded in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""
    quota_code: NotRequired["capo_notifications.types.quota_code.QuotaCode"]
    """<p>The code for the service quota in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notifications#ServiceQuotaExceededException``."""

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
