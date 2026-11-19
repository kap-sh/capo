"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalLevels``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_level

BuyerAgreementApprovalLevels: TypeAlias = list[
    "capo_marketplace_agreement.types.buyer_agreement_approval_level.BuyerAgreementApprovalLevel"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalLevels) -> list:
    import capo_marketplace_agreement.types.buyer_agreement_approval_level

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_level.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BuyerAgreementApprovalLevels:
    import capo_marketplace_agreement.types.buyer_agreement_approval_level

    out: BuyerAgreementApprovalLevels = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.buyer_agreement_approval_level.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BuyerAgreementApprovalLevels) -> list[Any]:
    import capo_marketplace_agreement.types.buyer_agreement_approval_level

    return [
        capo_marketplace_agreement.types.buyer_agreement_approval_level.redact_sensitive(
            item
        )
        for item in value
    ]
