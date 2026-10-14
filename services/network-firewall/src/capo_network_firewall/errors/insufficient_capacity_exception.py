"""Generated from Smithy shape ``com.amazonaws.networkfirewall#InsufficientCapacityException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import ServiceError

if TYPE_CHECKING:
    import capo_network_firewall.types.error_message


class InsufficientCapacityException_(TypedDict, closed=True):
    message: NotRequired["capo_network_firewall.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsufficientCapacityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InsufficientCapacityException_:
    out: InsufficientCapacityException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InsufficientCapacityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkfirewall#InsufficientCapacityException``."""

    code: str | None = "InsufficientCapacityException"

    def __init__(
        self,
        data: InsufficientCapacityException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InsufficientCapacityException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InsufficientCapacityException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
