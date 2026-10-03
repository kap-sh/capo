"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_greengrassv2.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_greengrassv2.types.string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_greengrassv2.types.string.String"
    resource_id: NotRequired["capo_greengrassv2.types.string.String"]
    """<p>The ID of the resource that exceeds the service quota.</p>"""
    resource_type: NotRequired["capo_greengrassv2.types.string.String"]
    """<p>The type of the resource that exceeds the service quota.</p>"""
    quota_code: "capo_greengrassv2.types.string.String"
    """<p>The code for the quota in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""
    service_code: "capo_greengrassv2.types.string.String"
    """<p>The code for the service in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    out["quotaCode"] = value["quota_code"]
    out["serviceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrassv2#ServiceQuotaExceededException``."""

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
