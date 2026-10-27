"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointServiceQuotaExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_mediaconnect.errors import ServiceError


class SourceEndpointServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SourceEndpointServiceQuotaExceededException_:
    out: SourceEndpointServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class SourceEndpointServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointServiceQuotaExceededException``."""

    code: str | None = "SourceEndpointServiceQuotaExceededException"

    def __init__(
        self,
        data: SourceEndpointServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SourceEndpointServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SourceEndpointServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
