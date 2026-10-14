"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#TerminalStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_jobs_data_plane.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.error_message


class TerminalStateException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_jobs_data_plane.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TerminalStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TerminalStateException_:
    out: TerminalStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TerminalStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotjobsdataplane#TerminalStateException``."""

    code: str | None = "TerminalStateException"

    def __init__(
        self,
        data: TerminalStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TerminalStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TerminalStateException":
        return cls(deserialize_json(data), message, response=response)
