"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#ModelNotReadyException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_inference_router_runtime.errors import ServiceError


class ModelNotReadyException_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ModelNotReadyException_:
    out: ModelNotReadyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ModelNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#ModelNotReadyException``."""

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
            is_throttling_error=True,
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
