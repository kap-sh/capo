"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalPlan``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_plan_name
    import capo_marketplace_agreement.types.agreement_approval_plan_reference
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels


class BuyerAgreementApprovalPlan(TypedDict, closed=True):
    plan_reference: "capo_marketplace_agreement.types.agreement_approval_plan_reference.AgreementApprovalPlanReference"
    """<p>The identifier of the approval plan. Pass it in <code>StartAgreementApprovals</code> to start an agreement approval for this plan.</p>"""
    name: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_plan_name.AgreementApprovalPlanName"
    ]
    """<p>The name of the approval plan.</p>"""
    levels: "capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels.BuyerAgreementApprovalPlanLevels"
    """<p>The approval levels of the plan, in the order they are evaluated. Approvers at a level can act only after the previous level is approved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalPlan) -> dict:
    out: dict = {}
    out["planReference"] = value["plan_reference"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels

    out["levels"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels.serialize_aws_json_1_0(
            value["levels"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalPlan:
    out: BuyerAgreementApprovalPlan = {}  # type: ignore[typeddict-item]
    if data.get("planReference") is not None:
        out["plan_reference"] = data["planReference"]
    else:
        out["plan_reference"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("levels") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels

        out["levels"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels.deserialize_aws_json_1_0(
                data["levels"]
            )
        )
    else:
        out["levels"] = []
    return out


def redact_sensitive(value: BuyerAgreementApprovalPlan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "levels" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels

        out["levels"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_levels.redact_sensitive(
                value["levels"]
            )
        )
    return out
