"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MasterCardAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.application_cryptogram_type
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type


class MasterCardAttributes(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: MasterCardAttributes) -> dict:
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
    return out


def deserialize_json(data: dict) -> MasterCardAttributes:
    out: MasterCardAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MajorKeyDerivationMode") is not None:
        import capo_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            capo_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        raise DeserializationError(
            "MasterCardAttributes.major_key_derivation_mode required"
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "MasterCardAttributes.primary_account_number required"
        )
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("MasterCardAttributes.pan_sequence_number required")
    if data.get("ApplicationCryptogram") is not None:
        out["application_cryptogram"] = data["ApplicationCryptogram"]
    else:
        raise DeserializationError(
            "MasterCardAttributes.application_cryptogram required"
        )
    return out


def redact_sensitive(value: MasterCardAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "application_cryptogram" in value:
        out["application_cryptogram"] = "*** Sensitive Data Redacted ***"
    return out
