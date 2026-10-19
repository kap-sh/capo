"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_partnercentral_revenue_measurement.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason"
    """<p>The reason the service quota was exceeded.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason

    out["Reason"] = (
        capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason.serialize_cbor(
            value["reason"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason

        out["reason"] = (
            capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason",
            "",
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ServiceQuotaExceededException``."""

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
