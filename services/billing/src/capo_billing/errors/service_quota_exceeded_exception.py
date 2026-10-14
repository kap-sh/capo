"""Generated from Smithy shape ``com.amazonaws.billing#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_billing.types.error_message
    import capo_billing.types.quota_code
    import capo_billing.types.resource_id
    import capo_billing.types.resource_type
    import capo_billing.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_billing.types.error_message.ErrorMessage"
    resource_id: "capo_billing.types.resource_id.ResourceId"
    """<p> The ID of the resource. </p>"""
    resource_type: "capo_billing.types.resource_type.ResourceType"
    """<p> The type of Amazon Web Services resource. </p>"""
    service_code: "capo_billing.types.service_code.ServiceCode"
    """<p> The container for the <code>serviceCode</code>. </p>"""
    quota_code: "capo_billing.types.quota_code.QuotaCode"
    """<p> The container for the <code>quotaCode</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    out["serviceCode"] = value["service_code"]
    out["quotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
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
    """Modeled error for Smithy shape ``com.amazonaws.billing#ServiceQuotaExceededException``."""

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
