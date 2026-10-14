"""Generated from Smithy shape ``com.amazonaws.transfer#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import ServiceError

if TYPE_CHECKING:
    import capo_transfer.types.retry_after_seconds


class ThrottlingException_(TypedDict, closed=True):
    retry_after_seconds: NotRequired[
        "capo_transfer.types.retry_after_seconds.RetryAfterSeconds"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "retry_after_seconds" in value:
        out["RetryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("RetryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["RetryAfterSeconds"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transfer#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
