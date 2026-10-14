"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ConnectorTimeoutException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import ServiceError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.error_message


class ConnectorTimeoutException_(TypedDict, closed=True):
    message: NotRequired["capo_iottwinmaker.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorTimeoutException_:
    out: ConnectorTimeoutException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConnectorTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iottwinmaker#ConnectorTimeoutException``."""

    code: str | None = "ConnectorTimeoutException"

    def __init__(
        self,
        data: ConnectorTimeoutException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectorTimeoutException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConnectorTimeoutException":
        return cls(deserialize_json(data), message, response=response)
