"""Generated from Smithy shape ``com.amazonaws.kms#IncorrectKeyMaterialException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class IncorrectKeyMaterialException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncorrectKeyMaterialException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncorrectKeyMaterialException_:
    out: IncorrectKeyMaterialException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class IncorrectKeyMaterialException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#IncorrectKeyMaterialException``."""

    code: str | None = "IncorrectKeyMaterialException"

    def __init__(
        self,
        data: IncorrectKeyMaterialException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncorrectKeyMaterialException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IncorrectKeyMaterialException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
