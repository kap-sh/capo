"""Generated from Smithy shape ``com.amazonaws.health#UnsupportedLocale``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_health.errors import ServiceError

if TYPE_CHECKING:
    import capo_health.types.string


class UnsupportedLocale_(TypedDict, closed=True):
    message: NotRequired["capo_health.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedLocale_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedLocale_:
    out: UnsupportedLocale_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnsupportedLocale(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.health#UnsupportedLocale``."""

    code: str | None = "UnsupportedLocale"

    def __init__(
        self,
        data: UnsupportedLocale_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedLocale",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedLocale":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
