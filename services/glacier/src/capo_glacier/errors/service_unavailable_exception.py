"""Generated from Smithy shape ``com.amazonaws.glacier#ServiceUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glacier.errors import ServiceError

if TYPE_CHECKING:
    import capo_glacier.types.string


class ServiceUnavailableException_(TypedDict, closed=True):
    type: NotRequired["capo_glacier.types.string.string"]
    """<p>Server</p>"""
    code: NotRequired["capo_glacier.types.string.string"]
    """<p>500 Internal Server Error</p>"""
    message: NotRequired["capo_glacier.types.string.string"]
    """<p>Returned if the service cannot complete the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(
        self,
        data: ServiceUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceUnavailableException":
        return cls(deserialize_json(data), message, response=response)
