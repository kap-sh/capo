"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesDefaultRoleNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces.types.exception_message


class WorkspacesDefaultRoleNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesDefaultRoleNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesDefaultRoleNotFoundException_:
    out: WorkspacesDefaultRoleNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class WorkspacesDefaultRoleNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#WorkspacesDefaultRoleNotFoundException``."""

    code: str | None = "WorkspacesDefaultRoleNotFoundException"

    def __init__(
        self,
        data: WorkspacesDefaultRoleNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WorkspacesDefaultRoleNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WorkspacesDefaultRoleNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
