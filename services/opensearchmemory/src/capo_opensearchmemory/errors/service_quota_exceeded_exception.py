"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ServiceQuotaExceededException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_opensearchmemory.errors import ServiceError


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    """<p>A message that describes which quota the request would exceed.</p>"""
    quota_code: NotRequired["str"]
    """<p>The Service Quotas code of the quota that the request would exceed. Not currently returned.</p>"""
    service_code: NotRequired["str"]
    """<p>The Service Quotas code of the service. Not currently returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearchmemory#ServiceQuotaExceededException``."""

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
