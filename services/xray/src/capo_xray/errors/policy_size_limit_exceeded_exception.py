"""Generated from Smithy shape ``com.amazonaws.xray#PolicySizeLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import ServiceError

if TYPE_CHECKING:
    import capo_xray.types.error_message


class PolicySizeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicySizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicySizeLimitExceededException_:
    out: PolicySizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class PolicySizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#PolicySizeLimitExceededException``."""

    code: str | None = "PolicySizeLimitExceededException"

    def __init__(
        self,
        data: PolicySizeLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicySizeLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PolicySizeLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
