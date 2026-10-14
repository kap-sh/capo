"""Generated from Smithy shape ``com.amazonaws.health#ConcurrentModificationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_health.errors import ServiceError

if TYPE_CHECKING:
    import capo_health.types.string


class ConcurrentModificationException_(TypedDict, closed=True):
    message: NotRequired["capo_health.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConcurrentModificationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConcurrentModificationException_:
    out: ConcurrentModificationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConcurrentModificationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.health#ConcurrentModificationException``."""

    code: str | None = "ConcurrentModificationException"

    def __init__(
        self,
        data: ConcurrentModificationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConcurrentModificationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConcurrentModificationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
