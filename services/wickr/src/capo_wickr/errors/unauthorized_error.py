"""Generated from Smithy shape ``com.amazonaws.wickr#UnauthorizedError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import ServiceError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class UnauthorizedError_(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message explaining why the authentication failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedError_:
    out: UnauthorizedError_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnauthorizedError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#UnauthorizedError``."""

    code: str | None = "UnauthorizedError"

    def __init__(
        self,
        data: UnauthorizedError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedError":
        return cls(deserialize_json(data), message, response=response)
