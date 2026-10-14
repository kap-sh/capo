"""Generated from Smithy shape ``com.amazonaws.shield#InvalidResourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_shield.errors import ServiceError

if TYPE_CHECKING:
    import capo_shield.types.error_message


class InvalidResourceException_(TypedDict, closed=True):
    message: NotRequired["capo_shield.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResourceException_:
    out: InvalidResourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.shield#InvalidResourceException``."""

    code: str | None = "InvalidResourceException"

    def __init__(
        self,
        data: InvalidResourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
