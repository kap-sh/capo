"""Generated from Smithy shape ``com.amazonaws.healthlake#ConversationNotFoundException``."""

import zapros
from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, ServiceError


class ConversationNotFoundException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversationNotFoundException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConversationNotFoundException_:
    out: ConversationNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConversationNotFoundException_.message required")
    return out


class ConversationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.healthlake#ConversationNotFoundException``."""

    code: str | None = "ConversationNotFoundException"

    def __init__(
        self,
        data: ConversationNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConversationNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConversationNotFoundException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
