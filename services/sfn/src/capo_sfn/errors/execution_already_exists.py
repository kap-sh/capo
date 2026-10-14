"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.error_message


class ExecutionAlreadyExists_(TypedDict, closed=True):
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionAlreadyExists_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionAlreadyExists_:
    out: ExecutionAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ExecutionAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#ExecutionAlreadyExists``."""

    code: str | None = "ExecutionAlreadyExists"

    def __init__(
        self,
        data: ExecutionAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExecutionAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExecutionAlreadyExists":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
