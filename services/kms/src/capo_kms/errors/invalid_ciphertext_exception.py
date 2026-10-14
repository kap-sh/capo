"""Generated from Smithy shape ``com.amazonaws.kms#InvalidCiphertextException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class InvalidCiphertextException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidCiphertextException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidCiphertextException_:
    out: InvalidCiphertextException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidCiphertextException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidCiphertextException``."""

    code: str | None = "InvalidCiphertextException"

    def __init__(
        self,
        data: InvalidCiphertextException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCiphertextException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidCiphertextException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
