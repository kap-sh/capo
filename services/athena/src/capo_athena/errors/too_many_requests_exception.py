"""Generated from Smithy shape ``com.amazonaws.athena#TooManyRequestsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_athena.errors import ServiceError

if TYPE_CHECKING:
    import capo_athena.types.error_message
    import capo_athena.types.throttle_reason


class TooManyRequestsException_(TypedDict, closed=True):
    message: NotRequired["capo_athena.types.error_message.ErrorMessage"]
    reason: NotRequired["capo_athena.types.throttle_reason.ThrottleReason"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_athena.types.throttle_reason

        out["Reason"] = capo_athena.types.throttle_reason.serialize_aws_json_1_1(
            value["reason"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_athena.types.throttle_reason

        out["reason"] = capo_athena.types.throttle_reason.deserialize_aws_json_1_1(
            data["Reason"]
        )
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.athena#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(
        self,
        data: TooManyRequestsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequestsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyRequestsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
