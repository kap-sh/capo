"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GeneratePinDataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value
    import capo_payment_cryptography_data.types.pin_data


class GeneratePinDataOutput(TypedDict, closed=True):
    generation_key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the pin data generation key that Amazon Web Services Payment Cryptography uses for PIN, PVV or PIN Offset generation.</p>"""
    generation_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    encryption_key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses for encrypted pin block generation. For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>"""
    encryption_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    encrypted_pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType"
    """<p>The PIN block encrypted under PEK from Amazon Web Services Payment Cryptography. The encrypted PIN block is a composite of PAN (Primary Account Number) and PIN (Personal Identification Number), generated in accordance with ISO 9564 standard.</p>"""
    pin_data: "capo_payment_cryptography_data.types.pin_data.PinData"
    """<p>The attributes and values Amazon Web Services Payment Cryptography uses for pin data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratePinDataOutput) -> dict:
    out: dict = {}
    out["GenerationKeyArn"] = value["generation_key_arn"]
    out["GenerationKeyCheckValue"] = value["generation_key_check_value"]
    out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["EncryptionKeyCheckValue"] = value["encryption_key_check_value"]
    out["EncryptedPinBlock"] = value["encrypted_pin_block"]
    import capo_payment_cryptography_data.types.pin_data

    out["PinData"] = capo_payment_cryptography_data.types.pin_data.serialize_json(
        value["pin_data"]
    )
    return out


def deserialize_json(data: dict) -> GeneratePinDataOutput:
    out: GeneratePinDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("GenerationKeyArn") is not None:
        out["generation_key_arn"] = data["GenerationKeyArn"]
    else:
        out["generation_key_arn"] = ""
    if data.get("GenerationKeyCheckValue") is not None:
        out["generation_key_check_value"] = data["GenerationKeyCheckValue"]
    else:
        out["generation_key_check_value"] = ""
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    else:
        out["encryption_key_arn"] = ""
    if data.get("EncryptionKeyCheckValue") is not None:
        out["encryption_key_check_value"] = data["EncryptionKeyCheckValue"]
    else:
        out["encryption_key_check_value"] = ""
    if data.get("EncryptedPinBlock") is not None:
        out["encrypted_pin_block"] = data["EncryptedPinBlock"]
    else:
        out["encrypted_pin_block"] = ""
    if data.get("PinData") is not None:
        import capo_payment_cryptography_data.types.pin_data

        out["pin_data"] = (
            capo_payment_cryptography_data.types.pin_data.deserialize_json(
                data["PinData"]
            )
        )
    else:
        import capo_payment_cryptography_data.types._unknown

        out["pin_data"] = (
            capo_payment_cryptography_data.types._unknown.UnknownUnionMember("")
        )
    return out


def redact_sensitive(value: GeneratePinDataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encrypted_pin_block" in value:
        out["encrypted_pin_block"] = "*** Sensitive Data Redacted ***"
    if "pin_data" in value:
        import capo_payment_cryptography_data.types.pin_data

        out["pin_data"] = (
            capo_payment_cryptography_data.types.pin_data.redact_sensitive(
                value["pin_data"]
            )
        )
    return out
