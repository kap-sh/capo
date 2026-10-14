"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class ReplicationAlreadyExists_(TypedDict, closed=True):
    error_code: NotRequired["capo_efs.types.error_code.ErrorCode"]
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationAlreadyExists_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ReplicationAlreadyExists_:
    out: ReplicationAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ReplicationAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#ReplicationAlreadyExists``."""

    code: str | None = "ReplicationAlreadyExists"

    def __init__(
        self,
        data: ReplicationAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReplicationAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ReplicationAlreadyExists":
        return cls(deserialize_json(data), message, response=response)
