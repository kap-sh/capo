"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerificationFailedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.verification_failed_reason


class VerificationFailedException_(TypedDict, closed=True):
    reason: "capo_payment_cryptography_data.types.verification_failed_reason.VerificationFailedReason"
    """<p>The reason for the exception.</p>"""
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: VerificationFailedException_) -> dict:
    out: dict = {}
    out["Reason"] = value["reason"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> VerificationFailedException_:
    out: VerificationFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("VerificationFailedException_.reason required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("VerificationFailedException_.message required")
    return out


class VerificationFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.paymentcryptographydata#VerificationFailedException``."""

    code: str | None = "VerificationFailedException"

    def __init__(
        self,
        data: VerificationFailedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="VerificationFailedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "VerificationFailedException":
        return cls(deserialize_json(data), message, response=response)
