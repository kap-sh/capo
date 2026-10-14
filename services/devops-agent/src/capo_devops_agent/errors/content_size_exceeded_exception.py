"""Generated from Smithy shape ``com.amazonaws.devopsagent#ContentSizeExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, ServiceError


class ContentSizeExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ContentSizeExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ContentSizeExceededException_:
    out: ContentSizeExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ContentSizeExceededException_.message required")
    return out


class ContentSizeExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsagent#ContentSizeExceededException``."""

    code: str | None = "ContentSizeExceededException"

    def __init__(
        self,
        data: ContentSizeExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContentSizeExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ContentSizeExceededException":
        return cls(deserialize_json(data), message, response=response)
