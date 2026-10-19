"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvCommonAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.application_cryptogram_type
    import capo_payment_cryptography_data.types.emv_encryption_mode
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.pin_block_length_position
    import capo_payment_cryptography_data.types.pin_block_padding_type
    import capo_payment_cryptography_data.types.primary_account_number_type


class EmvCommonAttributes(TypedDict, closed=True):
    major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for the payment card.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    application_cryptogram: "capo_payment_cryptography_data.types.application_cryptogram_type.ApplicationCryptogramType"
    """<p>The application cryptogram for the current transaction that is provided by the terminal during transaction processing.</p>"""
    mode: "capo_payment_cryptography_data.types.emv_encryption_mode.EmvEncryptionMode"
    """<p>The block cipher method to use for encryption.</p>"""
    pin_block_padding_type: "capo_payment_cryptography_data.types.pin_block_padding_type.PinBlockPaddingType"
    """<p>The padding to be added to the PIN block prior to encryption.</p> <p>Padding type should be <code>ISO_IEC_7816_4</code>, if <code>PinBlockLengthPosition</code> is set to <code>FRONT_OF_PIN_BLOCK</code>. No padding is required, if <code>PinBlockLengthPosition</code> is set to <code>NONE</code>.</p>"""
    pin_block_length_position: "capo_payment_cryptography_data.types.pin_block_length_position.PinBlockLengthPosition"
    """<p>Specifies if PIN block length should be added to front of the pin block. </p> <p>If value is set to <code>FRONT_OF_PIN_BLOCK</code>, then PIN block padding type should be <code>ISO_IEC_7816_4</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmvCommonAttributes) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationCryptogram"] = value["application_cryptogram"]
    import capo_payment_cryptography_data.types.emv_encryption_mode

    out["Mode"] = (
        capo_payment_cryptography_data.types.emv_encryption_mode.serialize_json(
            value["mode"]
        )
    )
    import capo_payment_cryptography_data.types.pin_block_padding_type

    out["PinBlockPaddingType"] = (
        capo_payment_cryptography_data.types.pin_block_padding_type.serialize_json(
            value["pin_block_padding_type"]
        )
    )
    import capo_payment_cryptography_data.types.pin_block_length_position

    out["PinBlockLengthPosition"] = (
        capo_payment_cryptography_data.types.pin_block_length_position.serialize_json(
            value["pin_block_length_position"]
        )
    )
    return out


def deserialize_json(data: dict) -> EmvCommonAttributes:
    out: EmvCommonAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MajorKeyDerivationMode") is not None:
        import capo_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            capo_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        import typing

        out["major_key_derivation_mode"] = typing.cast(
            "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode",
            "",
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        out["primary_account_number"] = ""
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        out["pan_sequence_number"] = ""
    if data.get("ApplicationCryptogram") is not None:
        out["application_cryptogram"] = data["ApplicationCryptogram"]
    else:
        out["application_cryptogram"] = ""
    if data.get("Mode") is not None:
        import capo_payment_cryptography_data.types.emv_encryption_mode

        out["mode"] = (
            capo_payment_cryptography_data.types.emv_encryption_mode.deserialize_json(
                data["Mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_payment_cryptography_data.types.emv_encryption_mode.EmvEncryptionMode",
            "",
        )
    if data.get("PinBlockPaddingType") is not None:
        import capo_payment_cryptography_data.types.pin_block_padding_type

        out["pin_block_padding_type"] = (
            capo_payment_cryptography_data.types.pin_block_padding_type.deserialize_json(
                data["PinBlockPaddingType"]
            )
        )
    else:
        import typing

        out["pin_block_padding_type"] = typing.cast(
            "capo_payment_cryptography_data.types.pin_block_padding_type.PinBlockPaddingType",
            "",
        )
    if data.get("PinBlockLengthPosition") is not None:
        import capo_payment_cryptography_data.types.pin_block_length_position

        out["pin_block_length_position"] = (
            capo_payment_cryptography_data.types.pin_block_length_position.deserialize_json(
                data["PinBlockLengthPosition"]
            )
        )
    else:
        import typing

        out["pin_block_length_position"] = typing.cast(
            "capo_payment_cryptography_data.types.pin_block_length_position.PinBlockLengthPosition",
            "",
        )
    return out


def redact_sensitive(value: EmvCommonAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "application_cryptogram" in value:
        out["application_cryptogram"] = "*** Sensitive Data Redacted ***"
    return out
