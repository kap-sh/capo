"""Generated from Smithy shape ``com.amazonaws.neptunedata#IllegalArgumentException``."""

import zapros
from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError, ServiceError


class IllegalArgumentException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request in question.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IllegalArgumentException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> IllegalArgumentException_:
    out: IllegalArgumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("detailedMessage") is not None:
        out["detailed_message"] = data["detailedMessage"]
    else:
        raise DeserializationError(
            "IllegalArgumentException_.detailed_message required"
        )
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("IllegalArgumentException_.request_id required")
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("IllegalArgumentException_.code required")
    return out


class IllegalArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#IllegalArgumentException``."""

    code: str | None = "IllegalArgumentException"

    def __init__(
        self,
        data: IllegalArgumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalArgumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IllegalArgumentException":
        return cls(deserialize_json(data), message, response=response)
