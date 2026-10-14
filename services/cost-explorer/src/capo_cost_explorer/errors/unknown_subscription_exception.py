"""Generated from Smithy shape ``com.amazonaws.costexplorer#UnknownSubscriptionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import capo_cost_explorer.types.error_message


class UnknownSubscriptionException_(TypedDict, closed=True):
    message: NotRequired["capo_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnknownSubscriptionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnknownSubscriptionException_:
    out: UnknownSubscriptionException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnknownSubscriptionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#UnknownSubscriptionException``."""

    code: str | None = "UnknownSubscriptionException"

    def __init__(
        self,
        data: UnknownSubscriptionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnknownSubscriptionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnknownSubscriptionException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
