"""Generated from Smithy shape ``com.amazonaws.kms#ExpiredImportTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class ExpiredImportTokenException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpiredImportTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpiredImportTokenException_:
    out: ExpiredImportTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ExpiredImportTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#ExpiredImportTokenException``."""

    code: str | None = "ExpiredImportTokenException"

    def __init__(
        self,
        data: ExpiredImportTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredImportTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExpiredImportTokenException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
