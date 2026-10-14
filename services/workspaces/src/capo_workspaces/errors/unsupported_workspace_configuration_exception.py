"""Generated from Smithy shape ``com.amazonaws.workspaces#UnsupportedWorkspaceConfigurationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces.types.exception_message


class UnsupportedWorkspaceConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedWorkspaceConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedWorkspaceConfigurationException_:
    out: UnsupportedWorkspaceConfigurationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnsupportedWorkspaceConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#UnsupportedWorkspaceConfigurationException``."""

    code: str | None = "UnsupportedWorkspaceConfigurationException"

    def __init__(
        self,
        data: UnsupportedWorkspaceConfigurationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedWorkspaceConfigurationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedWorkspaceConfigurationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
