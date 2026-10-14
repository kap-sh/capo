"""Generated from Smithy shape ``com.amazonaws.ivs#ChannelNotBroadcasting``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ivs.types.error_message
    import capo_ivs.types.string


class ChannelNotBroadcasting_(TypedDict, closed=True):
    access_control_allow_origin: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    access_control_expose_headers: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    cache_control: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    content_security_policy: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    strict_transport_security: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    x_content_type_options: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    x_frame_options: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    x_amzn_error_type: NotRequired["capo_ivs.types.string.String"]
    """<p/>"""
    exception_message: NotRequired["capo_ivs.types.error_message.errorMessage"]
    """<p>The stream is offline for the given channel ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelNotBroadcasting_) -> dict:
    out: dict = {}
    if "exception_message" in value:
        out["exceptionMessage"] = value["exception_message"]
    return out


def deserialize_json(data: dict) -> ChannelNotBroadcasting_:
    out: ChannelNotBroadcasting_ = {}  # type: ignore[typeddict-item]
    if data.get("exceptionMessage") is not None:
        out["exception_message"] = data["exceptionMessage"]
    return out


class ChannelNotBroadcasting(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivs#ChannelNotBroadcasting``."""

    code: str | None = "ChannelNotBroadcasting"

    def __init__(
        self,
        data: ChannelNotBroadcasting_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ChannelNotBroadcasting",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ChannelNotBroadcasting":
        return cls(deserialize_json(data), message, response=response)
