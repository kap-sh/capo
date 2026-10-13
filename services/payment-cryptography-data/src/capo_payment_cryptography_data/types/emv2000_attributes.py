"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#Emv2000Attributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.hex_length_equals4
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type


class Emv2000Attributes(TypedDict, closed=True):
    major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for the payment card.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    application_transaction_counter: (
        "capo_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )
    """<p>The transaction counter of the current transaction that is provided by the terminal during transaction processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Emv2000Attributes) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationTransactionCounter"] = value["application_transaction_counter"]
    return out


def deserialize_json(data: dict) -> Emv2000Attributes:
    out: Emv2000Attributes = {}  # type: ignore[typeddict-item]
    if data.get("MajorKeyDerivationMode") is not None:
        import capo_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            capo_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "Emv2000Attributes.major_key_derivation_mode required"
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError("Emv2000Attributes.primary_account_number required")
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("Emv2000Attributes.pan_sequence_number required")
    if data.get("ApplicationTransactionCounter") is not None:
        out["application_transaction_counter"] = data["ApplicationTransactionCounter"]
    else:
        raise DeserializationError(
            "Emv2000Attributes.application_transaction_counter required"
        )
    return out


def redact_sensitive(value: Emv2000Attributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    return out
