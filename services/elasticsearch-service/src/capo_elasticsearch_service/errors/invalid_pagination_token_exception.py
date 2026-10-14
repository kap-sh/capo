"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InvalidPaginationTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.error_message


class InvalidPaginationTokenException_(TypedDict, closed=True):
    message: NotRequired["capo_elasticsearch_service.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidPaginationTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidPaginationTokenException_:
    out: InvalidPaginationTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidPaginationTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticsearchservice#InvalidPaginationTokenException``."""

    code: str | None = "InvalidPaginationTokenException"

    def __init__(
        self,
        data: InvalidPaginationTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPaginationTokenException":
        return cls(deserialize_json(data), message, response=response)
