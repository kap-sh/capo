"""Generated from Smithy shape ``com.amazonaws.glue#InvalidIntegrationStateFault``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import ServiceError

if TYPE_CHECKING:
    import capo_glue.types.integration_error_message


class InvalidIntegrationStateFault_(TypedDict, closed=True):
    message: NotRequired[
        "capo_glue.types.integration_error_message.IntegrationErrorMessage"
    ]
    """<p>A message describing the problem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidIntegrationStateFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidIntegrationStateFault_:
    out: InvalidIntegrationStateFault_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidIntegrationStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glue#InvalidIntegrationStateFault``."""

    code: str | None = "InvalidIntegrationStateFault"

    def __init__(
        self,
        data: InvalidIntegrationStateFault_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidIntegrationStateFault",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidIntegrationStateFault":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
