"""Generated from Smithy shape ``com.amazonaws.rum#PolicyNotFoundException``."""

import zapros
from typing_extensions import TypedDict

from capo_rum.errors import DeserializationError, ServiceError


class PolicyNotFoundException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: PolicyNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyNotFoundException_:
    out: PolicyNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PolicyNotFoundException_.message required")
    return out


class PolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rum#PolicyNotFoundException``."""

    code: str | None = "PolicyNotFoundException"

    def __init__(
        self,
        data: PolicyNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicyNotFoundException":
        return cls(deserialize_json(data), message, response=response)
