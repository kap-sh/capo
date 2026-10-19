"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyEmv2000``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.hex_length_equals4
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type


class SessionKeyEmv2000(TypedDict, closed=True):
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).</p>"""
    application_transaction_counter: (
        "capo_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )
    """<p>The transaction counter that is provided by the terminal during transaction processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyEmv2000) -> dict:
    out: dict = {}
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationTransactionCounter"] = value["application_transaction_counter"]
    return out


def deserialize_json(data: dict) -> SessionKeyEmv2000:
    out: SessionKeyEmv2000 = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        out["primary_account_number"] = ""
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        out["pan_sequence_number"] = ""
    if data.get("ApplicationTransactionCounter") is not None:
        out["application_transaction_counter"] = data["ApplicationTransactionCounter"]
    else:
        out["application_transaction_counter"] = ""
    return out


def redact_sensitive(value: SessionKeyEmv2000) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    return out
