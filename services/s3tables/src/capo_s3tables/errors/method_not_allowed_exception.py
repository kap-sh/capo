"""Generated from Smithy shape ``com.amazonaws.s3tables#MethodNotAllowedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3tables.types.error_message


class MethodNotAllowedException_(TypedDict, closed=True):
    message: NotRequired["capo_s3tables.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MethodNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MethodNotAllowedException_:
    out: MethodNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MethodNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3tables#MethodNotAllowedException``."""

    code: str | None = "MethodNotAllowedException"

    def __init__(
        self,
        data: MethodNotAllowedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MethodNotAllowedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MethodNotAllowedException":
        return cls(deserialize_json(data), message, response=response)
