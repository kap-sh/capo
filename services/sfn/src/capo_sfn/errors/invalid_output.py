"""Generated from Smithy shape ``com.amazonaws.sfn#InvalidOutput``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.error_message


class InvalidOutput_(TypedDict, closed=True):
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidOutput_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidOutput_:
    out: InvalidOutput_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidOutput(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#InvalidOutput``."""

    code: str | None = "InvalidOutput"

    def __init__(
        self,
        data: InvalidOutput_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOutput",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidOutput":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
