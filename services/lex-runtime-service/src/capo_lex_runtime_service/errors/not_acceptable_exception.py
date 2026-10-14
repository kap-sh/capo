"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#NotAcceptableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.string


class NotAcceptableException_(TypedDict, closed=True):
    message: NotRequired["capo_lex_runtime_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: NotAcceptableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotAcceptableException_:
    out: NotAcceptableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class NotAcceptableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#NotAcceptableException``."""

    code: str | None = "NotAcceptableException"

    def __init__(
        self,
        data: NotAcceptableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotAcceptableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotAcceptableException":
        return cls(deserialize_json(data), message, response=response)
