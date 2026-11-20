"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connectscheduling.errors import ServiceError

if TYPE_CHECKING:
    import capo_connectscheduling.types.message


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_connectscheduling.types.message.Message"
    quota_code: NotRequired["str"]
    """<p>The code of the quota that would be exceeded, for use with the Service Quotas API.</p>"""
    service_code: NotRequired["str"]
    """<p>The code of the service that owns the quota.</p>"""
    resource_id: NotRequired["str"]
    """<p>The identifier or ARN of the resource whose quota would be exceeded.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource whose quota would be exceeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectscheduling#ServiceQuotaExceededException``."""

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
