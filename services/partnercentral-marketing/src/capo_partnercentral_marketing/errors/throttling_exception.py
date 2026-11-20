"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.error_message


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    retry_after_seconds: NotRequired["int"]
    """Seconds before retry."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "retry_after_seconds" in value:
        out["RetryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_cbor(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("RetryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["RetryAfterSeconds"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_cbor(data), message, response=response)
