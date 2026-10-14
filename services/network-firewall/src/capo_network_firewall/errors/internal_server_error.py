"""Generated from Smithy shape ``com.amazonaws.networkfirewall#InternalServerError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import ServiceError

if TYPE_CHECKING:
    import capo_network_firewall.types.error_message


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["capo_network_firewall.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkfirewall#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(
        self,
        data: InternalServerError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerError":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
