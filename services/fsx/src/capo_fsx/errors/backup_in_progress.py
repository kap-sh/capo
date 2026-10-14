"""Generated from Smithy shape ``com.amazonaws.fsx#BackupInProgress``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class BackupInProgress_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupInProgress_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackupInProgress_:
    out: BackupInProgress_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class BackupInProgress(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#BackupInProgress``."""

    code: str | None = "BackupInProgress"

    def __init__(
        self,
        data: BackupInProgress_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackupInProgress",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BackupInProgress":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
