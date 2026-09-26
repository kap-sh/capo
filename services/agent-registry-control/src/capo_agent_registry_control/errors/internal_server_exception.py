"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import ServiceError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.non_blank_string


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_agent_registry_control.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.agentregistrycontrol#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message)
