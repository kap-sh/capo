"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseUsageException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.message


class LicenseUsageException_(TypedDict, closed=True):
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseUsageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseUsageException_:
    out: LicenseUsageException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class LicenseUsageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#LicenseUsageException``."""

    code: str | None = "LicenseUsageException"

    def __init__(
        self,
        data: LicenseUsageException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LicenseUsageException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LicenseUsageException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
