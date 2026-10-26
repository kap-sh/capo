"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#ReEncryptDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.cipher_text_type
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.re_encryption_attributes
    import capo_payment_cryptography_data.types.wrapped_key


class ReEncryptDataInput(TypedDict, closed=True):
    incoming_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key of incoming ciphertext data.</p> <p>When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.</p>"""
    outgoing_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key of outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>"""
    cipher_text: "capo_payment_cryptography_data.types.cipher_text_type.CipherTextType"
    """<p>Ciphertext to be encrypted. The minimum allowed length is 16 bytes and maximum allowed length is 4096 bytes.</p>"""
    incoming_encryption_attributes: "capo_payment_cryptography_data.types.re_encryption_attributes.ReEncryptionAttributes"
    """<p>The attributes and values for incoming ciphertext.</p>"""
    outgoing_encryption_attributes: "capo_payment_cryptography_data.types.re_encryption_attributes.ReEncryptionAttributes"
    """<p>The attributes and values for outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>"""
    incoming_wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key of incoming ciphertext data.</p>"""
    outgoing_wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key of outgoing ciphertext data after encryption by Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReEncryptDataInput) -> dict:
    out: dict = {}
    out["OutgoingKeyIdentifier"] = value["outgoing_key_identifier"]
    out["CipherText"] = value["cipher_text"]
    import capo_payment_cryptography_data.types.re_encryption_attributes

    out["IncomingEncryptionAttributes"] = (
        capo_payment_cryptography_data.types.re_encryption_attributes.serialize_json(
            value["incoming_encryption_attributes"]
        )
    )
    import capo_payment_cryptography_data.types.re_encryption_attributes

    out["OutgoingEncryptionAttributes"] = (
        capo_payment_cryptography_data.types.re_encryption_attributes.serialize_json(
            value["outgoing_encryption_attributes"]
        )
    )
    if "incoming_wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["IncomingWrappedKey"] = (
            capo_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["incoming_wrapped_key"]
            )
        )
    if "outgoing_wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["OutgoingWrappedKey"] = (
            capo_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["outgoing_wrapped_key"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReEncryptDataInput:
    out: ReEncryptDataInput = {}  # type: ignore[typeddict-item]
    if data.get("OutgoingKeyIdentifier") is not None:
        out["outgoing_key_identifier"] = data["OutgoingKeyIdentifier"]
    else:
        out["outgoing_key_identifier"] = ""
    if data.get("CipherText") is not None:
        out["cipher_text"] = data["CipherText"]
    else:
        out["cipher_text"] = ""
    if data.get("IncomingEncryptionAttributes") is not None:
        import capo_payment_cryptography_data.types.re_encryption_attributes

        out["incoming_encryption_attributes"] = (
            capo_payment_cryptography_data.types.re_encryption_attributes.deserialize_json(
                data["IncomingEncryptionAttributes"]
            )
        )
    else:
        out["incoming_encryption_attributes"] = {"$unknown": {"name": ""}}
    if data.get("OutgoingEncryptionAttributes") is not None:
        import capo_payment_cryptography_data.types.re_encryption_attributes

        out["outgoing_encryption_attributes"] = (
            capo_payment_cryptography_data.types.re_encryption_attributes.deserialize_json(
                data["OutgoingEncryptionAttributes"]
            )
        )
    else:
        out["outgoing_encryption_attributes"] = {"$unknown": {"name": ""}}
    if data.get("IncomingWrappedKey") is not None:
        import capo_payment_cryptography_data.types.wrapped_key

        out["incoming_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["IncomingWrappedKey"]
            )
        )
    if data.get("OutgoingWrappedKey") is not None:
        import capo_payment_cryptography_data.types.wrapped_key

        out["outgoing_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["OutgoingWrappedKey"]
            )
        )
    return out


def redact_sensitive(value: ReEncryptDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cipher_text" in value:
        out["cipher_text"] = "*** Sensitive Data Redacted ***"
    if "incoming_encryption_attributes" in value:
        import capo_payment_cryptography_data.types.re_encryption_attributes

        out["incoming_encryption_attributes"] = (
            capo_payment_cryptography_data.types.re_encryption_attributes.redact_sensitive(
                value["incoming_encryption_attributes"]
            )
        )
    if "outgoing_encryption_attributes" in value:
        import capo_payment_cryptography_data.types.re_encryption_attributes

        out["outgoing_encryption_attributes"] = (
            capo_payment_cryptography_data.types.re_encryption_attributes.redact_sensitive(
                value["outgoing_encryption_attributes"]
            )
        )
    if "incoming_wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["incoming_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.redact_sensitive(
                value["incoming_wrapped_key"]
            )
        )
    if "outgoing_wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["outgoing_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.redact_sensitive(
                value["outgoing_wrapped_key"]
            )
        )
    return out
