"""Generated from Smithy shape ``com.amazonaws.ram#MissingRequiredParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class MissingRequiredParameterException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: MissingRequiredParameterException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MissingRequiredParameterException_:
    out: MissingRequiredParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class MissingRequiredParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#MissingRequiredParameterException``."""

    code: str | None = "MissingRequiredParameterException"

    def __init__(
        self,
        data: MissingRequiredParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingRequiredParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MissingRequiredParameterException":
        return cls(deserialize_json(data), message, response=response)
