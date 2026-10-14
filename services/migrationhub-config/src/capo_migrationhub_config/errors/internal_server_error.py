"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#InternalServerError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_migrationhub_config.errors import ServiceError

if TYPE_CHECKING:
    import capo_migrationhub_config.types.error_message


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["capo_migrationhub_config.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubconfig#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(
        self,
        data: InternalServerError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
