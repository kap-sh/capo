"""Generated from Smithy shape ``com.amazonaws.qbusiness#ExternalResourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_qbusiness.errors import ServiceError

if TYPE_CHECKING:
    import capo_qbusiness.types.error_message


class ExternalResourceException_(TypedDict, closed=True):
    message: "capo_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: ExternalResourceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExternalResourceException_:
    out: ExternalResourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class ExternalResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#ExternalResourceException``."""

    code: str | None = "ExternalResourceException"

    def __init__(
        self,
        data: ExternalResourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExternalResourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExternalResourceException":
        return cls(deserialize_json(data), message, response=response)
