"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListMarketplaceRevenueShareAllocationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary_list
    import capo_partnercentral_revenue_measurement.types.next_token


class ListMarketplaceRevenueShareAllocationsOutput(TypedDict, closed=True):
    marketplace_revenue_share_allocation_summaries: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary_list.MarketplaceRevenueShareAllocationSummaryList"
    """<p>The list of allocation summaries for the current page.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Pagination token for the next page. Absent if no more results.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMarketplaceRevenueShareAllocationsOutput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary_list

    out["MarketplaceRevenueShareAllocationSummaries"] = (
        capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary_list.serialize_cbor(
            value["marketplace_revenue_share_allocation_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListMarketplaceRevenueShareAllocationsOutput:
    out: ListMarketplaceRevenueShareAllocationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("MarketplaceRevenueShareAllocationSummaries") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary_list

        out["marketplace_revenue_share_allocation_summaries"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_summary_list.deserialize_cbor(
                data["MarketplaceRevenueShareAllocationSummaries"]
            )
        )
    else:
        out["marketplace_revenue_share_allocation_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
