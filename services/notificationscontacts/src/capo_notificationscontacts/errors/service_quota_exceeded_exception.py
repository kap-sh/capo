"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notificationscontacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.error_message
    import capo_notificationscontacts.types.quota_code
    import capo_notificationscontacts.types.resource_id
    import capo_notificationscontacts.types.resource_type
    import capo_notificationscontacts.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_notificationscontacts.types.error_message.ErrorMessage"
    resource_id: "capo_notificationscontacts.types.resource_id.ResourceId"
    """<p>The ID of the resource that exceeds the service quota.</p>"""
    resource_type: "capo_notificationscontacts.types.resource_type.ResourceType"
    """<p>The type of the resource that exceeds the service quota.</p>"""
    service_code: "capo_notificationscontacts.types.service_code.ServiceCode"
    """<p>The code for the service quota exceeded in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""
    quota_code: "capo_notificationscontacts.types.quota_code.QuotaCode"
    """<p>The code for the service quota in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    out["serviceCode"] = value["service_code"]
    out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_id required"
        )
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notificationscontacts#ServiceQuotaExceededException``."""

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
