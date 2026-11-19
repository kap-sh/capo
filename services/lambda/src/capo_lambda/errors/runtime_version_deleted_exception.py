"""Generated from Smithy shape ``com.amazonaws.lambda#RuntimeVersionDeletedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string


class RuntimeVersionDeletedException_(TypedDict, closed=True):
    type: NotRequired["capo_lambda.types.string.String"]
    """<p>Indicates the exception type for a deleted runtime version.</p>"""
    message: NotRequired["capo_lambda.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionDeletedException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RuntimeVersionDeletedException_:
    out: RuntimeVersionDeletedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class RuntimeVersionDeletedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#RuntimeVersionDeletedException``."""

    code: str | None = "RuntimeVersionDeletedException"

    def __init__(
        self,
        data: RuntimeVersionDeletedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RuntimeVersionDeletedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RuntimeVersionDeletedException":
        return cls(deserialize_json(data), message, response=response)
