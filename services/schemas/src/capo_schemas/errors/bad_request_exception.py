"""Generated from Smithy shape ``com.amazonaws.schemas#BadRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_schemas.errors import ServiceError

if TYPE_CHECKING:
    import capo_schemas.types.__string


class BadRequestException_(TypedDict, closed=True):
    code: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The message string of the error output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.schemas#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(
        self,
        data: BadRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BadRequestException":
        return cls(deserialize_json(data), message, response=response)
