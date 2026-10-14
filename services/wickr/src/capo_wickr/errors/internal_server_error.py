"""Generated from Smithy shape ``com.amazonaws.wickr#InternalServerError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class InternalServerError_(TypedDict, closed=True):
    message: "capo_wickr.types.generic_string.GenericString"
    """<p>A message describing the internal server error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerError_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerError_.message required")
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(
        self,
        data: InternalServerError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerError":
        return cls(deserialize_json(data), message, response=response)
