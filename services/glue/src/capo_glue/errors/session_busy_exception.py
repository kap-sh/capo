"""Generated from Smithy shape ``com.amazonaws.glue#SessionBusyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.orchestration_message_string


class SessionBusyException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_glue.types.orchestration_message_string.OrchestrationMessageString"
    ]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionBusyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionBusyException_:
    out: SessionBusyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class SessionBusyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#SessionBusyException``."""

    code: str | None = "SessionBusyException"

    def __init__(
        self,
        data: SessionBusyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SessionBusyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SessionBusyException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
