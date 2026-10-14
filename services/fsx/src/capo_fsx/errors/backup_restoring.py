"""Generated from Smithy shape ``com.amazonaws.fsx#BackupRestoring``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message
    import capo_fsx.types.file_system_id


class BackupRestoring_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    """<p>The ID of a file system being restored from the backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupRestoring_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackupRestoring_:
    out: BackupRestoring_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    return out


class BackupRestoring(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#BackupRestoring``."""

    code: str | None = "BackupRestoring"

    def __init__(
        self,
        data: BackupRestoring_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackupRestoring",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BackupRestoring":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
