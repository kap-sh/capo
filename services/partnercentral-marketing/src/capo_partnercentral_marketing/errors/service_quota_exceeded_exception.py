"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.error_message


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    resource_type: NotRequired["str"]
    """The affected resource type."""
    quota_code: NotRequired["str"]
    """The exceeded quota code."""
    service_code: NotRequired["str"]
    """The service code."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    return out


def deserialize_cbor(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#ServiceQuotaExceededException``."""

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
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_cbor(data), message, response=response)
