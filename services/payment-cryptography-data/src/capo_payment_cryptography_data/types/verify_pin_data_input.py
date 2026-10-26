"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyPinDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.dukpt_attributes
    import capo_payment_cryptography_data.types.encrypted_pin_block_type
    import capo_payment_cryptography_data.types.integer_range_between4_and12
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.pin_block_format_for_pin_data
    import capo_payment_cryptography_data.types.pin_verification_attributes
    import capo_payment_cryptography_data.types.primary_account_number_type
    import capo_payment_cryptography_data.types.wrapped_key


class VerifyPinDataInput(TypedDict, closed=True):
    verification_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the PIN verification key.</p>"""
    encryption_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key under which the PIN block data is encrypted. This key type can be PEK or BDK.</p>"""
    verification_attributes: "capo_payment_cryptography_data.types.pin_verification_attributes.PinVerificationAttributes"
    """<p>The attributes and values for PIN data verification.</p>"""
    encrypted_pin_block: "capo_payment_cryptography_data.types.encrypted_pin_block_type.EncryptedPinBlockType"
    """<p>The encrypted PIN block data that Amazon Web Services Payment Cryptography verifies.</p>"""
    primary_account_number: NotRequired[
        "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    ]
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>"""
    pin_block_format: "capo_payment_cryptography_data.types.pin_block_format_for_pin_data.PinBlockFormatForPinData"
    """<p>The PIN encoding format for pin data generation as specified in ISO 9564. Amazon Web Services Payment Cryptography supports <code>ISO_Format_0</code> and <code>ISO_Format_3</code>.</p> <p>The <code>ISO_Format_0</code> PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.</p> <p>The <code>ISO_Format_3</code> PIN block format is the same as <code>ISO_Format_0</code> except that the fill digits are random values from 10 to 15.</p>"""
    pin_data_length: NotRequired[
        "capo_payment_cryptography_data.types.integer_range_between4_and12.IntegerRangeBetween4And12"
    ]
    """<p>The length of PIN being verified.</p>"""
    dukpt_attributes: NotRequired[
        "capo_payment_cryptography_data.types.dukpt_attributes.DukptAttributes"
    ]
    """<p>The attributes and values for the DUKPT encrypted PIN block data.</p>"""
    encryption_wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VerifyPinDataInput) -> dict:
    out: dict = {}
    out["VerificationKeyIdentifier"] = value["verification_key_identifier"]
    out["EncryptionKeyIdentifier"] = value["encryption_key_identifier"]
    import capo_payment_cryptography_data.types.pin_verification_attributes

    out["VerificationAttributes"] = (
        capo_payment_cryptography_data.types.pin_verification_attributes.serialize_json(
            value["verification_attributes"]
        )
    )
    out["EncryptedPinBlock"] = value["encrypted_pin_block"]
    if "primary_account_number" in value:
        out["PrimaryAccountNumber"] = value["primary_account_number"]
    import capo_payment_cryptography_data.types.pin_block_format_for_pin_data

    out["PinBlockFormat"] = (
        capo_payment_cryptography_data.types.pin_block_format_for_pin_data.serialize_json(
            value["pin_block_format"]
        )
    )
    if "pin_data_length" in value:
        out["PinDataLength"] = value["pin_data_length"]
    if "dukpt_attributes" in value:
        import capo_payment_cryptography_data.types.dukpt_attributes

        out["DukptAttributes"] = (
            capo_payment_cryptography_data.types.dukpt_attributes.serialize_json(
                value["dukpt_attributes"]
            )
        )
    if "encryption_wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["EncryptionWrappedKey"] = (
            capo_payment_cryptography_data.types.wrapped_key.serialize_json(
                value["encryption_wrapped_key"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyPinDataInput:
    out: VerifyPinDataInput = {}  # type: ignore[typeddict-item]
    if data.get("VerificationKeyIdentifier") is not None:
        out["verification_key_identifier"] = data["VerificationKeyIdentifier"]
    else:
        out["verification_key_identifier"] = ""
    if data.get("EncryptionKeyIdentifier") is not None:
        out["encryption_key_identifier"] = data["EncryptionKeyIdentifier"]
    else:
        out["encryption_key_identifier"] = ""
    if data.get("VerificationAttributes") is not None:
        import capo_payment_cryptography_data.types.pin_verification_attributes

        out["verification_attributes"] = (
            capo_payment_cryptography_data.types.pin_verification_attributes.deserialize_json(
                data["VerificationAttributes"]
            )
        )
    else:
        out["verification_attributes"] = {"$unknown": {"name": ""}}
    if data.get("EncryptedPinBlock") is not None:
        out["encrypted_pin_block"] = data["EncryptedPinBlock"]
    else:
        out["encrypted_pin_block"] = ""
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    if data.get("PinBlockFormat") is not None:
        import capo_payment_cryptography_data.types.pin_block_format_for_pin_data

        out["pin_block_format"] = (
            capo_payment_cryptography_data.types.pin_block_format_for_pin_data.deserialize_json(
                data["PinBlockFormat"]
            )
        )
    else:
        import typing

        out["pin_block_format"] = typing.cast(
            "capo_payment_cryptography_data.types.pin_block_format_for_pin_data.PinBlockFormatForPinData",
            "",
        )
    if data.get("PinDataLength") is not None:
        out["pin_data_length"] = data["PinDataLength"]
    if data.get("DukptAttributes") is not None:
        import capo_payment_cryptography_data.types.dukpt_attributes

        out["dukpt_attributes"] = (
            capo_payment_cryptography_data.types.dukpt_attributes.deserialize_json(
                data["DukptAttributes"]
            )
        )
    if data.get("EncryptionWrappedKey") is not None:
        import capo_payment_cryptography_data.types.wrapped_key

        out["encryption_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["EncryptionWrappedKey"]
            )
        )
    return out


def redact_sensitive(value: VerifyPinDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "verification_attributes" in value:
        import capo_payment_cryptography_data.types.pin_verification_attributes

        out["verification_attributes"] = (
            capo_payment_cryptography_data.types.pin_verification_attributes.redact_sensitive(
                value["verification_attributes"]
            )
        )
    if "encrypted_pin_block" in value:
        out["encrypted_pin_block"] = "*** Sensitive Data Redacted ***"
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "encryption_wrapped_key" in value:
        import capo_payment_cryptography_data.types.wrapped_key

        out["encryption_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.redact_sensitive(
                value["encryption_wrapped_key"]
            )
        )
    return out
