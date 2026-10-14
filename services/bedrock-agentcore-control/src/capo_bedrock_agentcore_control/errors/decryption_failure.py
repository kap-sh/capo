"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DecryptionFailure``."""

import zapros
from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError, ServiceError


class DecryptionFailure_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: DecryptionFailure_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DecryptionFailure_:
    out: DecryptionFailure_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DecryptionFailure_.message required")
    return out


class DecryptionFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DecryptionFailure``."""

    code: str | None = "DecryptionFailure"

    def __init__(
        self,
        data: DecryptionFailure_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DecryptionFailure",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DecryptionFailure":
        return cls(deserialize_json(data), message, response=response)
