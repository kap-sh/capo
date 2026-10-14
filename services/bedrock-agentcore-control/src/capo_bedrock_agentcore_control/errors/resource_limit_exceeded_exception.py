"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceLimitExceededException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import ServiceError


class ResourceLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(
        self,
        data: ResourceLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
