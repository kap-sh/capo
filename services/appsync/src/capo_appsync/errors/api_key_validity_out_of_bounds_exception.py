"""Generated from Smithy shape ``com.amazonaws.appsync#ApiKeyValidityOutOfBoundsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import ServiceError

if TYPE_CHECKING:
    import capo_appsync.types.string


class ApiKeyValidityOutOfBoundsException_(TypedDict, closed=True):
    message: NotRequired["capo_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyValidityOutOfBoundsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ApiKeyValidityOutOfBoundsException_:
    out: ApiKeyValidityOutOfBoundsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ApiKeyValidityOutOfBoundsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#ApiKeyValidityOutOfBoundsException``."""

    code: str | None = "ApiKeyValidityOutOfBoundsException"

    def __init__(
        self,
        data: ApiKeyValidityOutOfBoundsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ApiKeyValidityOutOfBoundsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ApiKeyValidityOutOfBoundsException":
        return cls(deserialize_json(data), message, response=response)
