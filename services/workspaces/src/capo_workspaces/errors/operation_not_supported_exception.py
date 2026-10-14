"""Generated from Smithy shape ``com.amazonaws.workspaces#OperationNotSupportedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces.types.exception_error_code
    import capo_workspaces.types.exception_message


class OperationNotSupportedException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.exception_message.ExceptionMessage"]
    """<p>The exception error message.</p>"""
    reason: NotRequired["capo_workspaces.types.exception_error_code.ExceptionErrorCode"]
    """<p>The exception error reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationNotSupportedException_:
    out: OperationNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out


class OperationNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#OperationNotSupportedException``."""

    code: str | None = "OperationNotSupportedException"

    def __init__(
        self,
        data: OperationNotSupportedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationNotSupportedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OperationNotSupportedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
