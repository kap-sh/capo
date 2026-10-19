"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListMarketplaceRevenueShareAllocationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.marketplace_product_id
    import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.revision_token
    import capo_partnercentral_revenue_measurement.types.sort_order


class ListMarketplaceRevenueShareAllocationsInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog containing the allocations.</p>"""
    product_id: "capo_partnercentral_revenue_measurement.types.marketplace_product_id.MarketplaceProductId"
    """<p>The AWS Marketplace product identifier for the parent revenue share.</p>"""
    status: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_status.AllocationStatus"
    ]
    """<p>Filter by allocation status.</p>"""
    after_effective_from: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>Inclusive lower bound for EffectiveFrom date filter.</p>"""
    before_effective_from: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>Exclusive upper bound for EffectiveFrom date filter (half-open range).</p>"""
    sort_by: NotRequired[
        "capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field.MarketplaceRevenueShareAllocationSortField"
    ]
    """<p>The field to sort marketplace revenue share allocations by.</p>"""
    sort_order: NotRequired[
        "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
    ]
    """<p>The direction to sort results. Defaults to DESCENDING.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results per page.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Pagination token from a previous response.</p>"""
    marketplace_revenue_share_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>Optional share revision for historical list. Returns allocations as they existed at this revision.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMarketplaceRevenueShareAllocationsInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["ProductId"] = value["product_id"]
    if "status" in value:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["Status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.serialize_cbor(
                value["status"]
            )
        )
    if "after_effective_from" in value:
        out["AfterEffectiveFrom"] = value["after_effective_from"]
    if "before_effective_from" in value:
        out["BeforeEffectiveFrom"] = value["before_effective_from"]
    if "sort_by" in value:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field

        out["SortBy"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field.serialize_cbor(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_partnercentral_revenue_measurement.types.sort_order

        out["SortOrder"] = (
            capo_partnercentral_revenue_measurement.types.sort_order.serialize_cbor(
                value["sort_order"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "marketplace_revenue_share_revision" in value:
        out["MarketplaceRevenueShareRevision"] = value[
            "marketplace_revenue_share_revision"
        ]
    return out


def deserialize_cbor(data: dict) -> ListMarketplaceRevenueShareAllocationsInput:
    out: ListMarketplaceRevenueShareAllocationsInput = {}  # type: ignore[typeddict-item]
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
    if data.get("Status") is not None:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["status"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("AfterEffectiveFrom") is not None:
        out["after_effective_from"] = data["AfterEffectiveFrom"]
    if data.get("BeforeEffectiveFrom") is not None:
        out["before_effective_from"] = data["BeforeEffectiveFrom"]
    if data.get("SortBy") is not None:
        import capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field

        out["sort_by"] = (
            capo_partnercentral_revenue_measurement.types.marketplace_revenue_share_allocation_sort_field.deserialize_cbor(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_partnercentral_revenue_measurement.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_revenue_measurement.types.sort_order.deserialize_cbor(
                data["SortOrder"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MarketplaceRevenueShareRevision") is not None:
        out["marketplace_revenue_share_revision"] = data[
            "MarketplaceRevenueShareRevision"
        ]
    return out
