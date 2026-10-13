"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#Ibm3624PinOffset``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.decimalization_table_type
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.hex_length_equals1
    import capo_payment_cryptography_data.types.pin_validation_data_type


class Ibm3624PinOffset(TypedDict, closed=True):
    encrypted_pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType"
    """<p>The encrypted PIN block data. According to ISO 9564 standard, a PIN Block is an encoded representation of a payment card Personal Account Number (PAN) and the cardholder Personal Identification Number (PIN).</p>"""
    decimalization_table: "capo_payment_cryptography_data.types.decimalization_table_type.DecimalizationTableType"
    """<p>The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.</p>"""
    pin_validation_data_pad_character: (
        "capo_payment_cryptography_data.types.hex_length_equals1.HexLengthEquals1"
    )
    """<p>The padding character for validation data.</p>"""
    pin_validation_data: "capo_payment_cryptography_data.types.pin_validation_data_type.PinValidationDataType"
    """<p>The unique data for cardholder identification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ibm3624PinOffset) -> dict:
    out: dict = {}
    out["EncryptedPinBlock"] = value["encrypted_pin_block"]
    out["DecimalizationTable"] = value["decimalization_table"]
    out["PinValidationDataPadCharacter"] = value["pin_validation_data_pad_character"]
    out["PinValidationData"] = value["pin_validation_data"]
    return out


def deserialize_json(data: dict) -> Ibm3624PinOffset:
    out: Ibm3624PinOffset = {}  # type: ignore[typeddict-item]
    if data.get("EncryptedPinBlock") is not None:
        out["encrypted_pin_block"] = data["EncryptedPinBlock"]
    else:
        raise DeserializationError("Ibm3624PinOffset.encrypted_pin_block required")
    if data.get("DecimalizationTable") is not None:
        out["decimalization_table"] = data["DecimalizationTable"]
    else:
        raise DeserializationError("Ibm3624PinOffset.decimalization_table required")
    if data.get("PinValidationDataPadCharacter") is not None:
        out["pin_validation_data_pad_character"] = data["PinValidationDataPadCharacter"]
    else:
        raise DeserializationError(
            "Ibm3624PinOffset.pin_validation_data_pad_character required"
        )
    if data.get("PinValidationData") is not None:
        out["pin_validation_data"] = data["PinValidationData"]
    else:
        raise DeserializationError("Ibm3624PinOffset.pin_validation_data required")
    return out


def redact_sensitive(value: Ibm3624PinOffset) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encrypted_pin_block" in value:
        out["encrypted_pin_block"] = "*** Sensitive Data Redacted ***"
    if "decimalization_table" in value:
        out["decimalization_table"] = "*** Sensitive Data Redacted ***"
    if "pin_validation_data" in value:
        out["pin_validation_data"] = "*** Sensitive Data Redacted ***"
    return out
