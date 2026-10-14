"""Generated from Smithy shape ``com.amazonaws.connect#InvalidActiveRegionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message


class InvalidActiveRegionException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidActiveRegionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidActiveRegionException_:
    out: InvalidActiveRegionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidActiveRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidActiveRegionException``."""

    code: str | None = "InvalidActiveRegionException"

    def __init__(
        self,
        data: InvalidActiveRegionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidActiveRegionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidActiveRegionException":
        return cls(deserialize_json(data), message, response=response)
