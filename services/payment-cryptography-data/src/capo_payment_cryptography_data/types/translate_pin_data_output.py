"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslatePinDataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value


class TranslatePinDataOutput(TypedDict, closed=True):
    pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType"
    """<p>The outgoing encrypted PIN block data after translation.</p>"""
    key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses to encrypt outgoing PIN block data after translation.</p>"""
    key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslatePinDataOutput) -> dict:
    out: dict = {}
    out["PinBlock"] = value["pin_block"]
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    return out


def deserialize_json(data: dict) -> TranslatePinDataOutput:
    out: TranslatePinDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("PinBlock") is not None:
        out["pin_block"] = data["PinBlock"]
    else:
        out["pin_block"] = ""
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        out["key_arn"] = ""
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        out["key_check_value"] = ""
    return out


def redact_sensitive(value: TranslatePinDataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pin_block" in value:
        out["pin_block"] = "*** Sensitive Data Redacted ***"
    return out
