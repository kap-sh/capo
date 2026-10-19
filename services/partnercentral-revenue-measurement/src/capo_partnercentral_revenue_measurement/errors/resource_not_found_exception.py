"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_partnercentral_revenue_measurement.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason


class ResourceNotFoundException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason.ResourceNotFoundExceptionReason"
    """<p>The reason the resource was not found.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason

    out["Reason"] = (
        capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason.serialize_cbor(
            value["reason"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason

        out["reason"] = (
            capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.resource_not_found_exception_reason.ResourceNotFoundExceptionReason",
            "",
        )
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(
        self,
        data: ResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotFoundException":
        return cls(deserialize_cbor(data), message, response=response)
