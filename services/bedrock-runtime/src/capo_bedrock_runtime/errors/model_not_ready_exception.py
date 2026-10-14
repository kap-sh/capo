"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelNotReadyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.non_blank_string


class ModelNotReadyException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock_runtime.types.non_blank_string.NonBlankString"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ModelNotReadyException_:
    out: ModelNotReadyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ModelNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelNotReadyException``."""

    code: str | None = "ModelNotReadyException"

    def __init__(
        self,
        data: ModelNotReadyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ModelNotReadyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ModelNotReadyException":
        return cls(deserialize_json(data), message, response=response)
