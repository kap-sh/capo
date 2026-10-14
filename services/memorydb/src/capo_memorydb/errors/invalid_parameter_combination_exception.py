"""Generated from Smithy shape ``com.amazonaws.memorydb#InvalidParameterCombinationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import capo_memorydb.types.aws_query_error_message


class InvalidParameterCombinationException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_memorydb.types.aws_query_error_message.AwsQueryErrorMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidParameterCombinationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidParameterCombinationException_:
    out: InvalidParameterCombinationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidParameterCombinationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#InvalidParameterCombinationException``."""

    code: str | None = "InvalidParameterCombinationException"

    def __init__(
        self,
        data: InvalidParameterCombinationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterCombinationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParameterCombinationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
