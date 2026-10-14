"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#InternalServerException``."""

import zapros
from typing_extensions import TypedDict

from capo_partnercentral_revenue_measurement.errors import (
    DeserializationError,
    ServiceError,
)


class InternalServerException_(TypedDict, closed=True):
    message: "str"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_cbor(data), message, response=response)
