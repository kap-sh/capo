"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter
    import capo_billingconductor.types.max_custom_line_item_results
    import capo_billingconductor.types.token


class ListResourcesAssociatedToCustomLineItemInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The billing period for which the resource associations will be listed. </p>"""
    arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> The ARN of the custom line item for which the resource associations will be listed. </p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
    ]
    """<p> (Optional) The maximum number of resource associations to be retrieved. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> (Optional) The pagination token that's returned by a previous request. </p>"""
    filters: NotRequired[
        "capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter.ListResourcesAssociatedToCustomLineItemFilter"
    ]
    """<p> (Optional) A <code>ListResourcesAssociatedToCustomLineItemFilter</code> that can specify the types of resources that should be retrieved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesAssociatedToCustomLineItemInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    out["Arn"] = value["arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter

        out["Filters"] = (
            capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListResourcesAssociatedToCustomLineItemInput:
    out: ListResourcesAssociatedToCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter

        out["filters"] = (
            capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
