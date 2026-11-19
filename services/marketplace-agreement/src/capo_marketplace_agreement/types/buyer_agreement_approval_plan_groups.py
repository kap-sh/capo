"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalPlanGroups``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_group

BuyerAgreementApprovalPlanGroups: TypeAlias = list[
    "capo_marketplace_agreement.types.buyer_agreement_approval_plan_group.BuyerAgreementApprovalPlanGroup"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalPlanGroups) -> list:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_group

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_group.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BuyerAgreementApprovalPlanGroups:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_group

    out: BuyerAgreementApprovalPlanGroups = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_group.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuyerAgreementApprovalPlanGroups) -> list:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_group

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_group.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> BuyerAgreementApprovalPlanGroups:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_group

    out: BuyerAgreementApprovalPlanGroups = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_group.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: BuyerAgreementApprovalPlanGroups) -> list[Any]:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_group

    return [
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_group.redact_sensitive(
            item
        )
        for item in value
    ]
