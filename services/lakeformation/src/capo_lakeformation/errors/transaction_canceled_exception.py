"""Generated from Smithy shape ``com.amazonaws.lakeformation#TransactionCanceledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class TransactionCanceledException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionCanceledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TransactionCanceledException_:
    out: TransactionCanceledException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TransactionCanceledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#TransactionCanceledException``."""

    code: str | None = "TransactionCanceledException"

    def __init__(
        self,
        data: TransactionCanceledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionCanceledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TransactionCanceledException":
        return cls(deserialize_json(data), message, response=response)
