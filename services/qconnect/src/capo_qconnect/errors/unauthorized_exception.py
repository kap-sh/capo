"""Generated from Smithy shape ``com.amazonaws.qconnect#UnauthorizedException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import ServiceError


class UnauthorizedException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qconnect#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(
        self,
        data: UnauthorizedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedException":
        return cls(deserialize_json(data), message, response=response)
