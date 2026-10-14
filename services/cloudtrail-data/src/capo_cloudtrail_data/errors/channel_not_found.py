"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ChannelNotFound``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail_data.errors import ServiceError


class ChannelNotFound_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ChannelNotFound_:
    out: ChannelNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ChannelNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtraildata#ChannelNotFound``."""

    code: str | None = "ChannelNotFound"

    def __init__(
        self,
        data: ChannelNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ChannelNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ChannelNotFound":
        return cls(deserialize_json(data), message, response=response)
