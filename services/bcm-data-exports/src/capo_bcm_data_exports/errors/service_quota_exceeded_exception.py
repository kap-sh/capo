"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bcm_data_exports.errors import ServiceError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.generic_string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_bcm_data_exports.types.generic_string.GenericString"
    resource_id: NotRequired["capo_bcm_data_exports.types.generic_string.GenericString"]
    """<p>The identifier of the resource that exceeded quota.</p>"""
    resource_type: NotRequired[
        "capo_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The type of the resource that exceeded quota.</p>"""
    quota_code: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The quota code that was exceeded.</p>"""
    service_code: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The service code that exceeded quota. It will always be “AWSBillingAndCostManagementDataExports”.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["QuotaCode"] = value["quota_code"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    else:
        out["quota_code"] = ""
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bcmdataexports#ServiceQuotaExceededException``."""

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
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
