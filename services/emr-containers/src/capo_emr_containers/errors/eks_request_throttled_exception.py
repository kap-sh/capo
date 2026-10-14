"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EKSRequestThrottledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import ServiceError

if TYPE_CHECKING:
    import capo_emr_containers.types.string1024


class EKSRequestThrottledException_(TypedDict, closed=True):
    message: NotRequired["capo_emr_containers.types.string1024.String1024"]


# --- restJson1 ser/de ---
def serialize_json(value: EKSRequestThrottledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EKSRequestThrottledException_:
    out: EKSRequestThrottledException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class EKSRequestThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.emrcontainers#EKSRequestThrottledException``."""

    code: str | None = "EKSRequestThrottledException"

    def __init__(
        self,
        data: EKSRequestThrottledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EKSRequestThrottledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EKSRequestThrottledException":
        return cls(deserialize_json(data), message, response=response)
