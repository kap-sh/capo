"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetMarketplaceRevenueShareAllocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id
    import capo_partnercentral_revenue_measurement.types.revision_token


class GetMarketplaceRevenueShareAllocationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that the allocation belongs to.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier of the parent revenue share.</p>"""
    marketplace_revenue_share_allocation_id: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id.MarketplaceRevenueShareAllocationId"
    """<p>The unique identifier of the allocation to retrieve.</p>"""
    marketplace_revenue_share_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The revision of the parent marketplace revenue share at which to retrieve the allocation. Omit to return the latest.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMarketplaceRevenueShareAllocationInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["ProductId"] = value["product_id"]
    out["MarketplaceRevenueShareAllocationId"] = value[
        "marketplace_revenue_share_allocation_id"
    ]
    if "marketplace_revenue_share_revision" in value:
        out["MarketplaceRevenueShareRevision"] = value[
            "marketplace_revenue_share_revision"
        ]
    return out


def deserialize_cbor(data: dict) -> GetMarketplaceRevenueShareAllocationInput:
    out: GetMarketplaceRevenueShareAllocationInput = {}  # type: ignore[typeddict-item]
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
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("MarketplaceRevenueShareAllocationId") is not None:
        out["marketplace_revenue_share_allocation_id"] = data[
            "MarketplaceRevenueShareAllocationId"
        ]
    else:
        out["marketplace_revenue_share_allocation_id"] = ""
    if data.get("MarketplaceRevenueShareRevision") is not None:
        out["marketplace_revenue_share_revision"] = data[
            "MarketplaceRevenueShareRevision"
        ]
    return out
