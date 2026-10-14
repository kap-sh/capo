"""Generated from Smithy shape ``com.amazonaws.efs#DependencyTimeout``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class DependencyTimeout_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyTimeout_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyTimeout_:
    out: DependencyTimeout_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("DependencyTimeout_.error_code required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DependencyTimeout(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#DependencyTimeout``."""

    code: str | None = "DependencyTimeout"

    def __init__(
        self,
        data: DependencyTimeout_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyTimeout",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DependencyTimeout":
        return cls(deserialize_json(data), message, response=response)
