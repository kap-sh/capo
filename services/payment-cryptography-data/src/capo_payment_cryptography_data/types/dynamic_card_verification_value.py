"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DynamicCardVerificationValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.card_expiry_date_type
    import capo_payment_cryptography_data.types.hex_length_between2_and4
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.service_code_type


class DynamicCardVerificationValue(TypedDict, closed=True):
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).</p>"""
    card_expiry_date: (
        "capo_payment_cryptography_data.types.card_expiry_date_type.CardExpiryDateType"
    )
    """<p>The expiry date of a payment card.</p>"""
    service_code: (
        "capo_payment_cryptography_data.types.service_code_type.ServiceCodeType"
    )
    """<p>The service code of the payment card. This is different from Card Security Code (CSC).</p>"""
    application_transaction_counter: "capo_payment_cryptography_data.types.hex_length_between2_and4.HexLengthBetween2And4"
    """<p>The transaction counter value that comes from the terminal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamicCardVerificationValue) -> dict:
    out: dict = {}
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["CardExpiryDate"] = value["card_expiry_date"]
    out["ServiceCode"] = value["service_code"]
    out["ApplicationTransactionCounter"] = value["application_transaction_counter"]
    return out


def deserialize_json(data: dict) -> DynamicCardVerificationValue:
    out: DynamicCardVerificationValue = {}  # type: ignore[typeddict-item]
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        raise DeserializationError(
            "DynamicCardVerificationValue.pan_sequence_number required"
        )
    if data.get("CardExpiryDate") is not None:
        out["card_expiry_date"] = data["CardExpiryDate"]
    else:
        raise DeserializationError(
            "DynamicCardVerificationValue.card_expiry_date required"
        )
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError("DynamicCardVerificationValue.service_code required")
    if data.get("ApplicationTransactionCounter") is not None:
        out["application_transaction_counter"] = data["ApplicationTransactionCounter"]
    else:
        raise DeserializationError(
            "DynamicCardVerificationValue.application_transaction_counter required"
        )
    return out


def redact_sensitive(value: DynamicCardVerificationValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "card_expiry_date" in value:
        out["card_expiry_date"] = "*** Sensitive Data Redacted ***"
    if "service_code" in value:
        out["service_code"] = "*** Sensitive Data Redacted ***"
    return out
