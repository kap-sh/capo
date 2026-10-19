"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetRevenueAttributionAllocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revision_token


class GetRevenueAttributionAllocationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that contains the resource.</p>"""
    revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The revenue attribution identifier.</p>"""
    revenue_attribution_allocation_id: "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_id.RevenueAttributionAllocationId"
    """<p>The allocation identifier.</p>"""
    revenue_attribution_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>Point-in-time revision number to query.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRevenueAttributionAllocationInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["RevenueAttributionIdentifier"] = value["revenue_attribution_identifier"]
    out["RevenueAttributionAllocationId"] = value["revenue_attribution_allocation_id"]
    if "revenue_attribution_revision" in value:
        out["RevenueAttributionRevision"] = value["revenue_attribution_revision"]
    return out


def deserialize_cbor(data: dict) -> GetRevenueAttributionAllocationInput:
    out: GetRevenueAttributionAllocationInput = {}  # type: ignore[typeddict-item]
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
    if data.get("RevenueAttributionAllocationId") is not None:
        out["revenue_attribution_allocation_id"] = data[
            "RevenueAttributionAllocationId"
        ]
    else:
        out["revenue_attribution_allocation_id"] = ""
    if data.get("RevenueAttributionRevision") is not None:
        out["revenue_attribution_revision"] = data["RevenueAttributionRevision"]
    return out
