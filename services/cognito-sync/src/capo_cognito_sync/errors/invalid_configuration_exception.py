"""Generated from Smithy shape ``com.amazonaws.cognitosync#InvalidConfigurationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_cognito_sync.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_cognito_sync.types.exception_message


class InvalidConfigurationException_(TypedDict, closed=True):
    message: "capo_cognito_sync.types.exception_message.ExceptionMessage"
    """Message returned by InvalidConfigurationException."""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidConfigurationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidConfigurationException_:
    out: InvalidConfigurationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidConfigurationException_.message required")
    return out


class InvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitosync#InvalidConfigurationException``."""

    code: str | None = "InvalidConfigurationException"

    def __init__(
        self,
        data: InvalidConfigurationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidConfigurationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidConfigurationException":
        return cls(deserialize_json(data), message, response=response)
