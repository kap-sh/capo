"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PendingVerification``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.error_message
    import capo_ivs_realtime.types.string


class PendingVerification_(TypedDict, closed=True):
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
    """<p> Your account is pending verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingVerification_) -> dict:
    out: dict = {}
    if "exception_message" in value:
        out["exceptionMessage"] = value["exception_message"]
    return out


def deserialize_json(data: dict) -> PendingVerification_:
    out: PendingVerification_ = {}  # type: ignore[typeddict-item]
    if data.get("exceptionMessage") is not None:
        out["exception_message"] = data["exceptionMessage"]
    return out


class PendingVerification(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivsrealtime#PendingVerification``."""

    code: str | None = "PendingVerification"

    def __init__(
        self,
        data: PendingVerification_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PendingVerification",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PendingVerification":
        return cls(deserialize_json(data), message, response=response)
