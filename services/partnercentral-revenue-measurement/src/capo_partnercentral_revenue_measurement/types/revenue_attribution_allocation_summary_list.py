"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary

RevenueAttributionAllocationSummaryList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary.RevenueAttributionAllocationSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationSummaryList) -> list:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RevenueAttributionAllocationSummaryList:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary

    out: RevenueAttributionAllocationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: RevenueAttributionAllocationSummaryList) -> list[Any]:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary

    return [
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_summary.redact_sensitive(
            item
        )
        for item in value
    ]
