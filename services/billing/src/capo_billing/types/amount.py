"""Generated from Smithy shape ``com.amazonaws.billing#Amount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.currency_amount
    import capo_billing.types.currency_code


class Amount(TypedDict, closed=True):
    currency_code: "capo_billing.types.currency_code.CurrencyCode"
    """<p>The ISO 4217 currency code for the amount (for example, <code>USD</code>).</p>"""
    currency_amount: "capo_billing.types.currency_amount.CurrencyAmount"
    """<p>The amount as a decimal string (for example, <code>"743.21"</code>). Negative values represent credits that reduce a bill.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Amount) -> dict:
    out: dict = {}
    out["currencyCode"] = value["currency_code"]
    out["currencyAmount"] = value["currency_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Amount:
    out: Amount = {}  # type: ignore[typeddict-item]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    else:
        out["currency_code"] = ""
    if data.get("currencyAmount") is not None:
        out["currency_amount"] = data["currencyAmount"]
    else:
        out["currency_amount"] = ""
    return out
