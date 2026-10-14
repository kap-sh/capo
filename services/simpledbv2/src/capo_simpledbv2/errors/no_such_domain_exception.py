"""Generated from Smithy shape ``com.amazonaws.simpledbv2#NoSuchDomainException``."""

import zapros
from typing_extensions import TypedDict

from capo_simpledbv2.errors import DeserializationError, ServiceError


class NoSuchDomainException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NoSuchDomainException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoSuchDomainException_:
    out: NoSuchDomainException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NoSuchDomainException_.message required")
    return out


class NoSuchDomainException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#NoSuchDomainException``."""

    code: str | None = "NoSuchDomainException"

    def __init__(
        self,
        data: NoSuchDomainException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchDomainException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchDomainException":
        return cls(deserialize_json(data), message, response=response)
