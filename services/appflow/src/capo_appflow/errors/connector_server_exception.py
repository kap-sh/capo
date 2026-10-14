"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import ServiceError

if TYPE_CHECKING:
    import capo_appflow.types.error_message


class ConnectorServerException_(TypedDict, closed=True):
    message: NotRequired["capo_appflow.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorServerException_:
    out: ConnectorServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConnectorServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appflow#ConnectorServerException``."""

    code: str | None = "ConnectorServerException"

    def __init__(
        self,
        data: ConnectorServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectorServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConnectorServerException":
        return cls(deserialize_json(data), message, response=response)
