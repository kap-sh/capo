"""Generated from Smithy shape ``com.amazonaws.emrcontainers#RequestThrottledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import ServiceError

if TYPE_CHECKING:
    import capo_emr_containers.types.string1024


class RequestThrottledException_(TypedDict, closed=True):
    message: NotRequired["capo_emr_containers.types.string1024.String1024"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestThrottledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestThrottledException_:
    out: RequestThrottledException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class RequestThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.emrcontainers#RequestThrottledException``."""

    code: str | None = "RequestThrottledException"

    def __init__(
        self,
        data: RequestThrottledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestThrottledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RequestThrottledException":
        return cls(deserialize_json(data), message, response=response)
