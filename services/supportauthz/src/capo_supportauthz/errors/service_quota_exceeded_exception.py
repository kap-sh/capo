"""Generated from Smithy shape ``com.amazonaws.supportauthz#ServiceQuotaExceededException``."""

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    resource_id: "str"
    """<p>The identifier of the resource that exceeded the quota.</p>"""
    resource_type: "str"
    """<p>The type of the resource that exceeded the quota.</p>"""
    service_code: "str"
    """<p>The service code of the originating service.</p>"""
    quota_code: "str"
    """<p>The quota code of the exceeded quota.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.supportauthz#ServiceQuotaExceededException``."""

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
