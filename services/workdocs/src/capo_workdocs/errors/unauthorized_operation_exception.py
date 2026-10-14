"""Generated from Smithy shape ``com.amazonaws.workdocs#UnauthorizedOperationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import capo_workdocs.types.error_message_type
    import capo_workdocs.types.exception_code_type


class UnauthorizedOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_workdocs.types.error_message_type.ErrorMessageType"]
    code: NotRequired["capo_workdocs.types.exception_code_type.ExceptionCodeType"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> UnauthorizedOperationException_:
    out: UnauthorizedOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    return out


class UnauthorizedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#UnauthorizedOperationException``."""

    code: str | None = "UnauthorizedOperationException"

    def __init__(
        self,
        data: UnauthorizedOperationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedOperationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedOperationException":
        return cls(deserialize_json(data), message, response=response)
