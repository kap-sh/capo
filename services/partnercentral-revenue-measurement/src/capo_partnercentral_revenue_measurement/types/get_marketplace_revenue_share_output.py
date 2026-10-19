"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#GetMarketplaceRevenueShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id


class GetMarketplaceRevenueShareOutput(TypedDict, closed=True):
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier of the revenue share.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the marketplace revenue share.</p>"""
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that the marketplace revenue share belongs to.</p>"""
    product_code: NotRequired["str"]
    """<p>The AWS Marketplace product code.</p>"""
    product_name: NotRequired["str"]
    """<p>The display name of the AWS Marketplace product.</p>"""
    created_date: NotRequired["datetime.datetime"]
    """<p>The date when the marketplace revenue share was created.</p>"""
    last_modified_date: NotRequired["datetime.datetime"]
    """<p>The date when the marketplace revenue share was last modified.</p>"""
    revision: NotRequired["int"]
    """<p>The revision number of the retrieved marketplace revenue share.</p>"""
    latest_revision: NotRequired["int"]
    """<p>The latest revision number of the marketplace revenue share.</p>"""
    total_active_marketplace_revenue_share_allocation_count: NotRequired["int"]
    """<p>The number of active allocations under this marketplace revenue share.</p>"""
    total_marketplace_revenue_share_allocation_count: NotRequired["int"]
    """<p>The total number of allocations under this marketplace revenue share.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMarketplaceRevenueShareOutput) -> dict:
    out: dict = {}
    out["ProductId"] = value["product_id"]
    out["Arn"] = value["arn"]
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "created_date" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["CreatedDate"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["created_date"]
            )
        )
    if "last_modified_date" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["LastModifiedDate"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["last_modified_date"]
            )
        )
    if "revision" in value:
        out["Revision"] = value["revision"]
    if "latest_revision" in value:
        out["LatestRevision"] = value["latest_revision"]
    if "total_active_marketplace_revenue_share_allocation_count" in value:
        out["TotalActiveMarketplaceRevenueShareAllocationCount"] = value[
            "total_active_marketplace_revenue_share_allocation_count"
        ]
    if "total_marketplace_revenue_share_allocation_count" in value:
        out["TotalMarketplaceRevenueShareAllocationCount"] = value[
            "total_marketplace_revenue_share_allocation_count"
        ]
    return out


def deserialize_cbor(data: dict) -> GetMarketplaceRevenueShareOutput:
    out: GetMarketplaceRevenueShareOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
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
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    if data.get("CreatedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedDate"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["last_modified_date"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["LastModifiedDate"]
            )
        )
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    if data.get("LatestRevision") is not None:
        out["latest_revision"] = data["LatestRevision"]
    if data.get("TotalActiveMarketplaceRevenueShareAllocationCount") is not None:
        out["total_active_marketplace_revenue_share_allocation_count"] = data[
            "TotalActiveMarketplaceRevenueShareAllocationCount"
        ]
    if data.get("TotalMarketplaceRevenueShareAllocationCount") is not None:
        out["total_marketplace_revenue_share_allocation_count"] = data[
            "TotalMarketplaceRevenueShareAllocationCount"
        ]
    return out
