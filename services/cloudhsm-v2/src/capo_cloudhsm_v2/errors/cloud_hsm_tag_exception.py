"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmTagException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.error_message


class CloudHsmTagException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmTagException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmTagException_:
    out: CloudHsmTagException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CloudHsmTagException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmTagException``."""

    code: str | None = "CloudHsmTagException"

    def __init__(
        self,
        data: CloudHsmTagException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmTagException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudHsmTagException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
