"""Generated from Smithy shape ``com.amazonaws.lambda#RuntimeAliasDeletedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class RuntimeAliasDeletedException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>Indicates the exception type for a deleted runtime alias.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeAliasDeletedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RuntimeAliasDeletedException_:
    out: RuntimeAliasDeletedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class RuntimeAliasDeletedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#RuntimeAliasDeletedException``."""

    code: str | None = "RuntimeAliasDeletedException"

    def __init__(
        self,
        data: RuntimeAliasDeletedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RuntimeAliasDeletedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RuntimeAliasDeletedException":
        return cls(deserialize_json(data), message, response=response)
