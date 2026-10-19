"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CreateMarketplaceRevenueShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list


class CreateMarketplaceRevenueShareInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog in which to create the marketplace revenue share.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
    ]
    """<p>A unique token to ensure idempotency of the create request.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier for this revenue share.</p>"""
    tags: NotRequired[
        "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list.MarketplaceRevenueShareTagList"
    ]
    """<p>Tags to associate with the marketplace revenue share upon creation.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateMarketplaceRevenueShareInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ProductId"] = value["product_id"]
    if "tags" in value:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list

        out["Tags"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list.serialize_cbor(
                value["tags"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateMarketplaceRevenueShareInput:
    out: CreateMarketplaceRevenueShareInput = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("Tags") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list

        out["tags"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_tag_list.deserialize_cbor(
                data["Tags"]
            )
        )
    return out
