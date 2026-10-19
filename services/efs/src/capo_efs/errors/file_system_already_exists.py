"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message
    import capo_efs.types.file_system_id


class FileSystemAlreadyExists_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemAlreadyExists_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    out["FileSystemId"] = value["file_system_id"]
    return out


def deserialize_json(data: dict) -> FileSystemAlreadyExists_:
    out: FileSystemAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    else:
        out["file_system_id"] = ""
    return out


class FileSystemAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#FileSystemAlreadyExists``."""

    code: str | None = "FileSystemAlreadyExists"

    def __init__(
        self,
        data: FileSystemAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileSystemAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FileSystemAlreadyExists":
        return cls(deserialize_json(data), message, response=response)
