"""Generated from Smithy shape ``com.amazonaws.licensemanager#RedirectException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.location
    import capo_license_manager.types.message


class RedirectException_(TypedDict, closed=True):
    location: NotRequired["capo_license_manager.types.location.Location"]
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedirectException_) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedirectException_:
    out: RedirectException_ = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class RedirectException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#RedirectException``."""

    code: str | None = "RedirectException"

    def __init__(
        self,
        data: RedirectException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RedirectException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RedirectException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
