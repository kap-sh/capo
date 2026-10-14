"""Generated from Smithy shape ``com.amazonaws.appintegrations#DuplicateResourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appintegrations.errors import ServiceError

if TYPE_CHECKING:
    import capo_appintegrations.types.message


class DuplicateResourceException_(TypedDict, closed=True):
    message: NotRequired["capo_appintegrations.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: DuplicateResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DuplicateResourceException_:
    out: DuplicateResourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DuplicateResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appintegrations#DuplicateResourceException``."""

    code: str | None = "DuplicateResourceException"

    def __init__(
        self,
        data: DuplicateResourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateResourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateResourceException":
        return cls(deserialize_json(data), message, response=response)
