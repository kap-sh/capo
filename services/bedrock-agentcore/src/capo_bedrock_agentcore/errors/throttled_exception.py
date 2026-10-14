"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ThrottledException``."""

import zapros
from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, ServiceError


class ThrottledException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ThrottledException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottledException_:
    out: ThrottledException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottledException_.message required")
    return out


class ThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#ThrottledException``."""

    code: str | None = "ThrottledException"

    def __init__(
        self,
        data: ThrottledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottledException":
        return cls(deserialize_json(data), message, response=response)
