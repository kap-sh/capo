"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.error_message


class CloudHsmResourceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudhsm_v2.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudHsmResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudHsmResourceNotFoundException_:
    out: CloudHsmResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CloudHsmResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudhsmv2#CloudHsmResourceNotFoundException``."""

    code: str | None = "CloudHsmResourceNotFoundException"

    def __init__(
        self,
        data: CloudHsmResourceNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmResourceNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CloudHsmResourceNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
