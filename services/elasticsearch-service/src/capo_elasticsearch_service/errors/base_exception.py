"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#BaseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.error_message


class BaseException_(TypedDict, closed=True):
    message: NotRequired["capo_elasticsearch_service.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BaseException_:
    out: BaseException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class BaseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticsearchservice#BaseException``."""

    code: str | None = "BaseException"

    def __init__(
        self,
        data: BaseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BaseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BaseException":
        return cls(deserialize_json(data), message, response=response)
