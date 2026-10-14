"""Generated from Smithy shape ``com.amazonaws.backupgateway#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_backup_gateway.errors import ServiceError

if TYPE_CHECKING:
    import capo_backup_gateway.types.string


class InternalServerException_(TypedDict, closed=True):
    error_code: NotRequired["capo_backup_gateway.types.string.string"]
    """<p>A description of which internal error occured.</p>"""
    message: NotRequired["capo_backup_gateway.types.string.string"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backupgateway#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
