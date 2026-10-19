"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetMarketplaceRevenueShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id


class GetMarketplaceRevenueShareInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that the marketplace revenue share belongs to.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier of the revenue share to retrieve.</p>"""
    revision: NotRequired["int"]
    """<p>The revision of the marketplace revenue share to retrieve. Omit to return the latest revision.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMarketplaceRevenueShareInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["ProductId"] = value["product_id"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_cbor(data: dict) -> GetMarketplaceRevenueShareInput:
    out: GetMarketplaceRevenueShareInput = {}  # type: ignore[typeddict-item]
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
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    return out
