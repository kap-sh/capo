"""Generated from Smithy shape ``com.amazonaws.licensemanager#NoEntitlementsAllowedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.message


class NoEntitlementsAllowedException_(TypedDict, closed=True):
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoEntitlementsAllowedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoEntitlementsAllowedException_:
    out: NoEntitlementsAllowedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NoEntitlementsAllowedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#NoEntitlementsAllowedException``."""

    code: str | None = "NoEntitlementsAllowedException"

    def __init__(
        self,
        data: NoEntitlementsAllowedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoEntitlementsAllowedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoEntitlementsAllowedException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
