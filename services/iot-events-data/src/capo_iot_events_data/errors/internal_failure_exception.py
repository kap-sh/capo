"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#InternalFailureException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot_events_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot_events_data.types.error_message


class InternalFailureException_(TypedDict, closed=True):
    message: NotRequired["capo_iot_events_data.types.error_message.ErrorMessage"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ioteventsdata#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(
        self,
        data: InternalFailureException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalFailureException":
        return cls(deserialize_json(data), message, response=response)
