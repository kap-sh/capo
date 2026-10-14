"""Generated from Smithy shape ``com.amazonaws.polly#SynthesisTaskNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_polly.errors import ServiceError

if TYPE_CHECKING:
    import capo_polly.types.error_message


class SynthesisTaskNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SynthesisTaskNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SynthesisTaskNotFoundException_:
    out: SynthesisTaskNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class SynthesisTaskNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#SynthesisTaskNotFoundException``."""

    code: str | None = "SynthesisTaskNotFoundException"

    def __init__(
        self,
        data: SynthesisTaskNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SynthesisTaskNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SynthesisTaskNotFoundException":
        return cls(deserialize_json(data), message, response=response)
