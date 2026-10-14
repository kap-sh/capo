"""Generated from Smithy shape ``com.amazonaws.workspaces#OperationInProgressException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces.types.exception_message


class OperationInProgressException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationInProgressException_:
    out: OperationInProgressException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class OperationInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#OperationInProgressException``."""

    code: str | None = "OperationInProgressException"

    def __init__(
        self,
        data: OperationInProgressException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationInProgressException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OperationInProgressException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
