"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#StartAgreementApprovalsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_plan_inputs
    import capo_marketplace_agreement.types.agreement_approval_purchase_orders
    import capo_marketplace_agreement.types.agreement_request_id


class StartAgreementApprovalsInput(TypedDict, closed=True):
    agreement_request_id: (
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    )
    """<p>The unique identifier of the agreement request to start approvals for.</p>"""
    plan_inputs: "capo_marketplace_agreement.types.agreement_approval_plan_inputs.AgreementApprovalPlanInputs"
    """<p>The approval plans to start agreement approvals for.</p>"""
    purchase_orders: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_purchase_orders.AgreementApprovalPurchaseOrders"
    ]
    """<p>An optional list of purchase order references to associate with charges on the agreement request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAgreementApprovalsInput) -> dict:
    out: dict = {}
    out["agreementRequestId"] = value["agreement_request_id"]
    import capo_marketplace_agreement.types.agreement_approval_plan_inputs

    out["planInputs"] = (
        capo_marketplace_agreement.types.agreement_approval_plan_inputs.serialize_aws_json_1_0(
            value["plan_inputs"]
        )
    )
    if "purchase_orders" in value:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchaseOrders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.serialize_aws_json_1_0(
                value["purchase_orders"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAgreementApprovalsInput:
    out: StartAgreementApprovalsInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
    if data.get("planInputs") is not None:
        import capo_marketplace_agreement.types.agreement_approval_plan_inputs

        out["plan_inputs"] = (
            capo_marketplace_agreement.types.agreement_approval_plan_inputs.deserialize_aws_json_1_0(
                data["planInputs"]
            )
        )
    else:
        out["plan_inputs"] = []
    if data.get("purchaseOrders") is not None:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchase_orders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.deserialize_aws_json_1_0(
                data["purchaseOrders"]
            )
        )
    return out


def redact_sensitive(value: StartAgreementApprovalsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "plan_inputs" in value:
        import capo_marketplace_agreement.types.agreement_approval_plan_inputs

        out["plan_inputs"] = (
            capo_marketplace_agreement.types.agreement_approval_plan_inputs.redact_sensitive(
                value["plan_inputs"]
            )
        )
    return out
