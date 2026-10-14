"""Generated from Smithy shape ``com.amazonaws.workspaces#UnsupportedNetworkConfigurationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces.types.exception_message


class UnsupportedNetworkConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedNetworkConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedNetworkConfigurationException_:
    out: UnsupportedNetworkConfigurationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnsupportedNetworkConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#UnsupportedNetworkConfigurationException``."""

    code: str | None = "UnsupportedNetworkConfigurationException"

    def __init__(
        self,
        data: UnsupportedNetworkConfigurationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedNetworkConfigurationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedNetworkConfigurationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
