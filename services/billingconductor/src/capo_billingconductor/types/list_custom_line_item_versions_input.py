"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.list_custom_line_item_versions_filter
    import capo_billingconductor.types.max_custom_line_item_results
    import capo_billingconductor.types.token


class ListCustomLineItemVersionsInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p>The Amazon Resource Name (ARN) for the custom line item.</p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
    ]
    """<p>The maximum number of custom line item versions to retrieve.</p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>"""
    filters: NotRequired[
        "capo_billingconductor.types.list_custom_line_item_versions_filter.ListCustomLineItemVersionsFilter"
    ]
    """<p>A <code>ListCustomLineItemVersionsFilter</code> that specifies the billing period range in which the custom line item versions are applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemVersionsInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_billingconductor.types.list_custom_line_item_versions_filter

        out["Filters"] = (
            capo_billingconductor.types.list_custom_line_item_versions_filter.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemVersionsInput:
    out: ListCustomLineItemVersionsInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_billingconductor.types.list_custom_line_item_versions_filter

        out["filters"] = (
            capo_billingconductor.types.list_custom_line_item_versions_filter.deserialize_json(
                data["Filters"]
            )
        )
    return out
