"""Generated from Smithy shape ``com.amazonaws.launchwizard#ResourceLimitException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_launch_wizard.errors import ServiceError


class ResourceLimitException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitException_:
    out: ResourceLimitException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceLimitException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.launchwizard#ResourceLimitException``."""

    code: str | None = "ResourceLimitException"

    def __init__(
        self,
        data: ResourceLimitException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceLimitException":
        return cls(deserialize_json(data), message, response=response)
