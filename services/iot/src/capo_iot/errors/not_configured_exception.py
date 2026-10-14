"""Generated from Smithy shape ``com.amazonaws.iot#NotConfiguredException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot.types.error_message2


class NotConfiguredException_(TypedDict, closed=True):
    message: NotRequired["capo_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotConfiguredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotConfiguredException_:
    out: NotConfiguredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class NotConfiguredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#NotConfiguredException``."""

    code: str | None = "NotConfiguredException"

    def __init__(
        self,
        data: NotConfiguredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotConfiguredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotConfiguredException":
        return cls(deserialize_json(data), message, response=response)
