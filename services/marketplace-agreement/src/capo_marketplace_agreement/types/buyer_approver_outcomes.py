"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerApproverOutcomes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.approver_outcome

BuyerApproverOutcomes: TypeAlias = list[
    "capo_marketplace_agreement.types.approver_outcome.ApproverOutcome"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerApproverOutcomes) -> list:
    import capo_marketplace_agreement.types.approver_outcome

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.approver_outcome.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BuyerApproverOutcomes:
    import capo_marketplace_agreement.types.approver_outcome

    out: BuyerApproverOutcomes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.approver_outcome.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BuyerApproverOutcomes) -> list[Any]:
    import capo_marketplace_agreement.types.approver_outcome

    return [
        capo_marketplace_agreement.types.approver_outcome.redact_sensitive(item)
        for item in value
    ]
