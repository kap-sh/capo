"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CardVerificationValue1``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.card_expiry_date_type
    import capo_payment_cryptography_data.types.service_code_type


class CardVerificationValue1(TypedDict, closed=True):
    card_expiry_date: (
        "capo_payment_cryptography_data.types.card_expiry_date_type.CardExpiryDateType"
    )
    """<p>The expiry date of a payment card.</p>"""
    service_code: (
        "capo_payment_cryptography_data.types.service_code_type.ServiceCodeType"
    )
    """<p>The service code of the payment card. This is different from Card Security Code (CSC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CardVerificationValue1) -> dict:
    out: dict = {}
    out["CardExpiryDate"] = value["card_expiry_date"]
    out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> CardVerificationValue1:
    out: CardVerificationValue1 = {}  # type: ignore[typeddict-item]
    if data.get("CardExpiryDate") is not None:
        out["card_expiry_date"] = data["CardExpiryDate"]
    else:
        out["card_expiry_date"] = ""
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    else:
        out["service_code"] = ""
    return out


def redact_sensitive(value: CardVerificationValue1) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "card_expiry_date" in value:
        out["card_expiry_date"] = "*** Sensitive Data Redacted ***"
    if "service_code" in value:
        out["service_code"] = "*** Sensitive Data Redacted ***"
    return out
