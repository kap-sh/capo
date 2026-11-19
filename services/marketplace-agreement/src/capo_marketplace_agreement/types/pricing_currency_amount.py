"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PricingCurrencyAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.currency_code


class PricingCurrencyAmount(TypedDict, closed=True):
    amount: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>The monetary amount before tax.</p>"""
    max_adjustment_amount: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The maximum refundable amount as a string representation of a decimal number.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>The 3-letter ISO 4217 currency code (for example, <code>USD</code>, <code>EUR</code>, <code>JPY</code>).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PricingCurrencyAmount) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "max_adjustment_amount" in value:
        out["maxAdjustmentAmount"] = value["max_adjustment_amount"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PricingCurrencyAmount:
    out: PricingCurrencyAmount = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("maxAdjustmentAmount") is not None:
        out["max_adjustment_amount"] = data["maxAdjustmentAmount"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PricingCurrencyAmount) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "max_adjustment_amount" in value:
        out["maxAdjustmentAmount"] = value["max_adjustment_amount"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    return out


def deserialize_cbor(data: dict) -> PricingCurrencyAmount:
    out: PricingCurrencyAmount = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("maxAdjustmentAmount") is not None:
        out["max_adjustment_amount"] = data["maxAdjustmentAmount"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    return out
