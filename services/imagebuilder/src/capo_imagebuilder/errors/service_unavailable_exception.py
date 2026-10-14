"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ServiceUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import capo_imagebuilder.types.error_message


class ServiceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#ServiceUnavailableException``."""

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
