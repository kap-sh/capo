"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#MonetaryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.amount
    import capo_partnercentral_marketing.types.currency_code


class MonetaryValue(TypedDict, closed=True):
    amount: "capo_partnercentral_marketing.types.amount.Amount"
    """The amount, as a decimal string with at most two decimal places."""
    currency_code: "capo_partnercentral_marketing.types.currency_code.CurrencyCode"
    """The ISO 4217 currency the amount is denominated in."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MonetaryValue) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    out["CurrencyCode"] = value["currency_code"]
    return out


def deserialize_cbor(data: dict) -> MonetaryValue:
    out: MonetaryValue = {}  # type: ignore[typeddict-item]
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("CurrencyCode") is not None:
        out["currency_code"] = data["CurrencyCode"]
    else:
        out["currency_code"] = ""
    return out
