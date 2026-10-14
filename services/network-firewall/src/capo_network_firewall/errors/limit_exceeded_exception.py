"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import ServiceError

if TYPE_CHECKING:
    import capo_network_firewall.types.error_message


class LimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_network_firewall.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkfirewall#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(
        self,
        data: LimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
