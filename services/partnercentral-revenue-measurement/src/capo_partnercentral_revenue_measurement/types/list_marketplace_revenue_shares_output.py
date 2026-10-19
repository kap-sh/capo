"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListMarketplaceRevenueSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list
    import capo_partnercentral_revenue_measurement.types.next_token


class ListMarketplaceRevenueSharesOutput(TypedDict, closed=True):
    marketplace_revenue_share_summaries: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list.MarketplaceRevenueShareSummaryList"
    """<p>The list of marketplace revenue share summaries.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Token for pagination. Present if there are more results available.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMarketplaceRevenueSharesOutput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list

    out["MarketplaceRevenueShareSummaries"] = (
        capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list.serialize_cbor(
            value["marketplace_revenue_share_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListMarketplaceRevenueSharesOutput:
    out: ListMarketplaceRevenueSharesOutput = {}  # type: ignore[typeddict-item]
    if data.get("MarketplaceRevenueShareSummaries") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list

        out["marketplace_revenue_share_summaries"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_summary_list.deserialize_cbor(
                data["MarketplaceRevenueShareSummaries"]
            )
        )
    else:
        out["marketplace_revenue_share_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
