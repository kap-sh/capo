"""Generated from Smithy shape ``com.amazonaws.elementalinference#TooManyRequestException``."""

import zapros
from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, ServiceError


class TooManyRequestException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestException_:
    out: TooManyRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("TooManyRequestException_.message required")
    return out


class TooManyRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elementalinference#TooManyRequestException``."""

    code: str | None = "TooManyRequestException"

    def __init__(
        self,
        data: TooManyRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="TooManyRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyRequestException":
        return cls(deserialize_json(data), message, response=response)
