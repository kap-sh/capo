"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#RevenueShareAllocationChangeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation

RevenueShareAllocationChangeList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.revenue_share_allocation.RevenueShareAllocation"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevenueShareAllocationChangeList) -> list:
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.revenue_share_allocation.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RevenueShareAllocationChangeList:
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation

    out: RevenueShareAllocationChangeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.revenue_share_allocation.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: RevenueShareAllocationChangeList) -> list[Any]:
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation

    return [
        capo_partnercentral_revenue_measurement.types.revenue_share_allocation.redact_sensitive(
            item
        )
        for item in value
    ]
