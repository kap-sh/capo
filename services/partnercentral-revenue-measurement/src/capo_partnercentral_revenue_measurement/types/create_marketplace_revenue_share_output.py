"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#CreateMarketplaceRevenueShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id


class CreateMarketplaceRevenueShareOutput(TypedDict, closed=True):
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier of the newly created revenue share.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the newly created marketplace revenue share.</p>"""
    catalog: NotRequired[
        "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    ]
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
    """<p>The revision number of the newly created marketplace revenue share.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateMarketplaceRevenueShareOutput) -> dict:
    out: dict = {}
    out["ProductId"] = value["product_id"]
    out["Arn"] = value["arn"]
    if "catalog" in value:
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
    return out


def deserialize_cbor(data: dict) -> CreateMarketplaceRevenueShareOutput:
    out: CreateMarketplaceRevenueShareOutput = {}  # type: ignore[typeddict-item]
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
    return out
