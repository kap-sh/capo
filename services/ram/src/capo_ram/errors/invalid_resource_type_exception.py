"""Generated from Smithy shape ``com.amazonaws.ram#InvalidResourceTypeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class InvalidResourceTypeException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidResourceTypeException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidResourceTypeException_:
    out: InvalidResourceTypeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InvalidResourceTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#InvalidResourceTypeException``."""

    code: str | None = "InvalidResourceTypeException"

    def __init__(
        self,
        data: InvalidResourceTypeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceTypeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceTypeException":
        return cls(deserialize_json(data), message, response=response)
