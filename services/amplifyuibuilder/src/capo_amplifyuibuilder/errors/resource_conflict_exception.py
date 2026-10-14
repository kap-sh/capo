"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ResourceConflictException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_amplifyuibuilder.errors import ServiceError


class ResourceConflictException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceConflictException_:
    out: ResourceConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.amplifyuibuilder#ResourceConflictException``."""

    code: str | None = "ResourceConflictException"

    def __init__(
        self,
        data: ResourceConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceConflictException":
        return cls(deserialize_json(data), message, response=response)
