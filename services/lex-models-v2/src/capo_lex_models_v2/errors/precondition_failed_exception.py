"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PreconditionFailedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.exception_message


class PreconditionFailedException_(TypedDict, closed=True):
    message: NotRequired["capo_lex_models_v2.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: PreconditionFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PreconditionFailedException_:
    out: PreconditionFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class PreconditionFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexmodelsv2#PreconditionFailedException``."""

    code: str | None = "PreconditionFailedException"

    def __init__(
        self,
        data: PreconditionFailedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionFailedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PreconditionFailedException":
        return cls(deserialize_json(data), message, response=response)
