"""Generated from Smithy shape ``com.amazonaws.wickr#BadRequestError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import ServiceError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class BadRequestError_(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A detailed message explaining what was wrong with the request and how to correct it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestError_:
    out: BadRequestError_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class BadRequestError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#BadRequestError``."""

    code: str | None = "BadRequestError"

    def __init__(
        self,
        data: BadRequestError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BadRequestError":
        return cls(deserialize_json(data), message, response=response)
