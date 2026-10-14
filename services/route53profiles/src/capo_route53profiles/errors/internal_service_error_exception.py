"""Generated from Smithy shape ``com.amazonaws.route53profiles#InternalServiceErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53profiles.errors import ServiceError

if TYPE_CHECKING:
    import capo_route53profiles.types.exception_message


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_route53profiles.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53profiles#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(
        self,
        data: InternalServiceErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServiceErrorException":
        return cls(deserialize_json(data), message, response=response)
