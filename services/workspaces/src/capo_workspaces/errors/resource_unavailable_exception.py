"""Generated from Smithy shape ``com.amazonaws.workspaces#ResourceUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces.types.exception_message
    import capo_workspaces.types.non_empty_string


class ResourceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces.types.exception_message.ExceptionMessage"]
    """<p>The exception error message.</p>"""
    resource_id: NotRequired["capo_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the resource that is not available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(
        self,
        data: ResourceUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceUnavailableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
