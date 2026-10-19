"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.listing_summary_list
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.non_negative_count


class SearchListingsOutput(TypedDict, closed=True):
    total_results: (
        "capo_marketplace_discovery.types.non_negative_count.NonNegativeCount"
    )
    """<p>The total number of listings matching the search criteria.</p>"""
    listing_summaries: (
        "capo_marketplace_discovery.types.listing_summary_list.ListingSummaryList"
    )
    """<p>The listing summaries matching the search criteria. Each summary includes the listing name, description, badges, categories, pricing models, reviews, and associated products.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsOutput) -> dict:
    out: dict = {}
    out["totalResults"] = value["total_results"]
    import capo_marketplace_discovery.types.listing_summary_list

    out["listingSummaries"] = (
        capo_marketplace_discovery.types.listing_summary_list.serialize_json(
            value["listing_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchListingsOutput:
    out: SearchListingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("totalResults") is not None:
        out["total_results"] = data["totalResults"]
    else:
        out["total_results"] = 0
    if data.get("listingSummaries") is not None:
        import capo_marketplace_discovery.types.listing_summary_list

        out["listing_summaries"] = (
            capo_marketplace_discovery.types.listing_summary_list.deserialize_json(
                data["listingSummaries"]
            )
        )
    else:
        out["listing_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
