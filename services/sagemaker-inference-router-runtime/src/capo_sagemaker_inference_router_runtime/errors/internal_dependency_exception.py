"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InternalDependencyException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_inference_router_runtime.errors import ServiceError


class InternalDependencyException_(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalDependencyException_:
    out: InternalDependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#InternalDependencyException``."""

    code: str | None = "InternalDependencyException"

    def __init__(
        self,
        data: InternalDependencyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalDependencyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalDependencyException":
        return cls(deserialize_json(data), message, response=response)
