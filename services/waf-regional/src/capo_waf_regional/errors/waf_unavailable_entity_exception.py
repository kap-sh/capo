"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFUnavailableEntityException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import capo_waf_regional.types.error_message


class WAFUnavailableEntityException_(TypedDict, closed=True):
    message: NotRequired["capo_waf_regional.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFUnavailableEntityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFUnavailableEntityException_:
    out: WAFUnavailableEntityException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class WAFUnavailableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFUnavailableEntityException``."""

    code: str | None = "WAFUnavailableEntityException"

    def __init__(
        self,
        data: WAFUnavailableEntityException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFUnavailableEntityException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFUnavailableEntityException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
