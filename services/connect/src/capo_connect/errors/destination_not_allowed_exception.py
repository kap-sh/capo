"""Generated from Smithy shape ``com.amazonaws.connect#DestinationNotAllowedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message


class DestinationNotAllowedException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]
    """<p>The message about the outbound calls.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DestinationNotAllowedException_:
    out: DestinationNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DestinationNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#DestinationNotAllowedException``."""

    code: str | None = "DestinationNotAllowedException"

    def __init__(
        self,
        data: DestinationNotAllowedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DestinationNotAllowedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DestinationNotAllowedException":
        return cls(deserialize_json(data), message, response=response)
