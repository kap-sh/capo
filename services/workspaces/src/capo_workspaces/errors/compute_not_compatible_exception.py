"""Generated from Smithy shape ``com.amazonaws.workspaces#ComputeNotCompatibleException``."""

import zapros
from typing_extensions import TypedDict

from capo_workspaces.errors import ServiceError


class ComputeNotCompatibleException_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeNotCompatibleException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeNotCompatibleException_:
    out: ComputeNotCompatibleException_ = {}  # type: ignore[typeddict-item]
    return out


class ComputeNotCompatibleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#ComputeNotCompatibleException``."""

    code: str | None = "ComputeNotCompatibleException"

    def __init__(
        self,
        data: ComputeNotCompatibleException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ComputeNotCompatibleException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ComputeNotCompatibleException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
