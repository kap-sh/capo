"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.access_denied_exception_reason
    import capo_partnercentral_marketing.types.error_message


class AccessDeniedException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    reason: NotRequired[
        "capo_partnercentral_marketing.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    ]
    """Why the caller was refused, when the refusal is about the caller's Partner Central state rather than IAM."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import capo_partnercentral_marketing.types.access_denied_exception_reason

        out["Reason"] = (
            capo_partnercentral_marketing.types.access_denied_exception_reason.serialize_cbor(
                value["reason"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_marketing.types.access_denied_exception_reason

        out["reason"] = (
            capo_partnercentral_marketing.types.access_denied_exception_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(
        self,
        data: AccessDeniedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedException":
        return cls(deserialize_cbor(data), message, response=response)
