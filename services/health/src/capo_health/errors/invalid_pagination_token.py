"""Generated from Smithy shape ``com.amazonaws.health#InvalidPaginationToken``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_health.errors import ServiceError

if TYPE_CHECKING:
    import capo_health.types.string


class InvalidPaginationToken_(TypedDict, closed=True):
    message: NotRequired["capo_health.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPaginationToken_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPaginationToken_:
    out: InvalidPaginationToken_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidPaginationToken(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.health#InvalidPaginationToken``."""

    code: str | None = "InvalidPaginationToken"

    def __init__(
        self,
        data: InvalidPaginationToken_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPaginationToken",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPaginationToken":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
