"""Generated from Smithy shape ``com.amazonaws.iot#TransferAlreadyCompletedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot.types.error_message2


class TransferAlreadyCompletedException_(TypedDict, closed=True):
    message: NotRequired["capo_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransferAlreadyCompletedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransferAlreadyCompletedException_:
    out: TransferAlreadyCompletedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TransferAlreadyCompletedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#TransferAlreadyCompletedException``."""

    code: str | None = "TransferAlreadyCompletedException"

    def __init__(
        self,
        data: TransferAlreadyCompletedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransferAlreadyCompletedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TransferAlreadyCompletedException":
        return cls(deserialize_json(data), message, response=response)
