"""Generated from Smithy shape ``com.amazonaws.omics#NotSupportedOperationException``."""

import zapros
from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, ServiceError


class NotSupportedOperationException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NotSupportedOperationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotSupportedOperationException_:
    out: NotSupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotSupportedOperationException_.message required")
    return out


class NotSupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.omics#NotSupportedOperationException``."""

    code: str | None = "NotSupportedOperationException"

    def __init__(
        self,
        data: NotSupportedOperationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotSupportedOperationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotSupportedOperationException":
        return cls(deserialize_json(data), message, response=response)
