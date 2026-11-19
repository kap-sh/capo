"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalGroups``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_group

BuyerAgreementApprovalGroups: TypeAlias = list[
    "capo_marketplace_agreement.types.buyer_agreement_approval_group.BuyerAgreementApprovalGroup"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalGroups) -> list:
    import capo_marketplace_agreement.types.buyer_agreement_approval_group

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_group.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BuyerAgreementApprovalGroups:
    import capo_marketplace_agreement.types.buyer_agreement_approval_group

    out: BuyerAgreementApprovalGroups = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_group.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BuyerAgreementApprovalGroups) -> list[Any]:
    import capo_marketplace_agreement.types.buyer_agreement_approval_group

    return [
        capo_marketplace_agreement.types.buyer_agreement_approval_group.redact_sensitive(
            item
        )
        for item in value
    ]
