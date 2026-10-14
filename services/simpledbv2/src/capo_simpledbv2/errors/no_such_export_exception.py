"""Generated from Smithy shape ``com.amazonaws.simpledbv2#NoSuchExportException``."""

import zapros
from typing_extensions import TypedDict

from capo_simpledbv2.errors import DeserializationError, ServiceError


class NoSuchExportException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NoSuchExportException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoSuchExportException_:
    out: NoSuchExportException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NoSuchExportException_.message required")
    return out


class NoSuchExportException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.simpledbv2#NoSuchExportException``."""

    code: str | None = "NoSuchExportException"

    def __init__(
        self,
        data: NoSuchExportException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchExportException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoSuchExportException":
        return cls(deserialize_json(data), message, response=response)
