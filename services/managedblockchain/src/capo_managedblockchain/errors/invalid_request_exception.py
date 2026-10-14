"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InvalidRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain.errors import ServiceError

if TYPE_CHECKING:
    import capo_managedblockchain.types.string


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_managedblockchain.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchain#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(
        self,
        data: InvalidRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRequestException":
        return cls(deserialize_json(data), message, response=response)
