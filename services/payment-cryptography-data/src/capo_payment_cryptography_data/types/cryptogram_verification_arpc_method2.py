"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CryptogramVerificationArpcMethod2``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.hex_length_equals8
    import capo_payment_cryptography_data.types.proprietary_authentication_data_type


class CryptogramVerificationArpcMethod2(TypedDict, closed=True):
    card_status_update: (
        "capo_payment_cryptography_data.types.hex_length_equals8.HexLengthEquals8"
    )
    """<p>The data indicating whether the issuer approves or declines an online transaction using an EMV chip card.</p>"""
    proprietary_authentication_data: NotRequired[
        "capo_payment_cryptography_data.types.proprietary_authentication_data_type.ProprietaryAuthenticationDataType"
    ]
    """<p>The proprietary authentication data used by issuer for communication during online transaction using an EMV chip card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CryptogramVerificationArpcMethod2) -> dict:
    out: dict = {}
    out["CardStatusUpdate"] = value["card_status_update"]
    if "proprietary_authentication_data" in value:
        out["ProprietaryAuthenticationData"] = value["proprietary_authentication_data"]
    return out


def deserialize_json(data: dict) -> CryptogramVerificationArpcMethod2:
    out: CryptogramVerificationArpcMethod2 = {}  # type: ignore[typeddict-item]
    if data.get("CardStatusUpdate") is not None:
        out["card_status_update"] = data["CardStatusUpdate"]
    else:
        out["card_status_update"] = ""
    if data.get("ProprietaryAuthenticationData") is not None:
        out["proprietary_authentication_data"] = data["ProprietaryAuthenticationData"]
    return out


def redact_sensitive(value: CryptogramVerificationArpcMethod2) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "proprietary_authentication_data" in value:
        out["proprietary_authentication_data"] = "*** Sensitive Data Redacted ***"
    return out
