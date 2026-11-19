"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPurchaseOrders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_purchase_order

AgreementApprovalPurchaseOrders: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_approval_purchase_order.AgreementApprovalPurchaseOrder"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPurchaseOrders) -> list:
    import capo_marketplace_agreement.types.agreement_approval_purchase_order

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_purchase_order.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementApprovalPurchaseOrders:
    import capo_marketplace_agreement.types.agreement_approval_purchase_order

    out: AgreementApprovalPurchaseOrders = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_purchase_order.deserialize_aws_json_1_0(
                item
            )
        )
    return out
