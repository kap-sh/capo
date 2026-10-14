"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#IdempotencyConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.error_message


class IdempotencyConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_marketplace_metering.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdempotencyConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdempotencyConflictException_:
    out: IdempotencyConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class IdempotencyConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#IdempotencyConflictException``."""

    code: str | None = "IdempotencyConflictException"

    def __init__(
        self,
        data: IdempotencyConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotencyConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IdempotencyConflictException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
