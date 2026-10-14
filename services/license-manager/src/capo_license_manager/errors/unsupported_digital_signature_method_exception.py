"""Generated from Smithy shape ``com.amazonaws.licensemanager#UnsupportedDigitalSignatureMethodException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.message


class UnsupportedDigitalSignatureMethodException_(TypedDict, closed=True):
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedDigitalSignatureMethodException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedDigitalSignatureMethodException_:
    out: UnsupportedDigitalSignatureMethodException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnsupportedDigitalSignatureMethodException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#UnsupportedDigitalSignatureMethodException``."""

    code: str | None = "UnsupportedDigitalSignatureMethodException"

    def __init__(
        self,
        data: UnsupportedDigitalSignatureMethodException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedDigitalSignatureMethodException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedDigitalSignatureMethodException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
