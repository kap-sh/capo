"""Generated from Smithy shape ``com.amazonaws.iotdataplane#MethodNotAllowedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_data_plane.types.error_message


class MethodNotAllowedException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_data_plane.types.error_message.errorMessage"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MethodNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MethodNotAllowedException_:
    out: MethodNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MethodNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotdataplane#MethodNotAllowedException``."""

    code: str | None = "MethodNotAllowedException"

    def __init__(
        self,
        data: MethodNotAllowedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MethodNotAllowedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MethodNotAllowedException":
        return cls(deserialize_json(data), message, response=response)
