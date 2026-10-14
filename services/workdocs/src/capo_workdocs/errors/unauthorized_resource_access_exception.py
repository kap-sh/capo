"""Generated from Smithy shape ``com.amazonaws.workdocs#UnauthorizedResourceAccessException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import capo_workdocs.types.error_message_type


class UnauthorizedResourceAccessException_(TypedDict, closed=True):
    message: NotRequired["capo_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedResourceAccessException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedResourceAccessException_:
    out: UnauthorizedResourceAccessException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnauthorizedResourceAccessException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#UnauthorizedResourceAccessException``."""

    code: str | None = "UnauthorizedResourceAccessException"

    def __init__(
        self,
        data: UnauthorizedResourceAccessException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedResourceAccessException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnauthorizedResourceAccessException":
        return cls(deserialize_json(data), message, response=response)
