"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#AmexCardSecurityCodeVersion1``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.card_expiry_date_type


class AmexCardSecurityCodeVersion1(TypedDict, closed=True):
    card_expiry_date: (
        "capo_payment_cryptography_data.types.card_expiry_date_type.CardExpiryDateType"
    )
    """<p>The expiry date of a payment card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmexCardSecurityCodeVersion1) -> dict:
    out: dict = {}
    out["CardExpiryDate"] = value["card_expiry_date"]
    return out


def deserialize_json(data: dict) -> AmexCardSecurityCodeVersion1:
    out: AmexCardSecurityCodeVersion1 = {}  # type: ignore[typeddict-item]
    if data.get("CardExpiryDate") is not None:
        out["card_expiry_date"] = data["CardExpiryDate"]
    else:
        out["card_expiry_date"] = ""
    return out


def redact_sensitive(value: AmexCardSecurityCodeVersion1) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "card_expiry_date" in value:
        out["card_expiry_date"] = "*** Sensitive Data Redacted ***"
    return out
