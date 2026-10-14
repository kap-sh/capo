"""Generated from Smithy shape ``com.amazonaws.drs#UninitializedAccountException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import ServiceError

if TYPE_CHECKING:
    import capo_drs.types.large_bounded_string


class UninitializedAccountException_(TypedDict, closed=True):
    message: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]


# --- restJson1 ser/de ---
def serialize_json(value: UninitializedAccountException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> UninitializedAccountException_:
    out: UninitializedAccountException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    return out


class UninitializedAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.drs#UninitializedAccountException``."""

    code: str | None = "UninitializedAccountException"

    def __init__(
        self,
        data: UninitializedAccountException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UninitializedAccountException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UninitializedAccountException":
        return cls(deserialize_json(data), message, response=response)
