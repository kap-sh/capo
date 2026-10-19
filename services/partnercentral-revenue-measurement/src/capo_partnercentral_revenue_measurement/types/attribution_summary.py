"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#AttributionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.allocation_count
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_summary
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_id
    import capo_partnercentral_revenue_measurement.types.revision_token
    import capo_partnercentral_revenue_measurement.types.tenancy_model


class AttributionSummary(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the revenue attribution.</p>"""
    id: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_id.RevenueAttributionId"
    ]
    """<p>The unique identifier of the revenue attribution.</p>"""
    catalog: NotRequired[
        "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    ]
    """<p>The catalog that the revenue attribution belongs to.</p>"""
    name: NotRequired["str"]
    """<p>The display name of the revenue attribution.</p>"""
    tenancy_model: (
        "capo_partnercentral_revenue_measurement.types.tenancy_model.TenancyModel"
    )
    """<p>The tenancy model for this revenue attribution.</p>"""
    marketplace_product: NotRequired[
        "capo_partnercentral_revenue_measurement.types.marketplace_product_summary.MarketplaceProductSummary"
    ]
    """<p>The AWS Marketplace product attributes associated with this attribution, if set.</p>"""
    created_date: NotRequired["datetime.datetime"]
    """<p>The date when the revenue attribution was created.</p>"""
    last_modified_date: NotRequired["datetime.datetime"]
    """<p>The date when the revenue attribution was last modified.</p>"""
    latest_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>The latest revision of the revenue attribution resource.</p>"""
    effective_from: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>The date from which this revenue attribution is effective, derived from the earliest allocation start date (YYYY-MM-DD).</p>"""
    effective_until: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>The date until which this revenue attribution is effective, derived from the latest allocation end date (YYYY-MM-DD).</p>"""
    total_active_revenue_attribution_allocation_count: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_count.AllocationCount"
    ]
    """<p>The total number of allocations under this revenue attribution whose Status is ACTIVE.</p>"""
    total_revenue_attribution_allocation_count: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_count.AllocationCount"
    ]
    """<p>The total number of allocations under this revenue attribution, counting both ACTIVE and INACTIVE.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttributionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "catalog" in value:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["Catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
                value["catalog"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    import capo_partnercentral_revenue_measurement.types.tenancy_model

    out["TenancyModel"] = (
        capo_partnercentral_revenue_measurement.types.tenancy_model.serialize_cbor(
            value["tenancy_model"]
        )
    )
    if "marketplace_product" in value:
        import capo_partnercentral_revenue_measurement.types.marketplace_product_summary

        out["MarketplaceProduct"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_product_summary.serialize_cbor(
                value["marketplace_product"]
            )
        )
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
    if "latest_revision" in value:
        out["LatestRevision"] = value["latest_revision"]
    if "effective_from" in value:
        out["EffectiveFrom"] = value["effective_from"]
    if "effective_until" in value:
        out["EffectiveUntil"] = value["effective_until"]
    if "total_active_revenue_attribution_allocation_count" in value:
        out["TotalActiveRevenueAttributionAllocationCount"] = value[
            "total_active_revenue_attribution_allocation_count"
        ]
    if "total_revenue_attribution_allocation_count" in value:
        out["TotalRevenueAttributionAllocationCount"] = value[
            "total_revenue_attribution_allocation_count"
        ]
    return out


def deserialize_cbor(data: dict) -> AttributionSummary:
    out: AttributionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TenancyModel") is not None:
        import capo_partnercentral_revenue_measurement.types.tenancy_model

        out["tenancy_model"] = (
            capo_partnercentral_revenue_measurement.types.tenancy_model.deserialize_cbor(
                data["TenancyModel"]
            )
        )
    else:
        import typing

        out["tenancy_model"] = typing.cast(
            "capo_partnercentral_revenue_measurement.types.tenancy_model.TenancyModel",
            "",
        )
    if data.get("MarketplaceProduct") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_product_summary

        out["marketplace_product"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_product_summary.deserialize_cbor(
                data["MarketplaceProduct"]
            )
        )
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
    if data.get("LatestRevision") is not None:
        out["latest_revision"] = data["LatestRevision"]
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    if data.get("TotalActiveRevenueAttributionAllocationCount") is not None:
        out["total_active_revenue_attribution_allocation_count"] = data[
            "TotalActiveRevenueAttributionAllocationCount"
        ]
    if data.get("TotalRevenueAttributionAllocationCount") is not None:
        out["total_revenue_attribution_allocation_count"] = data[
            "TotalRevenueAttributionAllocationCount"
        ]
    return out
