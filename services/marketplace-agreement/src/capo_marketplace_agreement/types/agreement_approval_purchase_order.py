"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPurchaseOrder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.charge_id
    import capo_marketplace_agreement.types.purchase_order_reference


class AgreementApprovalPurchaseOrder(TypedDict, closed=True):
    charge_id: "capo_marketplace_agreement.types.charge_id.ChargeId"
    """<p>The unique identifier of the charge to associate the purchase order with. Use <code>GetAgreementRequest</code> to retrieve the charges of the agreement request.</p>"""
    purchase_order_reference: NotRequired[
        "capo_marketplace_agreement.types.purchase_order_reference.PurchaseOrderReference"
    ]
    """<p>The purchase order reference to associate with the charge.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPurchaseOrder) -> dict:
    out: dict = {}
    out["chargeId"] = value["charge_id"]
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalPurchaseOrder:
    out: AgreementApprovalPurchaseOrder = {}  # type: ignore[typeddict-item]
    if data.get("chargeId") is not None:
        out["charge_id"] = data["chargeId"]
    else:
        out["charge_id"] = ""
    if data.get("purchaseOrderReference") is not None:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalPurchaseOrder) -> dict:
    out: dict = {}
    out["chargeId"] = value["charge_id"]
    if "purchase_order_reference" in value:
        out["purchaseOrderReference"] = value["purchase_order_reference"]
    return out


def deserialize_cbor(data: dict) -> AgreementApprovalPurchaseOrder:
    out: AgreementApprovalPurchaseOrder = {}  # type: ignore[typeddict-item]
    if data.get("chargeId") is not None:
        out["charge_id"] = data["chargeId"]
    else:
        out["charge_id"] = ""
    if data.get("purchaseOrderReference") is not None:
        out["purchase_order_reference"] = data["purchaseOrderReference"]
    return out
