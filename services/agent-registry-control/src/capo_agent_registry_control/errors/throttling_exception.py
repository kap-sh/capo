"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import ServiceError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.non_blank_string


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_agent_registry_control.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.agentregistrycontrol#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ThrottlingException":
        return cls(deserialize_json(data), message)
