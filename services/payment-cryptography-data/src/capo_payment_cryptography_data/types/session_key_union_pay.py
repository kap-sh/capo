"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyUnionPay``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.hex_length_equals4
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type


class SessionKeyUnionPay(TypedDict, closed=True):
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). If not used, enter <code>00</code>.</p>"""
    application_transaction_counter: (
        "capo_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )
    """<p>The transaction counter that the terminal provides during transaction processing. This value is in hexadecimal format. For example, enter a decimal counter of 109 as <code>006D</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyUnionPay) -> dict:
    out: dict = {}
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationTransactionCounter"] = value["application_transaction_counter"]
    return out


def deserialize_json(data: dict) -> SessionKeyUnionPay:
    out: SessionKeyUnionPay = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError("SessionKeyUnionPay.primary_account_number required")
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError("SessionKeyUnionPay.pan_sequence_number required")
    if data.get("ApplicationTransactionCounter") is not None:
        out["application_transaction_counter"] = data["ApplicationTransactionCounter"]
    else:
        raise DeserializationError(
            "SessionKeyUnionPay.application_transaction_counter required"
        )
    return out


def redact_sensitive(value: SessionKeyUnionPay) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    return out
