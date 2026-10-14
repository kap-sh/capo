"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateBridge420Exception``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import ServiceError


class CreateBridge420Exception_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateBridge420Exception_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateBridge420Exception_:
    out: CreateBridge420Exception_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CreateBridge420Exception(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#CreateBridge420Exception``."""

    code: str | None = "CreateBridge420Exception"

    def __init__(
        self,
        data: CreateBridge420Exception_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CreateBridge420Exception",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CreateBridge420Exception":
        return cls(deserialize_json(data), message, response=response)
