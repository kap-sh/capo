"""Generated from Smithy shape ``com.amazonaws.fsx#MissingFileSystemConfiguration``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class MissingFileSystemConfiguration_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MissingFileSystemConfiguration_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MissingFileSystemConfiguration_:
    out: MissingFileSystemConfiguration_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class MissingFileSystemConfiguration(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#MissingFileSystemConfiguration``."""

    code: str | None = "MissingFileSystemConfiguration"

    def __init__(
        self,
        data: MissingFileSystemConfiguration_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingFileSystemConfiguration",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MissingFileSystemConfiguration":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
