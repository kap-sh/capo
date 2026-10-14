"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#InvalidInputException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_migrationhub_config.errors import ServiceError

if TYPE_CHECKING:
    import capo_migrationhub_config.types.error_message


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["capo_migrationhub_config.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubconfig#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(
        self,
        data: InvalidInputException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidInputException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
