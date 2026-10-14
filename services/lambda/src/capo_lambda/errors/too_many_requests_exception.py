"""Generated from Smithy shape ``com.amazonaws.lambda#TooManyRequestsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import ServiceError

if TYPE_CHECKING:
    import capo_lambda.types.string
    import capo_lambda.types.throttle_reason


class TooManyRequestsException_(TypedDict, closed=True):
    retry_after_seconds: NotRequired["capo_lambda.types.string.String"]
    """<p>The number of seconds the caller should wait before retrying.</p>"""
    type: NotRequired["capo_lambda.types.string.String"]
    message: NotRequired["capo_lambda.types.string.String"]
    reason: NotRequired["capo_lambda.types.throttle_reason.ThrottleReason"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_lambda.types.throttle_reason

        out["Reason"] = capo_lambda.types.throttle_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("Reason") is not None:
        import capo_lambda.types.throttle_reason

        out["reason"] = capo_lambda.types.throttle_reason.deserialize_json(
            data["Reason"]
        )
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lambda#TooManyRequestsException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyRequestsException":
        return cls(deserialize_json(data), message, response=response)
