"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotNotFound``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class SnapshotNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotNotFound_:
    out: SnapshotNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SnapshotNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#SnapshotNotFound``."""

    code: str | None = "SnapshotNotFound"

    def __init__(
        self,
        data: SnapshotNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SnapshotNotFound":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
