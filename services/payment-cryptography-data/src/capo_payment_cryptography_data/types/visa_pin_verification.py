"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VisaPinVerification``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.integer_range_between0_and6
    import capo_payment_cryptography_data.types.verification_value_type


class VisaPinVerification(TypedDict, closed=True):
    pin_verification_key_index: "capo_payment_cryptography_data.types.integer_range_between0_and6.IntegerRangeBetween0And6"
    """<p>The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).</p>"""
    verification_value: "capo_payment_cryptography_data.types.verification_value_type.VerificationValueType"
    """<p>Parameters that are required to generate or verify Visa PVV (PIN Verification Value).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisaPinVerification) -> dict:
    out: dict = {}
    out["PinVerificationKeyIndex"] = value["pin_verification_key_index"]
    out["VerificationValue"] = value["verification_value"]
    return out


def deserialize_json(data: dict) -> VisaPinVerification:
    out: VisaPinVerification = {}  # type: ignore[typeddict-item]
    if data.get("PinVerificationKeyIndex") is not None:
        out["pin_verification_key_index"] = data["PinVerificationKeyIndex"]
    else:
        out["pin_verification_key_index"] = 0
    if data.get("VerificationValue") is not None:
        out["verification_value"] = data["VerificationValue"]
    else:
        out["verification_value"] = ""
    return out


def redact_sensitive(value: VisaPinVerification) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "verification_value" in value:
        out["verification_value"] = "*** Sensitive Data Redacted ***"
    return out
