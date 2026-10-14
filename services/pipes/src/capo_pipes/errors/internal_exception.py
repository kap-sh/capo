"""Generated from Smithy shape ``com.amazonaws.pipes#InternalException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError, ServiceError


class InternalException_(TypedDict, closed=True):
    message: "str"
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the action that caused the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalException_:
    out: InternalException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalException_.message required")
    return out


class InternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pipes#InternalException``."""

    code: str | None = "InternalException"

    def __init__(
        self,
        data: InternalException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalException":
        return cls(deserialize_json(data), message, response=response)
