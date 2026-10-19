"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyPinDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value


class VerifyPinDataOutput(TypedDict, closed=True):
    verification_key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the PIN encryption key that Amazon Web Services Payment Cryptography uses for PIN or PIN Offset verification.</p>"""
    verification_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    encryption_key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses for encrypted pin block generation.</p>"""
    encryption_key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyPinDataOutput) -> dict:
    out: dict = {}
    out["VerificationKeyArn"] = value["verification_key_arn"]
    out["VerificationKeyCheckValue"] = value["verification_key_check_value"]
    out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["EncryptionKeyCheckValue"] = value["encryption_key_check_value"]
    return out


def deserialize_json(data: dict) -> VerifyPinDataOutput:
    out: VerifyPinDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("VerificationKeyArn") is not None:
        out["verification_key_arn"] = data["VerificationKeyArn"]
    else:
        out["verification_key_arn"] = ""
    if data.get("VerificationKeyCheckValue") is not None:
        out["verification_key_check_value"] = data["VerificationKeyCheckValue"]
    else:
        out["verification_key_check_value"] = ""
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    else:
        out["encryption_key_arn"] = ""
    if data.get("EncryptionKeyCheckValue") is not None:
        out["encryption_key_check_value"] = data["EncryptionKeyCheckValue"]
    else:
        out["encryption_key_check_value"] = ""
    return out
