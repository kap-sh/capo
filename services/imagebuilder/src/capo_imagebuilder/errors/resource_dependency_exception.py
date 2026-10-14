"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ResourceDependencyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import ServiceError

if TYPE_CHECKING:
    import capo_imagebuilder.types.error_message


class ResourceDependencyException_(TypedDict, closed=True):
    message: NotRequired["capo_imagebuilder.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceDependencyException_:
    out: ResourceDependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.imagebuilder#ResourceDependencyException``."""

    code: str | None = "ResourceDependencyException"

    def __init__(
        self,
        data: ResourceDependencyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDependencyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceDependencyException":
        return cls(deserialize_json(data), message, response=response)
