"""Generated from Smithy shape ``com.amazonaws.ecr#KmsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message
    import capo_ecr.types.kms_error


class KmsException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]
    kms_error: NotRequired["capo_ecr.types.kms_error.KmsError"]
    """<p>The error code returned by KMS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KmsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "kms_error" in value:
        out["kmsError"] = value["kms_error"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KmsException_:
    out: KmsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("kmsError") is not None:
        out["kms_error"] = data["kmsError"]
    return out


class KmsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#KmsException``."""

    code: str | None = "KmsException"

    def __init__(
        self,
        data: KmsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KmsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
