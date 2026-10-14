"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServiceException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import ServiceError


class ServiceException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServiceException``."""

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
            is_retryable=True,
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
