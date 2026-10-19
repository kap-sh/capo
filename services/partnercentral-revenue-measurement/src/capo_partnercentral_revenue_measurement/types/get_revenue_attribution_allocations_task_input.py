"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetRevenueAttributionAllocationsTaskInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier


class GetRevenueAttributionAllocationsTaskInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that contains the resource.</p>"""
    revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The revenue attribution identifier.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRevenueAttributionAllocationsTaskInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["RevenueAttributionIdentifier"] = value["revenue_attribution_identifier"]
    return out


def deserialize_cbor(data: dict) -> GetRevenueAttributionAllocationsTaskInput:
    out: GetRevenueAttributionAllocationsTaskInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName", ""
        )
    if data.get("RevenueAttributionIdentifier") is not None:
        out["revenue_attribution_identifier"] = data["RevenueAttributionIdentifier"]
    else:
        out["revenue_attribution_identifier"] = ""
    return out
