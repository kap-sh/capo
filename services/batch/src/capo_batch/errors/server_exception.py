"""Generated from Smithy shape ``com.amazonaws.batch#ServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_batch.errors import ServiceError

if TYPE_CHECKING:
    import capo_batch.types.string


class ServerException_(TypedDict, closed=True):
    message: NotRequired["capo_batch.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServerException_:
    out: ServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.batch#ServerException``."""

    code: str | None = "ServerException"

    def __init__(
        self,
        data: ServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServerException":
        return cls(deserialize_json(data), message, response=response)
