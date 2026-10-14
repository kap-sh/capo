"""Generated from Smithy shape ``com.amazonaws.simpledbv2#NumberExportsLimitExceeded``."""

import zapros
from typing_extensions import TypedDict

from capo_simpledbv2.errors import DeserializationError, ServiceError


class NumberExportsLimitExceeded_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NumberExportsLimitExceeded_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NumberExportsLimitExceeded_:
    out: NumberExportsLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NumberExportsLimitExceeded_.message required")
    return out


class NumberExportsLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#NumberExportsLimitExceeded``."""

    code: str | None = "NumberExportsLimitExceeded"

    def __init__(
        self,
        data: NumberExportsLimitExceeded_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NumberExportsLimitExceeded",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NumberExportsLimitExceeded":
        return cls(deserialize_json(data), message, response=response)
