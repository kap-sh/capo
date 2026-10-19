"""Generated from Smithy shape ``com.amazonaws.ram#PermissionVersionsLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class PermissionVersionsLimitExceededException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: PermissionVersionsLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PermissionVersionsLimitExceededException_:
    out: PermissionVersionsLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class PermissionVersionsLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#PermissionVersionsLimitExceededException``."""

    code: str | None = "PermissionVersionsLimitExceededException"

    def __init__(
        self,
        data: PermissionVersionsLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PermissionVersionsLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PermissionVersionsLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
