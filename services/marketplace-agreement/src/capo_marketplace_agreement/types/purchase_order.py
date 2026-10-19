"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PurchaseOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.charge_revision
    import capo_marketplace_agreement.types.purchase_order_reference
    import capo_marketplace_agreement.types.resource_id


class PurchaseOrder(TypedDict, closed=True):
    charge_id: "capo_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the charge to associate the purchase order with.</p>"""
    charge_revision: NotRequired[
        "capo_marketplace_agreement.types.charge_revision.ChargeRevision"
    ]
    """<p>The revision of the charge.</p>"""
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement associated with this charge.</p>"""
    purchase_order_reference: NotRequired[
        "capo_marketplace_agreement.types.purchase_order_reference.PurchaseOrderReference"
    ]
    """<p>The purchase order reference to associate with the charge.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseOrder) -> dict:
    out: dict = {}
    out["chargeId"] = value["charge_id"]
    if "charge_revision" in value:
        out["chargeRevision"] = value["charge_revision"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PurchaseOrder:
    out: PurchaseOrder = {}  # type: ignore[typeddict-item]
    if data.get("chargeId") is not None:
        out["charge_id"] = data["chargeId"]
    else:
        out["charge_id"] = ""
    if data.get("chargeRevision") is not None:
        out["charge_revision"] = data["chargeRevision"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("purchaseOrderReference") is not None:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    return out
