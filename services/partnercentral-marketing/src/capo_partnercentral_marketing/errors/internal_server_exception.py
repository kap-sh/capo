"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.error_message


class InternalServerException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    retry_after_seconds: NotRequired["int"]
    """Seconds before retry."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "retry_after_seconds" in value:
        out["RetryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_cbor(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("RetryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["RetryAfterSeconds"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_cbor(data), message, response=response)
