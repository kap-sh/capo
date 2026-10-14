"""Generated from Smithy shape ``com.amazonaws.pi#InternalServiceError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_pi.errors import ServiceError

if TYPE_CHECKING:
    import capo_pi.types.error_string


class InternalServiceError_(TypedDict, closed=True):
    message: NotRequired["capo_pi.types.error_string.ErrorString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServiceError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServiceError_:
    out: InternalServiceError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServiceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pi#InternalServiceError``."""

    code: str | None = "InternalServiceError"

    def __init__(
        self,
        data: InternalServiceError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServiceError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
