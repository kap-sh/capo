"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#UpdateMarketplaceRevenueShareAllocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id
    import capo_partnercentral_revenue_measurement.types.revenue_share_percent
    import capo_partnercentral_revenue_measurement.types.revision_token


class UpdateMarketplaceRevenueShareAllocationInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog containing the allocation.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier for the parent revenue share.</p>"""
    marketplace_revenue_share_allocation_id: "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_id.MarketplaceRevenueShareAllocationId"
    """<p>The identifier of the allocation to update.</p>"""
    marketplace_revenue_share_revision: (
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    )
    """<p>The current revision of the parent share. Must match for optimistic concurrency control.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
    ]
    """<p>A unique token to ensure idempotency of the update request.</p>"""
    effective_from: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>The new effective start date. Must be the first day of a month. Only modifiable on future-dated allocations.</p>"""
    effective_until: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>The new effective end date. Must be the last day of a month and on or after today.</p>"""
    revenue_share_percent: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_share_percent.RevenueSharePercent"
    ]
    """<p>The new revenue share percentage. Only modifiable on future-dated allocations.</p>"""
    status: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
    ]
    """<p>The new status. Set to INACTIVE for soft-delete. Only modifiable on future-dated allocations.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateMarketplaceRevenueShareAllocationInput) -> dict:
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
    out["MarketplaceRevenueShareRevision"] = value["marketplace_revenue_share_revision"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "effective_from" in value:
        out["EffectiveFrom"] = value["effective_from"]
    if "effective_until" in value:
        out["EffectiveUntil"] = value["effective_until"]
    if "revenue_share_percent" in value:
        out["RevenueSharePercent"] = value["revenue_share_percent"]
    if "status" in value:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["Status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.serialize_cbor(
                value["status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateMarketplaceRevenueShareAllocationInput:
    out: UpdateMarketplaceRevenueShareAllocationInput = {}  # type: ignore[typeddict-item]
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
    else:
        out["marketplace_revenue_share_revision"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("EffectiveFrom") is not None:
        out["effective_from"] = data["EffectiveFrom"]
    if data.get("EffectiveUntil") is not None:
        out["effective_until"] = data["EffectiveUntil"]
    if data.get("RevenueSharePercent") is not None:
        out["revenue_share_percent"] = data["RevenueSharePercent"]
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.deserialize_cbor(
                data["Status"]
            )
        )
    return out
