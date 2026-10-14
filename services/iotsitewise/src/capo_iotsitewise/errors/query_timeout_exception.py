"""Generated from Smithy shape ``com.amazonaws.iotsitewise#QueryTimeoutException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import ServiceError

if TYPE_CHECKING:
    import capo_iotsitewise.types.error_message


class QueryTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_iotsitewise.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> QueryTimeoutException_:
    out: QueryTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class QueryTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotsitewise#QueryTimeoutException``."""

    code: str | None = "QueryTimeoutException"

    def __init__(
        self,
        data: QueryTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="QueryTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "QueryTimeoutException":
        return cls(deserialize_json(data), message, response=response)
