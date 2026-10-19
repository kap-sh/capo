"""Generated from Smithy shape ``com.amazonaws.neptunedata#MemoryLimitExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_neptunedata.errors import ServiceError


class MemoryLimitExceededException_(TypedDict, closed=True):
    detailed_message: "str"
    """<p>A detailed message describing the problem.</p>"""
    request_id: "str"
    """<p>The ID of the request that failed.</p>"""
    code: "str"
    """<p>The HTTP status code returned with the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryLimitExceededException_) -> dict:
    out: dict = {}
    out["detailedMessage"] = value["detailed_message"]
    out["requestId"] = value["request_id"]
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> MemoryLimitExceededException_:
    out: MemoryLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("detailedMessage") is not None:
        out["detailed_message"] = data["detailedMessage"]
    else:
        out["detailed_message"] = ""
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        out["request_id"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    return out


class MemoryLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptunedata#MemoryLimitExceededException``."""

    code: str | None = "MemoryLimitExceededException"

    def __init__(
        self,
        data: MemoryLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="MemoryLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MemoryLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
