"""Generated from Smithy shape ``com.amazonaws.athena#SessionAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_athena.errors import ServiceError

if TYPE_CHECKING:
    import capo_athena.types.error_message


class SessionAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_athena.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionAlreadyExistsException_:
    out: SessionAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SessionAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.athena#SessionAlreadyExistsException``."""

    code: str | None = "SessionAlreadyExistsException"

    def __init__(
        self,
        data: SessionAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SessionAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
