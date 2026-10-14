"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.error_message
    import capo_ivs_realtime.types.string


class InternalServerException_(TypedDict, closed=True):
    access_control_allow_origin: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    access_control_expose_headers: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    cache_control: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    content_security_policy: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    strict_transport_security: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    x_content_type_options: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    x_frame_options: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    x_amzn_error_type: NotRequired["capo_ivs_realtime.types.string.String"]
    """<p/>"""
    exception_message: NotRequired["capo_ivs_realtime.types.error_message.errorMessage"]
    """<p>Unexpected error during processing of request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "exception_message" in value:
        out["exceptionMessage"] = value["exception_message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("exceptionMessage") is not None:
        out["exception_message"] = data["exceptionMessage"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivsrealtime#InternalServerException``."""

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
            is_retryable=False,
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
