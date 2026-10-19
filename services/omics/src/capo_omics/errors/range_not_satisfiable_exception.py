"""Generated from Smithy shape ``com.amazonaws.omics#RangeNotSatisfiableException``."""

import zapros
from typing_extensions import TypedDict

from capo_omics.errors import ServiceError


class RangeNotSatisfiableException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RangeNotSatisfiableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RangeNotSatisfiableException_:
    out: RangeNotSatisfiableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class RangeNotSatisfiableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.omics#RangeNotSatisfiableException``."""

    code: str | None = "RangeNotSatisfiableException"

    def __init__(
        self,
        data: RangeNotSatisfiableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="RangeNotSatisfiableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RangeNotSatisfiableException":
        return cls(deserialize_json(data), message, response=response)
