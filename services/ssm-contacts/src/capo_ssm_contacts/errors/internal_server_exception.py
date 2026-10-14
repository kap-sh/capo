"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.retry_after_seconds
    import capo_ssm_contacts.types.string


class InternalServerException_(TypedDict, closed=True):
    message: "capo_ssm_contacts.types.string.String"
    retry_after_seconds: "capo_ssm_contacts.types.retry_after_seconds.RetryAfterSeconds"
    """Advice to clients on when the call can be safely retried"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["RetryAfterSeconds"] = value.get("retry_after_seconds", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    if data.get("RetryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["RetryAfterSeconds"]
    else:
        out["retry_after_seconds"] = 0
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmcontacts#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
