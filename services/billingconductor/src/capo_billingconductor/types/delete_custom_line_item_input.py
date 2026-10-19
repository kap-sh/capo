"""Generated from Smithy shape ``com.amazonaws.billingconductor#DeleteCustomLineItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.custom_line_item_billing_period_range


class DeleteCustomLineItemInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> The ARN of the custom line item to be deleted. </p>"""
    billing_period_range: NotRequired[
        "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomLineItemInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "billing_period_range" in value:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["BillingPeriodRange"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.serialize_json(
                value["billing_period_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteCustomLineItemInput:
    out: DeleteCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("BillingPeriodRange") is not None:
        import capo_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            capo_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out
