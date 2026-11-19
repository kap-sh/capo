"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalApproverInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_id
    import capo_marketplace_agreement.types.agreement_approval_note
    import capo_marketplace_agreement.types.agreement_approval_purchase_orders
    import capo_marketplace_agreement.types.approver_outcome_id


class BuyerAgreementApprovalApproverInput(TypedDict, closed=True):
    agreement_approval_id: (
        "capo_marketplace_agreement.types.agreement_approval_id.AgreementApprovalId"
    )
    """<p>The unique identifier of the agreement approval to approve.</p>"""
    purchase_orders: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_purchase_orders.AgreementApprovalPurchaseOrders"
    ]
    """<p>An optional list of purchase order references to associate with charges on the agreement request.</p>"""
    note: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_note.AgreementApprovalNote"
    ]
    """<p>An optional note that explains the decision (1-1000 characters).</p>"""
    approver_outcome_id_to_override: NotRequired[
        "capo_marketplace_agreement.types.approver_outcome_id.ApproverOutcomeId"
    ]
    """<p>The <code>approverOutcomeId</code> of the approver to decide on behalf of. You must be the management account or a delegated administrator of your AWS organization to set this field. Use <code>GetAgreementApproval</code> to retrieve the <code>approverOutcomeId</code> of each approver.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalApproverInput) -> dict:
    out: dict = {}
    out["agreementApprovalId"] = value["agreement_approval_id"]
    if "purchase_orders" in value:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchaseOrders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.serialize_aws_json_1_0(
                value["purchase_orders"]
            )
        )
    if "note" in value:
        out["note"] = value["note"]
    if "approver_outcome_id_to_override" in value:
        out["approverOutcomeIdToOverride"] = value["approver_outcome_id_to_override"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalApproverInput:
    out: BuyerAgreementApprovalApproverInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    if data.get("purchaseOrders") is not None:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchase_orders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.deserialize_aws_json_1_0(
                data["purchaseOrders"]
            )
        )
    if data.get("note") is not None:
        out["note"] = data["note"]
    if data.get("approverOutcomeIdToOverride") is not None:
        out["approver_outcome_id_to_override"] = data["approverOutcomeIdToOverride"]
    return out


def redact_sensitive(value: BuyerAgreementApprovalApproverInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "note" in value:
        out["note"] = "*** Sensitive Data Redacted ***"
    return out
