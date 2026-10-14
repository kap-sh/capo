"""Generated from Smithy shape ``com.amazonaws.ram#UnmatchedPolicyPermissionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class UnmatchedPolicyPermissionException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: UnmatchedPolicyPermissionException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnmatchedPolicyPermissionException_:
    out: UnmatchedPolicyPermissionException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "UnmatchedPolicyPermissionException_.message required"
        )
    return out


class UnmatchedPolicyPermissionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#UnmatchedPolicyPermissionException``."""

    code: str | None = "UnmatchedPolicyPermissionException"

    def __init__(
        self,
        data: UnmatchedPolicyPermissionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnmatchedPolicyPermissionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnmatchedPolicyPermissionException":
        return cls(deserialize_json(data), message, response=response)
