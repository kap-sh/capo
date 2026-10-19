"""Generated from Smithy shape ``com.amazonaws.simpledbv2#InvalidNextTokenException``."""

import zapros
from typing_extensions import TypedDict

from capo_simpledbv2.errors import ServiceError


class InvalidNextTokenException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidNextTokenException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidNextTokenException_:
    out: InvalidNextTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InvalidNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#InvalidNextTokenException``."""

    code: str | None = "InvalidNextTokenException"

    def __init__(
        self,
        data: InvalidNextTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidNextTokenException":
        return cls(deserialize_json(data), message, response=response)
