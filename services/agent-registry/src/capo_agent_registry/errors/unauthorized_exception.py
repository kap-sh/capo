"""Generated from Smithy shape ``com.amazonaws.agentregistry#UnauthorizedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry.errors import ServiceError

if TYPE_CHECKING:
    import capo_agent_registry.types.non_blank_string


class UnauthorizedException_(TypedDict, closed=True):
    message: NotRequired["capo_agent_registry.types.non_blank_string.NonBlankString"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.agentregistry#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(self, data: UnauthorizedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "UnauthorizedException":
        return cls(deserialize_json(data), message)
