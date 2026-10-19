"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputServiceQuotaExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_mediaconnect.errors import ServiceError


class RouterInputServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterInputServiceQuotaExceededException_:
    out: RouterInputServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class RouterInputServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#RouterInputServiceQuotaExceededException``."""

    code: str | None = "RouterInputServiceQuotaExceededException"

    def __init__(
        self,
        data: RouterInputServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RouterInputServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RouterInputServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
