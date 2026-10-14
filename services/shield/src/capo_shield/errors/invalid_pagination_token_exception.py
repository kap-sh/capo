"""Generated from Smithy shape ``com.amazonaws.shield#InvalidPaginationTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import ServiceError

if TYPE_CHECKING:
    import capo_shield.types.error_message


class InvalidPaginationTokenException_(TypedDict, closed=True):
    message: NotRequired["capo_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPaginationTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPaginationTokenException_:
    out: InvalidPaginationTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidPaginationTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidPaginationTokenException``."""

    code: str | None = "InvalidPaginationTokenException"

    def __init__(
        self,
        data: InvalidPaginationTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPaginationTokenException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
