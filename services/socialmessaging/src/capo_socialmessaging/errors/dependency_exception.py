"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DependencyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import ServiceError

if TYPE_CHECKING:
    import capo_socialmessaging.types.error_message


class DependencyException_(TypedDict, closed=True):
    message: NotRequired["capo_socialmessaging.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyException_:
    out: DependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.socialmessaging#DependencyException``."""

    code: str | None = "DependencyException"

    def __init__(
        self,
        data: DependencyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="DependencyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DependencyException":
        return cls(deserialize_json(data), message, response=response)
