"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueAttributionAllocationErrorDetailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail

RevenueAttributionAllocationErrorDetailList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail.RevenueAttributionAllocationErrorDetail"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueAttributionAllocationErrorDetailList) -> list:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RevenueAttributionAllocationErrorDetailList:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail

    out: RevenueAttributionAllocationErrorDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: RevenueAttributionAllocationErrorDetailList) -> list[Any]:
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail

    return [
        capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_error_detail.redact_sensitive(
            item
        )
        for item in value
    ]
