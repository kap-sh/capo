"""Generated from Smithy shape ``com.amazonaws.wickr#ForbiddenError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import ServiceError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class ForbiddenError_(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message explaining why access was denied and what permissions are required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ForbiddenError_:
    out: ForbiddenError_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ForbiddenError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#ForbiddenError``."""

    code: str | None = "ForbiddenError"

    def __init__(
        self,
        data: ForbiddenError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ForbiddenError":
        return cls(deserialize_json(data), message, response=response)
