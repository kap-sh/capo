"""Generated from Smithy shape ``com.amazonaws.securityhub#InvalidAccessException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_securityhub.errors import ServiceError

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class InvalidAccessException_(TypedDict, closed=True):
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidAccessException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> InvalidAccessException_:
    out: InvalidAccessException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    return out


class InvalidAccessException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityhub#InvalidAccessException``."""

    code: str | None = "InvalidAccessException"

    def __init__(
        self,
        data: InvalidAccessException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAccessException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidAccessException":
        return cls(deserialize_json(data), message, response=response)
