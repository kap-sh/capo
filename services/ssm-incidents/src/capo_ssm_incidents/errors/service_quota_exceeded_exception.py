"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.exception_message
    import capo_ssm_incidents.types.resource_type
    import capo_ssm_incidents.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_ssm_incidents.types.exception_message.ExceptionMessage"
    resource_identifier: NotRequired["str"]
    """The identifier for the requested resource"""
    resource_type: NotRequired["capo_ssm_incidents.types.resource_type.ResourceType"]
    """The resource type"""
    service_code: "capo_ssm_incidents.types.service_code.ServiceCode"
    """Originating service code"""
    quota_code: "str"
    """Originating quota code"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
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
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
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
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ServiceQuotaExceededException``."""

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
