"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ServiceQuotaExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_workspaces_instances.errors import ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    """<p>Description of the quota limitation.</p>"""
    resource_id: "str"
    """<p>Identifier of the resource related to the quota.</p>"""
    resource_type: "str"
    """<p>Type of resource related to the quota.</p>"""
    service_code: "str"
    """<p>Code identifying the service with the quota limitation.</p>"""
    quota_code: "str"
    """<p>Specific code for the exceeded quota.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    out["ServiceCode"] = value["service_code"]
    out["QuotaCode"] = value["quota_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    else:
        out["quota_code"] = ""
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#ServiceQuotaExceededException``."""

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
