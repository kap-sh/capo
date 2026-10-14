"""Generated from Smithy shape ``com.amazonaws.workmail#DirectoryInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmail.types.string


class DirectoryInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryInUseException_:
    out: DirectoryInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DirectoryInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#DirectoryInUseException``."""

    code: str | None = "DirectoryInUseException"

    def __init__(
        self,
        data: DirectoryInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DirectoryInUseException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
