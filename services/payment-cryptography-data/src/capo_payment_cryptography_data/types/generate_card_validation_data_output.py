"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateCardValidationDataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value
    import capo_payment_cryptography_data.types.validation_data_type


class GenerateCardValidationDataOutput(TypedDict, closed=True):
    key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the CVK encryption key that Amazon Web Services Payment Cryptography uses to generate CVV or CSC.</p>"""
    key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    validation_data: (
        "capo_payment_cryptography_data.types.validation_data_type.ValidationDataType"
    )
    """<p>The CVV or CSC value that Amazon Web Services Payment Cryptography generates for the card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateCardValidationDataOutput) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["ValidationData"] = value["validation_data"]
    return out


def deserialize_json(data: dict) -> GenerateCardValidationDataOutput:
    out: GenerateCardValidationDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        out["key_arn"] = ""
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        out["key_check_value"] = ""
    if data.get("ValidationData") is not None:
        out["validation_data"] = data["ValidationData"]
    else:
        out["validation_data"] = ""
    return out


def redact_sensitive(value: GenerateCardValidationDataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "validation_data" in value:
        out["validation_data"] = "*** Sensitive Data Redacted ***"
    return out
