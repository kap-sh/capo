"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.error_message


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_elasticsearch_service.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticsearchservice#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
