"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GeneratePinDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.integer_range_between4_and12
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.pin_block_format_for_pin_data
    import capo_payment_cryptography_data.types.pin_generation_attributes
    import capo_payment_cryptography_data.types.primary_account_number_type
    import capo_payment_cryptography_data.types.wrapped_key


class GeneratePinDataInput(TypedDict, closed=True):
    generation_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses for pin data generation.</p>"""
    encryption_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the PEK that Amazon Web Services Payment Cryptography uses to encrypt the PIN Block. For ECDH, it is the <code>keyARN</code> of the asymmetric ECC key.</p>"""
    generation_attributes: "capo_payment_cryptography_data.types.pin_generation_attributes.PinGenerationAttributes"
    """<p>The attributes and values to use for PIN, PVV, or PIN Offset generation.</p>"""
    pin_data_length: NotRequired[
        "capo_payment_cryptography_data.types.integer_range_between4_and12.IntegerRangeBetween4And12"
    ]
    """<p>The length of PIN under generation.</p>"""
    primary_account_number: NotRequired[
        "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    ]
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>"""
    pin_block_format: "capo_payment_cryptography_data.types.pin_block_format_for_pin_data.PinBlockFormatForPinData"
    """<p>The PIN encoding format for pin data generation as specified in ISO 9564. Amazon Web Services Payment Cryptography supports <code>ISO_Format_0</code>, <code>ISO_Format_3</code> and <code>ISO_Format_4</code>.</p> <p>The <code>ISO_Format_0</code> PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.</p> <p>The <code>ISO_Format_3</code> PIN block format is the same as <code>ISO_Format_0</code> except that the fill digits are random values from 10 to 15.</p> <p>The <code>ISO_Format_4</code> PIN block format is the only one supporting AES encryption.</p>"""
    encryption_wrapped_key: NotRequired[
        "capo_payment_cryptography_data.types.wrapped_key.WrappedKey"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratePinDataInput) -> dict:
    out: dict = {}
    out["GenerationKeyIdentifier"] = value["generation_key_identifier"]
    out["EncryptionKeyIdentifier"] = value["encryption_key_identifier"]
    import capo_payment_cryptography_data.types.pin_generation_attributes

    out["GenerationAttributes"] = (
        capo_payment_cryptography_data.types.pin_generation_attributes.serialize_json(
            value["generation_attributes"]
        )
    )
    if "pin_data_length" in value:
        out["PinDataLength"] = value["pin_data_length"]
    if "primary_account_number" in value:
        out["PrimaryAccountNumber"] = value["primary_account_number"]
    import capo_payment_cryptography_data.types.pin_block_format_for_pin_data

    out["PinBlockFormat"] = (
        capo_payment_cryptography_data.types.pin_block_format_for_pin_data.serialize_json(
            value["pin_block_format"]
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


def deserialize_json(data: dict) -> GeneratePinDataInput:
    out: GeneratePinDataInput = {}  # type: ignore[typeddict-item]
    if data.get("GenerationKeyIdentifier") is not None:
        out["generation_key_identifier"] = data["GenerationKeyIdentifier"]
    else:
        out["generation_key_identifier"] = ""
    if data.get("EncryptionKeyIdentifier") is not None:
        out["encryption_key_identifier"] = data["EncryptionKeyIdentifier"]
    else:
        out["encryption_key_identifier"] = ""
    if data.get("GenerationAttributes") is not None:
        import capo_payment_cryptography_data.types.pin_generation_attributes

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types.pin_generation_attributes.deserialize_json(
                data["GenerationAttributes"]
            )
        )
    else:
        out["generation_attributes"] = {"$unknown": {"name": ""}}
    if data.get("PinDataLength") is not None:
        out["pin_data_length"] = data["PinDataLength"]
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
    if data.get("EncryptionWrappedKey") is not None:
        import capo_payment_cryptography_data.types.wrapped_key

        out["encryption_wrapped_key"] = (
            capo_payment_cryptography_data.types.wrapped_key.deserialize_json(
                data["EncryptionWrappedKey"]
            )
        )
    return out


def redact_sensitive(value: GeneratePinDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "generation_attributes" in value:
        import capo_payment_cryptography_data.types.pin_generation_attributes

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types.pin_generation_attributes.redact_sensitive(
                value["generation_attributes"]
            )
        )
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
