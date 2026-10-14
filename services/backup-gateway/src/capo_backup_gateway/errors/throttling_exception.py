"""Generated from Smithy shape ``com.amazonaws.backupgateway#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_backup_gateway.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_backup_gateway.types.string


class ThrottlingException_(TypedDict, closed=True):
    error_code: "capo_backup_gateway.types.string.string"
    """<p>Error: TPS has been limited to protect against intentional or unintentional high request volumes.</p>"""
    message: NotRequired["capo_backup_gateway.types.string.string"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("ThrottlingException_.error_code required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backupgateway#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
