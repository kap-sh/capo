"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ExpectedCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.estimated_taxes
    import capo_marketplace_agreement.types.purchase_order_reference
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.timestamp
    import capo_marketplace_agreement.types.timing


class ExpectedCharge(TypedDict, closed=True):
    id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>Unique identifier of the charge for a given agreement.</p>"""
    time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the charge is due to be invoiced. This is available only when the charge date is known.</p>"""
    amount: NotRequired["capo_marketplace_agreement.types.bounded_string.BoundedString"]
    """<p>The tax-exclusive amount of the charge. Only available when the charge amount is known.</p>"""
    amount_after_tax: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The tax-inclusive amount the acceptor has to pay. The amount is only present for fixed charges.</p>"""
    timing: NotRequired["capo_marketplace_agreement.types.timing.Timing"]
    """<p>Indicates when the charge amount will be incurred. Values include <code>ON_ACCEPTANCE</code> (charged immediately when the agreement request is accepted), <code>BILLING_PERIOD</code> (charged on each billing period), and <code>SCHEDULED</code> (charged at a predetermined future date).</p>"""
    estimated_taxes: NotRequired[
        "capo_marketplace_agreement.types.estimated_taxes.EstimatedTaxes"
    ]
    """<p>Provides an aggregated view of estimated tax information for this specific charge.</p>"""
    purchase_order_reference: NotRequired[
        "capo_marketplace_agreement.types.purchase_order_reference.PurchaseOrderReference"
    ]
    """<p>The purchase order reference associated with the charge, if any.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedCharge) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["time"] = capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["time"]
        )
    if "amount" in value:
        out["amount"] = value["amount"]
    if "amount_after_tax" in value:
        out["amountAfterTax"] = value["amount_after_tax"]
    if "timing" in value:
        import capo_marketplace_agreement.types.timing

        out["timing"] = capo_marketplace_agreement.types.timing.serialize_aws_json_1_0(
            value["timing"]
        )
    if "estimated_taxes" in value:
        import capo_marketplace_agreement.types.estimated_taxes

        out["estimatedTaxes"] = (
            capo_marketplace_agreement.types.estimated_taxes.serialize_aws_json_1_0(
                value["estimated_taxes"]
            )
        )
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpectedCharge:
    out: ExpectedCharge = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("time") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["time"]
            )
        )
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    if data.get("amountAfterTax") is not None:
        out["amount_after_tax"] = data["amountAfterTax"]
    if data.get("timing") is not None:
        import capo_marketplace_agreement.types.timing

        out["timing"] = (
            capo_marketplace_agreement.types.timing.deserialize_aws_json_1_0(
                data["timing"]
            )
        )
    if data.get("estimatedTaxes") is not None:
        import capo_marketplace_agreement.types.estimated_taxes

        out["estimated_taxes"] = (
            capo_marketplace_agreement.types.estimated_taxes.deserialize_aws_json_1_0(
                data["estimatedTaxes"]
            )
        )
    if data.get("purchaseOrderReference") is not None:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    return out
