"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ThrottlingException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import (
    DeserializationError,
    ServiceError,
)


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    service_code: NotRequired["str"]
    """<p>The service code associated with the throttling error.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code associated with the throttling error.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    return out


def deserialize_cbor(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_cbor(data), message, response=response)
