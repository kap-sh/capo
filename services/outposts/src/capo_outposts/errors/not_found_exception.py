"""Generated from Smithy shape ``com.amazonaws.outposts#NotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_outposts.errors import ServiceError

if TYPE_CHECKING:
    import capo_outposts.types.error_message


class NotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_outposts.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.outposts#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(
        self,
        data: NotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotFoundException":
        return cls(deserialize_json(data), message, response=response)
