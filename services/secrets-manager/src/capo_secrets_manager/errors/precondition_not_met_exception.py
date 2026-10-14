"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PreconditionNotMetException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_secrets_manager.types.error_message


class PreconditionNotMetException_(TypedDict, closed=True):
    message: NotRequired["capo_secrets_manager.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreconditionNotMetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreconditionNotMetException_:
    out: PreconditionNotMetException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class PreconditionNotMetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#PreconditionNotMetException``."""

    code: str | None = "PreconditionNotMetException"

    def __init__(
        self,
        data: PreconditionNotMetException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionNotMetException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "PreconditionNotMetException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
