"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslatePinDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.as2805_pek_derivation_attributes
    import capo_payment_cryptography_data.types.dukpt_derivation_attributes
    import capo_payment_cryptography_data.types.hex_even_length_between16_and32
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.translation_iso_formats
    import capo_payment_cryptography_data.types.wrapped_key


class TranslatePinDataInput(TypedDict, closed=True):
    incoming_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key under which incoming PIN block data is encrypted. This key type can be PEK or BDK.</p> <p>For dynamic keys, it is the <code>keyARN</code> of KEK of the TR-31 wrapped PEK. For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>"""
    outgoing_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key for encrypting outgoing PIN block data. This key type can be PEK or BDK.</p> <p>For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>"""
    incoming_translation_attributes: "capo_payment_cryptography_data.types.translation_iso_formats.TranslationIsoFormats"
    """<p>The format of the incoming PIN block data for translation within Amazon Web Services Payment Cryptography.</p>"""
    outgoing_translation_attributes: "capo_payment_cryptography_data.types.translation_iso_formats.TranslationIsoFormats"
    """<p>The format of the outgoing PIN block data after translation by Amazon Web Services Payment Cryptography.</p>"""
    encrypted_pin_block: "capo_payment_cryptography_data.types.hex_even_length_between16_and32.HexEvenLengthBetween16And32"
    """<p>The encrypted PIN block data that Amazon Web Services Payment Cryptography translates.</p>"""
    incoming_dukpt_attributes: NotRequired[
        "capo_payment_cryptography_data.types.dukpt_derivation_attributes.DukptDerivationAttributes"
    ]
    """<p>The attributes and values to use for incoming DUKPT encryption key for PIN block translation.</p>"""
    outgoing_dukpt_attributes: NotRequired[
        "capo_payment_cryptography_data.types.dukpt_derivation_attributes.DukptDerivationAttributes"
    ]
    """<p>The attributes and values to use for outgoing DUKPT encryption key after PIN block translation.</p>"""
    incoming_wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key under which incoming PIN block data is encrypted.</p>"""
    outgoing_wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]
    """<p>The WrappedKeyBlock containing the encryption key for encrypting outgoing PIN block data.</p>"""
    incoming_as2805_attributes: NotRequired[
        "capo_payment_cryptography_data.types.as2805_pek_derivation_attributes.As2805PekDerivationAttributes"
    ]
    """<p>The attributes and values to use for incoming AS2805 encryption key for PIN block translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranslatePinDataInput) -> dict:
    out: dict = {}
    out["IncomingKeyIdentifier"] = value["incoming_key_identifier"]
    out["OutgoingKeyIdentifier"] = value["outgoing_key_identifier"]
    import capo_payment_cryptography_data.types.translation_iso_formats

    out["IncomingTranslationAttributes"] = (
        capo_payment_cryptography_data.types.translation_iso_formats.serialize_json(
            value["incoming_translation_attributes"]
        )
    )
    import capo_payment_cryptography_data.types.translation_iso_formats

    out["OutgoingTranslationAttributes"] = (
        capo_payment_cryptography_data.types.translation_iso_formats.serialize_json(
            value["outgoing_translation_attributes"]
        )
    )
    out["EncryptedPinBlock"] = value["encrypted_pin_block"]
    if "incoming_dukpt_attributes" in value:
        import capo_payment_cryptography_data.types.dukpt_derivation_attributes

        out["IncomingDukptAttributes"] = (
            capo_payment_cryptography_data.types.dukpt_derivation_attributes.serialize_json(
                value["incoming_dukpt_attributes"]
            )
        )
    if "outgoing_dukpt_attributes" in value:
        import capo_payment_cryptography_data.types.dukpt_derivation_attributes

        out["OutgoingDukptAttributes"] = (
            capo_payment_cryptography_data.types.dukpt_derivation_attributes.serialize_json(
                value["outgoing_dukpt_attributes"]
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
    if "incoming_as2805_attributes" in value:
        import capo_payment_cryptography_data.types.as2805_pek_derivation_attributes

        out["IncomingAs2805Attributes"] = (
            capo_payment_cryptography_data.types.as2805_pek_derivation_attributes.serialize_json(
                value["incoming_as2805_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranslatePinDataInput:
    out: TranslatePinDataInput = {}  # type: ignore[typeddict-item]
    if data.get("IncomingKeyIdentifier") is not None:
        out["incoming_key_identifier"] = data["IncomingKeyIdentifier"]
    else:
        out["incoming_key_identifier"] = ""
    if data.get("OutgoingKeyIdentifier") is not None:
        out["outgoing_key_identifier"] = data["OutgoingKeyIdentifier"]
    else:
        out["outgoing_key_identifier"] = ""
    if data.get("IncomingTranslationAttributes") is not None:
        import capo_payment_cryptography_data.types.translation_iso_formats

        out["incoming_translation_attributes"] = (
            capo_payment_cryptography_data.types.translation_iso_formats.deserialize_json(
                data["IncomingTranslationAttributes"]
            )
        )
    else:
        out["incoming_translation_attributes"] = {"$unknown": {"name": ""}}
    if data.get("OutgoingTranslationAttributes") is not None:
        import capo_payment_cryptography_data.types.translation_iso_formats

        out["outgoing_translation_attributes"] = (
            capo_payment_cryptography_data.types.translation_iso_formats.deserialize_json(
                data["OutgoingTranslationAttributes"]
            )
        )
    else:
        out["outgoing_translation_attributes"] = {"$unknown": {"name": ""}}
    if data.get("EncryptedPinBlock") is not None:
        out["encrypted_pin_block"] = data["EncryptedPinBlock"]
    else:
        out["encrypted_pin_block"] = ""
    if data.get("IncomingDukptAttributes") is not None:
        import capo_payment_cryptography_data.types.dukpt_derivation_attributes

        out["incoming_dukpt_attributes"] = (
            capo_payment_cryptography_data.types.dukpt_derivation_attributes.deserialize_json(
                data["IncomingDukptAttributes"]
            )
        )
    if data.get("OutgoingDukptAttributes") is not None:
        import capo_payment_cryptography_data.types.dukpt_derivation_attributes

        out["outgoing_dukpt_attributes"] = (
            capo_payment_cryptography_data.types.dukpt_derivation_attributes.deserialize_json(
                data["OutgoingDukptAttributes"]
            )
        )
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
    if data.get("IncomingAs2805Attributes") is not None:
        import capo_payment_cryptography_data.types.as2805_pek_derivation_attributes

        out["incoming_as2805_attributes"] = (
            capo_payment_cryptography_data.types.as2805_pek_derivation_attributes.deserialize_json(
                data["IncomingAs2805Attributes"]
            )
        )
    return out


def redact_sensitive(value: TranslatePinDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "incoming_translation_attributes" in value:
        import capo_payment_cryptography_data.types.translation_iso_formats

        out["incoming_translation_attributes"] = (
            capo_payment_cryptography_data.types.translation_iso_formats.redact_sensitive(
                value["incoming_translation_attributes"]
            )
        )
    if "outgoing_translation_attributes" in value:
        import capo_payment_cryptography_data.types.translation_iso_formats

        out["outgoing_translation_attributes"] = (
            capo_payment_cryptography_data.types.translation_iso_formats.redact_sensitive(
                value["outgoing_translation_attributes"]
            )
        )
    if "encrypted_pin_block" in value:
        out["encrypted_pin_block"] = "*** Sensitive Data Redacted ***"
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
