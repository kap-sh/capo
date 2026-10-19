"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.purchase_orders


class AcceptAgreementRequestInput(TypedDict, closed=True):
    agreement_request_id: (
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    )
    """<p>The unique identifier of the agreement request.</p>"""
    purchase_orders: NotRequired[
        "capo_marketplace_agreement.types.purchase_orders.PurchaseOrders"
    ]
    """<p>A list of purchase orders associated with accepting a marketplace agreement request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementRequestInput) -> dict:
    out: dict = {}
    out["agreementRequestId"] = value["agreement_request_id"]
    if "purchase_orders" in value:
        import capo_marketplace_agreement.types.purchase_orders

        out["purchaseOrders"] = (
            capo_marketplace_agreement.types.purchase_orders.serialize_aws_json_1_0(
                value["purchase_orders"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementRequestInput:
    out: AcceptAgreementRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
    if data.get("purchaseOrders") is not None:
        import capo_marketplace_agreement.types.purchase_orders

        out["purchase_orders"] = (
            capo_marketplace_agreement.types.purchase_orders.deserialize_aws_json_1_0(
                data["purchaseOrders"]
            )
        )
    return out
