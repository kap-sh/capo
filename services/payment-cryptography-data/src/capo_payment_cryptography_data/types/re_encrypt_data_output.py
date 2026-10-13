"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#ReEncryptDataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.cipher_text_type
    import capo_payment_cryptography_data.types.key_arn
    import capo_payment_cryptography_data.types.key_check_value


class ReEncryptDataOutput(TypedDict, closed=True):
    key_arn: "capo_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The keyARN (Amazon Resource Name) of the encryption key that Amazon Web Services Payment Cryptography uses for plaintext encryption.</p>"""
    key_check_value: (
        "capo_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.</p> <p>Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.</p>"""
    cipher_text: "capo_payment_cryptography_data.types.cipher_text_type.CipherTextType"
    """<p>The encrypted ciphertext.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReEncryptDataOutput) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["CipherText"] = value["cipher_text"]
    return out


def deserialize_json(data: dict) -> ReEncryptDataOutput:
    out: ReEncryptDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("KeyArn") is not None:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("ReEncryptDataOutput.key_arn required")
    if data.get("KeyCheckValue") is not None:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        raise DeserializationError("ReEncryptDataOutput.key_check_value required")
    if data.get("CipherText") is not None:
        out["cipher_text"] = data["CipherText"]
    else:
        raise DeserializationError("ReEncryptDataOutput.cipher_text required")
    return out


def redact_sensitive(value: ReEncryptDataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cipher_text" in value:
        out["cipher_text"] = "*** Sensitive Data Redacted ***"
    return out
