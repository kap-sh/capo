"""Generated from Smithy shape ``com.amazonaws.kms#KMSInvalidSignatureException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class KMSInvalidSignatureException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSInvalidSignatureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSInvalidSignatureException_:
    out: KMSInvalidSignatureException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class KMSInvalidSignatureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KMSInvalidSignatureException``."""

    code: str | None = "KMSInvalidSignatureException"

    def __init__(
        self,
        data: KMSInvalidSignatureException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInvalidSignatureException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KMSInvalidSignatureException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
