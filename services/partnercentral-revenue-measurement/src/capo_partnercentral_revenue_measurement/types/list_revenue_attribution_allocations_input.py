"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListRevenueAttributionAllocationsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_revenue_measurement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.allocation_effective_date_string
    import capo_partnercentral_revenue_measurement.types.allocation_status
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list
    import capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list
    import capo_partnercentral_revenue_measurement.types.entity_type_filter_list
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revision_token
    import capo_partnercentral_revenue_measurement.types.sort_order


class ListRevenueAttributionAllocationsInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog that contains the resource.</p>"""
    revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The revenue attribution identifier to query.</p>"""
    entity_type_filters: NotRequired[
        "capo_partnercentral_revenue_measurement.types.entity_type_filter_list.EntityTypeFilterList"
    ]
    """<p>Filter by deal entity types.</p>"""
    entity_identifier_filters: NotRequired[
        "capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list.EntityIdentifierFilterList"
    ]
    """<p>Filter by deal entity identifiers.</p>"""
    customer_aws_account_id_filters: NotRequired[
        "capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list.CustomerAwsAccountIdFilterList"
    ]
    """<p>Filter by customer AWS account IDs for associated deal entities.</p>"""
    status_filter: NotRequired[
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
    after_effective_until: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>Inclusive lower bound for EffectiveUntil date filter.</p>"""
    before_effective_until: NotRequired[
        "capo_partnercentral_revenue_measurement.types.allocation_effective_date_string.AllocationEffectiveDateString"
    ]
    """<p>Exclusive upper bound for EffectiveUntil date filter (half-open range).</p>"""
    sort_by: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field.RevenueAttributionAllocationSortField"
    ]
    """<p>Field to sort by.</p>"""
    sort_order: NotRequired[
        "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
    ]
    """<p>Sort direction. Defaults to ASCENDING.</p>"""
    revenue_attribution_revision: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    ]
    """<p>Point-in-time revision number to query.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum results per page.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Pagination token from previous response.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRevenueAttributionAllocationsInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["RevenueAttributionIdentifier"] = value["revenue_attribution_identifier"]
    if "entity_type_filters" in value:
        import capo_partnercentral_revenue_measurement.types.entity_type_filter_list

        out["EntityTypeFilters"] = (
            capo_partnercentral_revenue_measurement.types.entity_type_filter_list.serialize_cbor(
                value["entity_type_filters"]
            )
        )
    if "entity_identifier_filters" in value:
        import capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list

        out["EntityIdentifierFilters"] = (
            capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list.serialize_cbor(
                value["entity_identifier_filters"]
            )
        )
    if "customer_aws_account_id_filters" in value:
        import capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list

        out["CustomerAwsAccountIdFilters"] = (
            capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list.serialize_cbor(
                value["customer_aws_account_id_filters"]
            )
        )
    if "status_filter" in value:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["StatusFilter"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.serialize_cbor(
                value["status_filter"]
            )
        )
    if "after_effective_from" in value:
        out["AfterEffectiveFrom"] = value["after_effective_from"]
    if "before_effective_from" in value:
        out["BeforeEffectiveFrom"] = value["before_effective_from"]
    if "after_effective_until" in value:
        out["AfterEffectiveUntil"] = value["after_effective_until"]
    if "before_effective_until" in value:
        out["BeforeEffectiveUntil"] = value["before_effective_until"]
    if "sort_by" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field

        out["SortBy"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field.serialize_cbor(
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
    if "revenue_attribution_revision" in value:
        out["RevenueAttributionRevision"] = value["revenue_attribution_revision"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRevenueAttributionAllocationsInput:
    out: ListRevenueAttributionAllocationsInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_revenue_measurement.types.catalog_name

        out["catalog"] = (
            capo_partnercentral_revenue_measurement.types.catalog_name.deserialize_cbor(
                data["Catalog"]
            )
        )
    else:
        raise DeserializationError(
            "ListRevenueAttributionAllocationsInput.catalog required"
        )
    if data.get("RevenueAttributionIdentifier") is not None:
        out["revenue_attribution_identifier"] = data["RevenueAttributionIdentifier"]
    else:
        raise DeserializationError(
            "ListRevenueAttributionAllocationsInput.revenue_attribution_identifier required"
        )
    if data.get("EntityTypeFilters") is not None:
        import capo_partnercentral_revenue_measurement.types.entity_type_filter_list

        out["entity_type_filters"] = (
            capo_partnercentral_revenue_measurement.types.entity_type_filter_list.deserialize_cbor(
                data["EntityTypeFilters"]
            )
        )
    if data.get("EntityIdentifierFilters") is not None:
        import capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list

        out["entity_identifier_filters"] = (
            capo_partnercentral_revenue_measurement.types.entity_identifier_filter_list.deserialize_cbor(
                data["EntityIdentifierFilters"]
            )
        )
    if data.get("CustomerAwsAccountIdFilters") is not None:
        import capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list

        out["customer_aws_account_id_filters"] = (
            capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list.deserialize_cbor(
                data["CustomerAwsAccountIdFilters"]
            )
        )
    if data.get("StatusFilter") is not None:
        import capo_partnercentral_revenue_measurement.types.allocation_status

        out["status_filter"] = (
            capo_partnercentral_revenue_measurement.types.allocation_status.deserialize_cbor(
                data["StatusFilter"]
            )
        )
    if data.get("AfterEffectiveFrom") is not None:
        out["after_effective_from"] = data["AfterEffectiveFrom"]
    if data.get("BeforeEffectiveFrom") is not None:
        out["before_effective_from"] = data["BeforeEffectiveFrom"]
    if data.get("AfterEffectiveUntil") is not None:
        out["after_effective_until"] = data["AfterEffectiveUntil"]
    if data.get("BeforeEffectiveUntil") is not None:
        out["before_effective_until"] = data["BeforeEffectiveUntil"]
    if data.get("SortBy") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field

        out["sort_by"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_allocation_sort_field.deserialize_cbor(
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
    if data.get("RevenueAttributionRevision") is not None:
        out["revenue_attribution_revision"] = data["RevenueAttributionRevision"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRevenueAttributionAllocationsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer_aws_account_id_filters" in value:
        import capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list

        out["customer_aws_account_id_filters"] = (
            capo_partnercentral_revenue_measurement.types.customer_aws_account_id_filter_list.redact_sensitive(
                value["customer_aws_account_id_filters"]
            )
        )
    return out
