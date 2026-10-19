"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#Ibm3624RandomPin``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.decimalization_table_type
    import capo_payment_cryptography_data.types.hex_length_equals1
    import capo_payment_cryptography_data.types.pin_validation_data_type


class Ibm3624RandomPin(TypedDict, closed=True):
    decimalization_table: "capo_payment_cryptography_data.types.decimalization_table_type.DecimalizationTableType"
    """<p>The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.</p>"""
    pin_validation_data_pad_character: (
        "capo_payment_cryptography_data.types.hex_length_equals1.HexLengthEquals1"
    )
    """<p>The padding character for validation data.</p>"""
    pin_validation_data: "capo_payment_cryptography_data.types.pin_validation_data_type.PinValidationDataType"
    """<p>The unique data for cardholder identification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ibm3624RandomPin) -> dict:
    out: dict = {}
    out["DecimalizationTable"] = value["decimalization_table"]
    out["PinValidationDataPadCharacter"] = value["pin_validation_data_pad_character"]
    out["PinValidationData"] = value["pin_validation_data"]
    return out


def deserialize_json(data: dict) -> Ibm3624RandomPin:
    out: Ibm3624RandomPin = {}  # type: ignore[typeddict-item]
    if data.get("DecimalizationTable") is not None:
        out["decimalization_table"] = data["DecimalizationTable"]
    else:
        out["decimalization_table"] = ""
    if data.get("PinValidationDataPadCharacter") is not None:
        out["pin_validation_data_pad_character"] = data["PinValidationDataPadCharacter"]
    else:
        out["pin_validation_data_pad_character"] = ""
    if data.get("PinValidationData") is not None:
        out["pin_validation_data"] = data["PinValidationData"]
    else:
        out["pin_validation_data"] = ""
    return out


def redact_sensitive(value: Ibm3624RandomPin) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "decimalization_table" in value:
        out["decimalization_table"] = "*** Sensitive Data Redacted ***"
    if "pin_validation_data" in value:
        out["pin_validation_data"] = "*** Sensitive Data Redacted ***"
    return out
