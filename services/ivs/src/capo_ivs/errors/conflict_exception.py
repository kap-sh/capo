"""Generated from Smithy shape ``com.amazonaws.ivs#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ivs.types.error_message
    import capo_ivs.types.string


class ConflictException_(TypedDict, closed=True):
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
    """<p>Updating or deleting a resource can cause an inconsistent state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "exception_message" in value:
        out["exceptionMessage"] = value["exception_message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("exceptionMessage") is not None:
        out["exception_message"] = data["exceptionMessage"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ivs#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
