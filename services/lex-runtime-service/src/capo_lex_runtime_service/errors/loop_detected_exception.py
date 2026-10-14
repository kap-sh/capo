"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#LoopDetectedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.error_message


class LoopDetectedException_(TypedDict, closed=True):
    message: NotRequired["capo_lex_runtime_service.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: LoopDetectedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LoopDetectedException_:
    out: LoopDetectedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class LoopDetectedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#LoopDetectedException``."""

    code: str | None = "LoopDetectedException"

    def __init__(
        self,
        data: LoopDetectedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="LoopDetectedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LoopDetectedException":
        return cls(deserialize_json(data), message, response=response)
