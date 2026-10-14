"""Generated from Smithy shape ``com.amazonaws.groundstation#ResourceInUseException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import ServiceError


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.groundstation#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(
        self,
        data: ResourceInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceInUseException":
        return cls(deserialize_json(data), message, response=response)
