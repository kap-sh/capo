"""Generated from Smithy shape ``com.amazonaws.fsx#SourceBackupUnavailable``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.backup_id
    import capo_fsx.types.error_message


class SourceBackupUnavailable_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]
    backup_id: NotRequired["capo_fsx.types.backup_id.BackupId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceBackupUnavailable_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceBackupUnavailable_:
    out: SourceBackupUnavailable_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("BackupId") is not None:
        out["backup_id"] = data["BackupId"]
    return out


class SourceBackupUnavailable(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#SourceBackupUnavailable``."""

    code: str | None = "SourceBackupUnavailable"

    def __init__(
        self,
        data: SourceBackupUnavailable_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SourceBackupUnavailable",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SourceBackupUnavailable":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
