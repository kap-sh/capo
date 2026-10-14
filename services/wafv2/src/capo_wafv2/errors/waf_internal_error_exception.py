"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFInternalErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_wafv2.types.error_message


class WAFInternalErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInternalErrorException_:
    out: WAFInternalErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class WAFInternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFInternalErrorException``."""

    code: str | None = "WAFInternalErrorException"

    def __init__(
        self,
        data: WAFInternalErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInternalErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFInternalErrorException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
