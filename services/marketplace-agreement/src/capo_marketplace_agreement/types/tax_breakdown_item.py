"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TaxBreakdownItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string


class TaxBreakdownItem(TypedDict, closed=True):
    amount: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>The estimated tax amount.</p>"""
    rate: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>The tax rate, in decimals.</p>"""
    type: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>The type of tax (for example, VAT, ST, or GST).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxBreakdownItem) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "rate" in value:
        out["rate"] = value["rate"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaxBreakdownItem:
    out: TaxBreakdownItem = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("rate") is not None:
        out["rate"] = data["rate"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaxBreakdownItem) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "rate" in value:
        out["rate"] = value["rate"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_cbor(data: dict) -> TaxBreakdownItem:
    out: TaxBreakdownItem = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("rate") is not None:
        out["rate"] = data["rate"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
