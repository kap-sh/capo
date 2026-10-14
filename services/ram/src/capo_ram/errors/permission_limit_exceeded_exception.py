"""Generated from Smithy shape ``com.amazonaws.ram#PermissionLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class PermissionLimitExceededException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: PermissionLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PermissionLimitExceededException_:
    out: PermissionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PermissionLimitExceededException_.message required")
    return out


class PermissionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#PermissionLimitExceededException``."""

    code: str | None = "PermissionLimitExceededException"

    def __init__(
        self,
        data: PermissionLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PermissionLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
