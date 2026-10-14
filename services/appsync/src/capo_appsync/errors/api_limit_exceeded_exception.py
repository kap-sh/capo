"""Generated from Smithy shape ``com.amazonaws.appsync#ApiLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import ServiceError

if TYPE_CHECKING:
    import capo_appsync.types.string


class ApiLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_appsync.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ApiLimitExceededException_:
    out: ApiLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ApiLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appsync#ApiLimitExceededException``."""

    code: str | None = "ApiLimitExceededException"

    def __init__(
        self,
        data: ApiLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ApiLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ApiLimitExceededException":
        return cls(deserialize_json(data), message, response=response)
