"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputServiceQuotaExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, ServiceError


class RouterOutputServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterOutputServiceQuotaExceededException_:
    out: RouterOutputServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "RouterOutputServiceQuotaExceededException_.message required"
        )
    return out


class RouterOutputServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#RouterOutputServiceQuotaExceededException``."""

    code: str | None = "RouterOutputServiceQuotaExceededException"

    def __init__(
        self,
        data: RouterOutputServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RouterOutputServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RouterOutputServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
