"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#TimestampOutOfBoundsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.error_message


class TimestampOutOfBoundsException_(TypedDict, closed=True):
    message: NotRequired["capo_marketplace_metering.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestampOutOfBoundsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestampOutOfBoundsException_:
    out: TimestampOutOfBoundsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TimestampOutOfBoundsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#TimestampOutOfBoundsException``."""

    code: str | None = "TimestampOutOfBoundsException"

    def __init__(
        self,
        data: TimestampOutOfBoundsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TimestampOutOfBoundsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TimestampOutOfBoundsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
