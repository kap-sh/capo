"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorAuthenticationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import ServiceError

if TYPE_CHECKING:
    import capo_appflow.types.error_message


class ConnectorAuthenticationException_(TypedDict, closed=True):
    message: NotRequired["capo_appflow.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorAuthenticationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorAuthenticationException_:
    out: ConnectorAuthenticationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConnectorAuthenticationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appflow#ConnectorAuthenticationException``."""

    code: str | None = "ConnectorAuthenticationException"

    def __init__(
        self,
        data: ConnectorAuthenticationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectorAuthenticationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConnectorAuthenticationException":
        return cls(deserialize_json(data), message, response=response)
