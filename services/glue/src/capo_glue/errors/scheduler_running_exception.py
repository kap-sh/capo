"""Generated from Smithy shape ``com.amazonaws.glue#SchedulerRunningException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.message_string


class SchedulerRunningException_(TypedDict, closed=True):
    message: NotRequired["capo_glue.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchedulerRunningException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchedulerRunningException_:
    out: SchedulerRunningException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SchedulerRunningException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#SchedulerRunningException``."""

    code: str | None = "SchedulerRunningException"

    def __init__(
        self,
        data: SchedulerRunningException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SchedulerRunningException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SchedulerRunningException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
