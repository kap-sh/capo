"""Generated from Smithy shape ``com.amazonaws.workspaces#OperatingSystemNotCompatibleException``."""

import zapros
from typing_extensions import TypedDict

from capo_workspaces.errors import ServiceError


class OperatingSystemNotCompatibleException_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperatingSystemNotCompatibleException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> OperatingSystemNotCompatibleException_:
    out: OperatingSystemNotCompatibleException_ = {}  # type: ignore[typeddict-item]
    return out


class OperatingSystemNotCompatibleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspaces#OperatingSystemNotCompatibleException``."""

    code: str | None = "OperatingSystemNotCompatibleException"

    def __init__(
        self,
        data: OperatingSystemNotCompatibleException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperatingSystemNotCompatibleException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OperatingSystemNotCompatibleException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
