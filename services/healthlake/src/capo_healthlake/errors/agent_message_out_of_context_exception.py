"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentMessageOutOfContextException``."""

import zapros
from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, ServiceError


class AgentMessageOutOfContextException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgentMessageOutOfContextException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgentMessageOutOfContextException_:
    out: AgentMessageOutOfContextException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError(
            "AgentMessageOutOfContextException_.message required"
        )
    return out


class AgentMessageOutOfContextException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.healthlake#AgentMessageOutOfContextException``."""

    code: str | None = "AgentMessageOutOfContextException"

    def __init__(
        self,
        data: AgentMessageOutOfContextException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AgentMessageOutOfContextException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AgentMessageOutOfContextException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
