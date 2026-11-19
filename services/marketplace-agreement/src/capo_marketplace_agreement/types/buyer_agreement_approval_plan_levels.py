"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalPlanLevels``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_level

BuyerAgreementApprovalPlanLevels: TypeAlias = list[
    "capo_marketplace_agreement.types.buyer_agreement_approval_plan_level.BuyerAgreementApprovalPlanLevel"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalPlanLevels) -> list:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_level

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_level.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BuyerAgreementApprovalPlanLevels:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_level

    out: BuyerAgreementApprovalPlanLevels = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_level.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BuyerAgreementApprovalPlanLevels) -> list[Any]:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_level

    return [
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_level.redact_sensitive(
            item
        )
        for item in value
    ]
