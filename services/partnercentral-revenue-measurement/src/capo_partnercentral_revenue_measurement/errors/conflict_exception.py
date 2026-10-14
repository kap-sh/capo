"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_partnercentral_revenue_measurement.errors import (
    DeserializationError,
    ServiceError,
)

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.conflict_exception_reason


class ConflictException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_revenue_measurement.types.conflict_exception_reason.ConflictExceptionReason"
    """<p>The reason for the conflict.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_revenue_measurement.types.conflict_exception_reason

    out["Reason"] = (
        capo_partnercentral_revenue_measurement.types.conflict_exception_reason.serialize_cbor(
            value["reason"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if data.get("Reason") is not None:
        import capo_partnercentral_revenue_measurement.types.conflict_exception_reason

        out["reason"] = (
            capo_partnercentral_revenue_measurement.types.conflict_exception_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError("ConflictException_.reason required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_cbor(data), message, response=response)
