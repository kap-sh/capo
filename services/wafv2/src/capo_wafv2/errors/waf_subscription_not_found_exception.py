"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFSubscriptionNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_wafv2.types.error_message


class WAFSubscriptionNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_wafv2.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFSubscriptionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFSubscriptionNotFoundException_:
    out: WAFSubscriptionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class WAFSubscriptionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFSubscriptionNotFoundException``."""

    code: str | None = "WAFSubscriptionNotFoundException"

    def __init__(
        self,
        data: WAFSubscriptionNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFSubscriptionNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFSubscriptionNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
