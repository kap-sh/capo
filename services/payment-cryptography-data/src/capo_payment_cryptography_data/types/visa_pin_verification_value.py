"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VisaPinVerificationValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.integer_range_between0_and6


class VisaPinVerificationValue(TypedDict, closed=True):
    encrypted_pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType"
    """<p>The encrypted PIN block data to verify.</p>"""
    pin_verification_key_index: "capo_payment_cryptography_data.types.integer_range_between0_and6.IntegerRangeBetween0And6"
    """<p>The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisaPinVerificationValue) -> dict:
    out: dict = {}
    out["EncryptedPinBlock"] = value["encrypted_pin_block"]
    out["PinVerificationKeyIndex"] = value["pin_verification_key_index"]
    return out


def deserialize_json(data: dict) -> VisaPinVerificationValue:
    out: VisaPinVerificationValue = {}  # type: ignore[typeddict-item]
    if data.get("EncryptedPinBlock") is not None:
        out["encrypted_pin_block"] = data["EncryptedPinBlock"]
    else:
        raise DeserializationError(
            "VisaPinVerificationValue.encrypted_pin_block required"
        )
    if data.get("PinVerificationKeyIndex") is not None:
        out["pin_verification_key_index"] = data["PinVerificationKeyIndex"]
    else:
        raise DeserializationError(
            "VisaPinVerificationValue.pin_verification_key_index required"
        )
    return out


def redact_sensitive(value: VisaPinVerificationValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encrypted_pin_block" in value:
        out["encrypted_pin_block"] = "*** Sensitive Data Redacted ***"
    return out
