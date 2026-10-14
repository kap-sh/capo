"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UnauthorizedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_resource_groups.errors import ServiceError

if TYPE_CHECKING:
    import capo_resource_groups.types.error_message


class UnauthorizedException_(TypedDict, closed=True):
    message: NotRequired["capo_resource_groups.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourcegroups#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(
        self,
        data: UnauthorizedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedException":
        return cls(deserialize_json(data), message, response=response)
