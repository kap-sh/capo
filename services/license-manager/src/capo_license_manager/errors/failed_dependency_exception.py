"""Generated from Smithy shape ``com.amazonaws.licensemanager#FailedDependencyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.message
    import capo_license_manager.types.string


class FailedDependencyException_(TypedDict, closed=True):
    message: NotRequired["capo_license_manager.types.message.Message"]
    error_code: NotRequired["capo_license_manager.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedDependencyException_:
    out: FailedDependencyException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    return out


class FailedDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#FailedDependencyException``."""

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
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "FailedDependencyException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
