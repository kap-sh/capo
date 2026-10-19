"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_managedblockchain_query.errors import ServiceError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.exception_message
    import capo_managedblockchain_query.types.quota_code
    import capo_managedblockchain_query.types.resource_id
    import capo_managedblockchain_query.types.resource_type
    import capo_managedblockchain_query.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_managedblockchain_query.types.exception_message.ExceptionMessage"
    """<p>The container for the exception message.</p>"""
    resource_id: "capo_managedblockchain_query.types.resource_id.ResourceId"
    """<p>The <code>resourceId</code> of the resource that caused the exception.</p>"""
    resource_type: "capo_managedblockchain_query.types.resource_type.ResourceType"
    """<p>The <code>resourceType</code> of the resource that caused the exception.</p>"""
    service_code: "capo_managedblockchain_query.types.service_code.ServiceCode"
    """<p>The container for the <code>serviceCode</code>.</p>"""
    quota_code: "capo_managedblockchain_query.types.quota_code.QuotaCode"
    """<p>The container for the <code>quotaCode</code>.</p>"""


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
        out["message"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        out["service_code"] = ""
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    else:
        out["quota_code"] = ""
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchainquery#ServiceQuotaExceededException``."""

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
