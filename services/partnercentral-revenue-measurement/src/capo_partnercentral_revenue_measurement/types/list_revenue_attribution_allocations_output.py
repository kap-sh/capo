"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListRevenueAttributionAllocationsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list


class ListRevenueAttributionAllocationsOutput(TypedDict, closed=True):
    revenue_attribution_allocation_summaries: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list.RevenueAttributionAllocationSummaryList"
    """<p>Paginated list of allocations matching filters.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Token for next page. Absent if no more results.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRevenueAttributionAllocationsOutput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list

    out["RevenueAttributionAllocationSummaries"] = (
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list.serialize_cbor(
            value["revenue_attribution_allocation_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRevenueAttributionAllocationsOutput:
    out: ListRevenueAttributionAllocationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RevenueAttributionAllocationSummaries") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list

        out["revenue_attribution_allocation_summaries"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list.deserialize_cbor(
                data["RevenueAttributionAllocationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListRevenueAttributionAllocationsOutput.revenue_attribution_allocation_summaries required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRevenueAttributionAllocationsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "revenue_attribution_allocation_summaries" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list

        out["revenue_attribution_allocation_summaries"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary_list.redact_sensitive(
                value["revenue_attribution_allocation_summaries"]
            )
        )
    return out
