"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ServiceException``."""

import zapros
from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import ServiceError


class ServiceException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ServiceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(
        self,
        data: ServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceException":
        return cls(deserialize_json(data), message, response=response)
