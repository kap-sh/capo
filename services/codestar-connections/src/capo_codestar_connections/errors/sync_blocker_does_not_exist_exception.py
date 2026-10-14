"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SyncBlockerDoesNotExistException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codestar_connections.errors import ServiceError

if TYPE_CHECKING:
    import capo_codestar_connections.types.error_message


class SyncBlockerDoesNotExistException_(TypedDict, closed=True):
    message: NotRequired["capo_codestar_connections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerDoesNotExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerDoesNotExistException_:
    out: SyncBlockerDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SyncBlockerDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codestarconnections#SyncBlockerDoesNotExistException``."""

    code: str | None = "SyncBlockerDoesNotExistException"

    def __init__(
        self,
        data: SyncBlockerDoesNotExistException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SyncBlockerDoesNotExistException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SyncBlockerDoesNotExistException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
