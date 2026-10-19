"""Generated from Smithy shape ``com.amazonaws.billingconductor#BatchAssociateResourcesToCustomLineItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.custom_line_item_batch_associations_list
    import capo_billingconductor.types.custom_line_item_billing_period_range


class BatchAssociateResourcesToCustomLineItemInput(TypedDict, closed=True):
    target_arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> A percentage custom line item ARN to associate the resources to. </p>"""
    resource_arns: "capo_billingconductor.types.custom_line_item_batch_associations_list.CustomLineItemBatchAssociationsList"
    """<p> A list containing the ARNs of the resources to be associated. </p>"""
    billing_period_range: NotRequired[
        "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateResourcesToCustomLineItemInput) -> dict:
    out: dict = {}
    out["TargetArn"] = value["target_arn"]
    import capo_billingconductor.types.custom_line_item_batch_associations_list

    out["ResourceArns"] = (
        capo_billingconductor.types.custom_line_item_batch_associations_list.serialize_json(
            value["resource_arns"]
        )
    )
    if "billing_period_range" in value:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["BillingPeriodRange"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.serialize_json(
                value["billing_period_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateResourcesToCustomLineItemInput:
    out: BatchAssociateResourcesToCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    else:
        out["target_arn"] = ""
    if data.get("ResourceArns") is not None:
        import capo_billingconductor.types.custom_line_item_batch_associations_list

        out["resource_arns"] = (
            capo_billingconductor.types.custom_line_item_batch_associations_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        out["resource_arns"] = []
    if data.get("BillingPeriodRange") is not None:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out
