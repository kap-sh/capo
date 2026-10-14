"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#UnsupportedMediaTypeException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.string


class UnsupportedMediaTypeException_(TypedDict, closed=True):
    message: NotRequired["capo_lex_runtime_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedMediaTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedMediaTypeException_:
    out: UnsupportedMediaTypeException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnsupportedMediaTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#UnsupportedMediaTypeException``."""

    code: str | None = "UnsupportedMediaTypeException"

    def __init__(
        self,
        data: UnsupportedMediaTypeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedMediaTypeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedMediaTypeException":
        return cls(deserialize_json(data), message, response=response)
