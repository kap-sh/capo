"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DecryptDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.cipher_text_type
    import capo_payment_cryptography_data.types.encryption_decryption_attributes
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.wrapped_key


class DecryptDataInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses for ciphertext decryption.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>"""
    cipher_text: "capo_payment_cryptography_data.types.cipher_text_type.CipherTextType"
    """<p>The ciphertext to decrypt.</p>"""
    decryption_attributes: "capo_payment_cryptography_data.types.encryption_decryption_attributes.EncryptionDecryptionAttributes"
    """<p>The encryption key type and attributes for ciphertext decryption.</p>"""
    wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key for ciphertext decryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecryptDataInput) -> dict:
    out: dict = {}
    out["CipherText"] = value["cipher_text"]
    import capo_payment_cryptography_data.types.encryption_decryption_attributes

    out["DecryptionAttributes"] = (
        capo_payment_cryptography_data.types.encryption_decryption_attributes.serialize_json(
            value["decryption_attributes"]
        )
    )
    if "wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["WrappedKey"] = (
            capo_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["wrapped_key"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecryptDataInput:
    out: DecryptDataInput = {}  # type: ignore[typeddict-item]
    if data.get("CipherText") is not None:
        out["cipher_text"] = data["CipherText"]
    else:
        raise DeserializationError("DecryptDataInput.cipher_text required")
    if data.get("DecryptionAttributes") is not None:
        import capo_payment_cryptography_data.types.encryption_decryption_attributes

        out["decryption_attributes"] = (
            capo_payment_cryptography_data.types.encryption_decryption_attributes.deserialize_json(
                data["DecryptionAttributes"]
            )
        )
    else:
        raise DeserializationError("DecryptDataInput.decryption_attributes required")
    if data.get("WrappedKey") is not None:
        import capo_payment_cryptography_data.types.wrapped_key

        out["wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["WrappedKey"]
            )
        )
    return out


def redact_sensitive(value: DecryptDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cipher_text" in value:
        out["cipher_text"] = "*** Sensitive Data Redacted ***"
    if "decryption_attributes" in value:
        import capo_payment_cryptography_data.types.encryption_decryption_attributes

        out["decryption_attributes"] = (
            capo_payment_cryptography_data.types.encryption_decryption_attributes.redact_sensitive(
                value["decryption_attributes"]
            )
        )
    if "wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.redact_sensitive(
                value["wrapped_key"]
            )
        )
    return out
