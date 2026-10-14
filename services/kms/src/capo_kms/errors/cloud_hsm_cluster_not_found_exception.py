"""Generated from Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class CloudHsmClusterNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmClusterNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmClusterNotFoundException_:
    out: CloudHsmClusterNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CloudHsmClusterNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotFoundException``."""

    code: str | None = "CloudHsmClusterNotFoundException"

    def __init__(
        self,
        data: CloudHsmClusterNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmClusterNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudHsmClusterNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
