"""Generated from Smithy shape ``com.amazonaws.panorama#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_panorama.types.string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_panorama.types.string.String"
    resource_id: NotRequired["capo_panorama.types.string.String"]
    """<p>The target resource's ID.</p>"""
    resource_type: NotRequired["capo_panorama.types.string.String"]
    """<p>The target resource's type.</p>"""
    quota_code: "capo_panorama.types.string.String"
    """<p>The name of the limit.</p>"""
    service_code: "capo_panorama.types.string.String"
    """<p>The name of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["QuotaCode"] = value["quota_code"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.panorama#ServiceQuotaExceededException``."""

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
