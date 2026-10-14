"""Generated from Smithy shape ``com.amazonaws.ram#ServerInternalException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class ServerInternalException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ServerInternalException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServerInternalException_:
    out: ServerInternalException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServerInternalException_.message required")
    return out


class ServerInternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ServerInternalException``."""

    code: str | None = "ServerInternalException"

    def __init__(
        self,
        data: ServerInternalException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerInternalException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServerInternalException":
        return cls(deserialize_json(data), message, response=response)
