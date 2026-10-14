"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GatewayTimeoutException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_amplifybackend.errors import ServiceError

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class GatewayTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>An error message to inform that the request failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GatewayTimeoutException_:
    out: GatewayTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class GatewayTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.amplifybackend#GatewayTimeoutException``."""

    code: str | None = "GatewayTimeoutException"

    def __init__(
        self,
        data: GatewayTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="GatewayTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "GatewayTimeoutException":
        return cls(deserialize_json(data), message, response=response)
