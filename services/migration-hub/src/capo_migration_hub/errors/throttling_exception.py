"""Generated from Smithy shape ``com.amazonaws.migrationhub#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_migration_hub.errors import ServiceError

if TYPE_CHECKING:
    import capo_migration_hub.types.error_message
    import capo_migration_hub.types.retry_after_seconds


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_migration_hub.types.error_message.ErrorMessage"
    """<p>A message that provides information about the exception.</p>"""
    retry_after_seconds: (
        "capo_migration_hub.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>The number of seconds the caller should wait before retrying.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["RetryAfterSeconds"] = value.get("retry_after_seconds", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("RetryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["RetryAfterSeconds"]
    else:
        out["retry_after_seconds"] = 0
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhub#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
