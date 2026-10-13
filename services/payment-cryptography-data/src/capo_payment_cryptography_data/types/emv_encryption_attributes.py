"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EmvEncryptionAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.emv_encryption_mode
    import capo_payment_cryptography_data.types.emv_major_key_derivation_mode
    import capo_payment_cryptography_data.types.initialization_vector_type
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type
    import capo_payment_cryptography_data.types.session_derivation_data_type


class EmvEncryptionAttributes(TypedDict, closed=True):
    major_key_derivation_mode: "capo_payment_cryptography_data.types.emv_major_key_derivation_mode.EmvMajorKeyDerivationMode"
    """<p>The EMV derivation mode to use for ICC master key derivation as per EMV version 4.3 book 2.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    session_derivation_data: "capo_payment_cryptography_data.types.session_derivation_data_type.SessionDerivationDataType"
    """<p>The derivation value used to derive the ICC session key. It is typically the application transaction counter value padded with zeros or previous ARQC value padded with zeros as per EMV version 4.3 book 2.</p>"""
    mode: NotRequired[
        "capo_payment_cryptography_data.types.emv_encryption_mode.EmvEncryptionMode"
    ]
    """<p>The block cipher method to use for encryption.</p>"""
    initialization_vector: NotRequired[
        "capo_payment_cryptography_data.types.initialization_vector_type.InitializationVectorType"
    ]
    """<p>An input used to provide the intial state. If no value is provided, Amazon Web Services Payment Cryptography defaults it to zero.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmvEncryptionAttributes) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.emv_major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.emv_major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["SessionDerivationData"] = value["session_derivation_data"]
    if "mode" in value:
        import capo_payment_cryptography_data.types.emv_encryption_mode

        out["Mode"] = (
            capo_payment_cryptography_data.types.emv_encryption_mode.serialize_json(
                value["mode"]
            )
        )
    if "initialization_vector" in value:
        out["InitializationVector"] = value["initialization_vector"]
    return out


def deserialize_json(data: dict) -> EmvEncryptionAttributes:
    out: EmvEncryptionAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MajorKeyDerivationMode") is not None:
        import capo_payment_cryptography_data.types.emv_major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            capo_payment_cryptography_data.types.emv_major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "EmvEncryptionAttributes.major_key_derivation_mode required"
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "EmvEncryptionAttributes.primary_account_number required"
        )
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError(
            "EmvEncryptionAttributes.pan_sequence_number required"
        )
    if data.get("SessionDerivationData") is not None:
        out["session_derivation_data"] = data["SessionDerivationData"]
    else:
        raise DeserializationError(
            "EmvEncryptionAttributes.session_derivation_data required"
        )
    if data.get("Mode") is not None:
        import capo_payment_cryptography_data.types.emv_encryption_mode

        out["mode"] = (
            capo_payment_cryptography_data.types.emv_encryption_mode.deserialize_json(
                data["Mode"]
            )
        )
    if data.get("InitializationVector") is not None:
        out["initialization_vector"] = data["InitializationVector"]
    return out


def redact_sensitive(value: EmvEncryptionAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "session_derivation_data" in value:
        out["session_derivation_data"] = "*** Sensitive Data Redacted ***"
    if "initialization_vector" in value:
        out["initialization_vector"] = "*** Sensitive Data Redacted ***"
    return out
