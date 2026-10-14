"""Generated from Smithy shape ``com.amazonaws.connect#InvalidRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.invalid_request_exception_reason
    import capo_connect.types.message


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]
    """<p>The message about the request.</p>"""
    reason: NotRequired[
        "capo_connect.types.invalid_request_exception_reason.InvalidRequestExceptionReason"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_connect.types.invalid_request_exception_reason

        out["Reason"] = (
            capo_connect.types.invalid_request_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_connect.types.invalid_request_exception_reason

        out["reason"] = (
            capo_connect.types.invalid_request_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(
        self,
        data: InvalidRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRequestException":
        return cls(deserialize_json(data), message, response=response)
