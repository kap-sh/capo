"""Generated from Smithy shape ``com.amazonaws.connect#ContactNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message


class ContactNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]
    """<p>The message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ContactNotFoundException_:
    out: ContactNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ContactNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#ContactNotFoundException``."""

    code: str | None = "ContactNotFoundException"

    def __init__(
        self,
        data: ContactNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContactNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ContactNotFoundException":
        return cls(deserialize_json(data), message, response=response)
