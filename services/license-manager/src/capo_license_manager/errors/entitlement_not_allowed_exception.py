"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementNotAllowedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.message


class EntitlementNotAllowedException_(TypedDict, closed=True):
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementNotAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementNotAllowedException_:
    out: EntitlementNotAllowedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class EntitlementNotAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#EntitlementNotAllowedException``."""

    code: str | None = "EntitlementNotAllowedException"

    def __init__(
        self,
        data: EntitlementNotAllowedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntitlementNotAllowedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EntitlementNotAllowedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
