"""Generated from Smithy shape ``com.amazonaws.ram#TagLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class TagLimitExceededException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: TagLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagLimitExceededException_:
    out: TagLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TagLimitExceededException_.message required")
    return out


class TagLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#TagLimitExceededException``."""

    code: str | None = "TagLimitExceededException"

    def __init__(
        self,
        data: TagLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TagLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
