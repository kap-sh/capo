"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.error_message


class CloudHsmResourceLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmResourceLimitExceededException_:
    out: CloudHsmResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CloudHsmResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceLimitExceededException``."""

    code: str | None = "CloudHsmResourceLimitExceededException"

    def __init__(
        self,
        data: CloudHsmResourceLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmResourceLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudHsmResourceLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
