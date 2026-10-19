"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EncryptionFailure``."""

import zapros
from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import ServiceError


class EncryptionFailure_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionFailure_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EncryptionFailure_:
    out: EncryptionFailure_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class EncryptionFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EncryptionFailure``."""

    code: str | None = "EncryptionFailure"

    def __init__(
        self,
        data: EncryptionFailure_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionFailure",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EncryptionFailure":
        return cls(deserialize_json(data), message, response=response)
