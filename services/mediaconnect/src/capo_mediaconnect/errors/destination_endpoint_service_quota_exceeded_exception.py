"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointServiceQuotaExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_mediaconnect.errors import ServiceError


class DestinationEndpointServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DestinationEndpointServiceQuotaExceededException_:
    out: DestinationEndpointServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class DestinationEndpointServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointServiceQuotaExceededException``."""

    code: str | None = "DestinationEndpointServiceQuotaExceededException"

    def __init__(
        self,
        data: DestinationEndpointServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DestinationEndpointServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DestinationEndpointServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
