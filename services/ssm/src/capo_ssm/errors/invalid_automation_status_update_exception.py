"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidAutomationStatusUpdateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidAutomationStatusUpdateException_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidAutomationStatusUpdateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidAutomationStatusUpdateException_:
    out: InvalidAutomationStatusUpdateException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidAutomationStatusUpdateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidAutomationStatusUpdateException``."""

    code: str | None = "InvalidAutomationStatusUpdateException"

    def __init__(
        self,
        data: InvalidAutomationStatusUpdateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAutomationStatusUpdateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidAutomationStatusUpdateException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
