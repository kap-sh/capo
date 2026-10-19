"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class ResourceShareLimitExceededException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceShareLimitExceededException_:
    out: ResourceShareLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class ResourceShareLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceShareLimitExceededException``."""

    code: str | None = "ResourceShareLimitExceededException"

    def __init__(
        self,
        data: ResourceShareLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceShareLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceShareLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
