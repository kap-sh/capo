"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.list_custom_line_items_filter
    import capo_billingconductor.types.max_custom_line_item_results
    import capo_billingconductor.types.token


class ListCustomLineItemsInput(TypedDict, closed=True):
    billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p> The preferred billing period to get custom line items (FFLIs). </p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
    ]
    """<p> The maximum number of billing groups to retrieve. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>"""
    filters: NotRequired[
        "capo_billingconductor.types.list_custom_line_items_filter.ListCustomLineItemsFilter"
    ]
    """<p>A <code>ListCustomLineItemsFilter</code> that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemsInput) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_billingconductor.types.list_custom_line_items_filter

        out["Filters"] = (
            capo_billingconductor.types.list_custom_line_items_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemsInput:
    out: ListCustomLineItemsInput = {}  # type: ignore[typeddict-item]
    if data.get("BillingPeriod") is not None:
        out["billing_period"] = data["BillingPeriod"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_billingconductor.types.list_custom_line_items_filter

        out["filters"] = (
            capo_billingconductor.types.list_custom_line_items_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out


def redact_sensitive(value: ListCustomLineItemsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_billingconductor.types.list_custom_line_items_filter

        out["filters"] = (
            capo_billingconductor.types.list_custom_line_items_filter.redact_sensitive(
                value["filters"]
            )
        )
    return out
