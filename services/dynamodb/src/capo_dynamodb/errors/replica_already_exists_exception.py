"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import capo_dynamodb.types.error_message


class ReplicaAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_dynamodb.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaAlreadyExistsException_:
    out: ReplicaAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ReplicaAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ReplicaAlreadyExistsException``."""

    code: str | None = "ReplicaAlreadyExistsException"

    def __init__(
        self,
        data: ReplicaAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReplicaAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ReplicaAlreadyExistsException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
