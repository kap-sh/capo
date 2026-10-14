"""Generated from Smithy shape ``com.amazonaws.networkmonitor#InternalServerException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_networkmonitor.errors import ServiceError


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmonitor#InternalServerException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message, response=response)
