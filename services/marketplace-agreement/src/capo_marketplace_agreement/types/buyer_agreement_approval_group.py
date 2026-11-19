"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_criteria
    import capo_marketplace_agreement.types.buyer_approver_outcomes


class BuyerAgreementApprovalGroup(TypedDict, closed=True):
    approval_criteria: "capo_marketplace_agreement.types.buyer_agreement_approval_criteria.BuyerAgreementApprovalCriteria"
    """<p>The number of approvers in the group who must approve.</p>"""
    approvers: (
        "capo_marketplace_agreement.types.buyer_approver_outcomes.BuyerApproverOutcomes"
    )
    """<p>The approvers in the group and the decision of each one.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalGroup) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.buyer_agreement_approval_criteria

    out["approvalCriteria"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_criteria.serialize_aws_json_1_0(
            value["approval_criteria"]
        )
    )
    import capo_marketplace_agreement.types.buyer_approver_outcomes

    out["approvers"] = (
        capo_marketplace_agreement.types.buyer_approver_outcomes.serialize_aws_json_1_0(
            value["approvers"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalGroup:
    out: BuyerAgreementApprovalGroup = {}  # type: ignore[typeddict-item]
    if data.get("approvalCriteria") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_criteria

        out["approval_criteria"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_criteria.deserialize_aws_json_1_0(
                data["approvalCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "BuyerAgreementApprovalGroup.approval_criteria required"
        )
    if data.get("approvers") is not None:
        import capo_marketplace_agreement.types.buyer_approver_outcomes

        out["approvers"] = (
            capo_marketplace_agreement.types.buyer_approver_outcomes.deserialize_aws_json_1_0(
                data["approvers"]
            )
        )
    else:
        out["approvers"] = []
    return out


def redact_sensitive(value: BuyerAgreementApprovalGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "approvers" in value:
        import capo_marketplace_agreement.types.buyer_approver_outcomes

        out["approvers"] = (
            capo_marketplace_agreement.types.buyer_approver_outcomes.redact_sensitive(
                value["approvers"]
            )
        )
    return out
