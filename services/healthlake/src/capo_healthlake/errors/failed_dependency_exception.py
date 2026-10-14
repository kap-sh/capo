"""Generated from Smithy shape ``com.amazonaws.healthlake#FailedDependencyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import ServiceError

if TYPE_CHECKING:
    import capo_healthlake.types.health_lake_string


class FailedDependencyException_(TypedDict, closed=True):
    message: NotRequired["capo_healthlake.types.health_lake_string.HealthLakeString"]
    """A message describing the error."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailedDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FailedDependencyException_:
    out: FailedDependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class FailedDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.healthlake#FailedDependencyException``."""

    code: str | None = "FailedDependencyException"

    def __init__(
        self,
        data: FailedDependencyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FailedDependencyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FailedDependencyException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
