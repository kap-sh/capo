"""Generated from Smithy shape ``com.amazonaws.workspaces#IncompatibleApplicationsException``."""

import zapros
from typing_extensions import TypedDict

from capo_workspaces.errors import ServiceError


class IncompatibleApplicationsException_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibleApplicationsException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> IncompatibleApplicationsException_:
    out: IncompatibleApplicationsException_ = {}  # type: ignore[typeddict-item]
    return out


class IncompatibleApplicationsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#IncompatibleApplicationsException``."""

    code: str | None = "IncompatibleApplicationsException"

    def __init__(
        self,
        data: IncompatibleApplicationsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleApplicationsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IncompatibleApplicationsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
