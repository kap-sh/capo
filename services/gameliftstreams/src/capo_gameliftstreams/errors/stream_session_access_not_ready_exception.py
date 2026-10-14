"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionAccessNotReadyException``."""

import zapros
from typing_extensions import TypedDict

from capo_gameliftstreams.errors import DeserializationError, ServiceError


class StreamSessionAccessNotReadyException_(TypedDict, closed=True):
    message: "str"
    """<p>Description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSessionAccessNotReadyException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> StreamSessionAccessNotReadyException_:
    out: StreamSessionAccessNotReadyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError(
            "StreamSessionAccessNotReadyException_.message required"
        )
    return out


class StreamSessionAccessNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionAccessNotReadyException``."""

    code: str | None = "StreamSessionAccessNotReadyException"

    def __init__(
        self,
        data: StreamSessionAccessNotReadyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="StreamSessionAccessNotReadyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "StreamSessionAccessNotReadyException":
        return cls(deserialize_json(data), message, response=response)
