"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#InvalidStateTransitionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_jobs_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.error_message


class InvalidStateTransitionException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_jobs_data_plane.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidStateTransitionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidStateTransitionException_:
    out: InvalidStateTransitionException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidStateTransitionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotjobsdataplane#InvalidStateTransitionException``."""

    code: str | None = "InvalidStateTransitionException"

    def __init__(
        self,
        data: InvalidStateTransitionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateTransitionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidStateTransitionException":
        return cls(deserialize_json(data), message, response=response)
