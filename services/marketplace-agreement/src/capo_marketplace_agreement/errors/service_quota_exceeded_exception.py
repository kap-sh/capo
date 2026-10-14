"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.exception_message
    import capo_marketplace_agreement.types.request_id
    import capo_marketplace_agreement.types.resource_id


class ServiceQuotaExceededException_(TypedDict, closed=True):
    request_id: NotRequired["capo_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "capo_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""
    quota_code: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The code of the quota that was exceeded.</p>"""
    service_code: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The code of the service whose quota was exceeded.</p>"""
    resource_type: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The type of the resource that exceeded the quota.</p>"""
    resource_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the resource that exceeded the quota.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#ServiceQuotaExceededException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
