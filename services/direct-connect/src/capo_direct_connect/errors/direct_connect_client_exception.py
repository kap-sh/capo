"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectClientException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_direct_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_direct_connect.types.error_message


class DirectConnectClientException_(TypedDict, closed=True):
    message: NotRequired["capo_direct_connect.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectClientException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectConnectClientException_:
    out: DirectConnectClientException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DirectConnectClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directconnect#DirectConnectClientException``."""

    code: str | None = "DirectConnectClientException"

    def __init__(
        self,
        data: DirectConnectClientException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectConnectClientException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DirectConnectClientException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
