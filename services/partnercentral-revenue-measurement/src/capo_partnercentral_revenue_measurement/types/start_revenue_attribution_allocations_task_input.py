"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#StartRevenueAttributionAllocationsTaskInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.client_token
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list
    import capo_partnercentral_revenue_measurement.types.revision_token


class StartRevenueAttributionAllocationsTaskInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog context for this operation.</p>"""
    revenue_attribution_identifier: "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier.RevenueAttributionIdentifier"
    """<p>The revenue attribution identifier.</p>"""
    revenue_attribution_revision: (
        "capo_partnercentral_revenue_measurement.types.revision_token.RevisionToken"
    )
    """<p>Current revision of the revenue attribution for optimistic locking.</p>"""
    revenue_share_allocations: "capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list.RevenueShareAllocationChangeList"
    """<p>The list of allocation changes to process in this batch.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.client_token.ClientToken"
    ]
    """<p>Idempotency token for deduplication and retry.</p>"""
    description: NotRequired["str"]
    """<p>Human-readable description of the batch.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartRevenueAttributionAllocationsTaskInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    out["RevenueAttributionIdentifier"] = value["revenue_attribution_identifier"]
    out["RevenueAttributionRevision"] = value["revenue_attribution_revision"]
    import capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list

    out["RevenueShareAllocations"] = (
        capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list.serialize_cbor(
            value["revenue_share_allocations"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> StartRevenueAttributionAllocationsTaskInput:
    out: StartRevenueAttributionAllocationsTaskInput = {}  # type: ignore[typeddict-item]
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
    if data.get("RevenueAttributionRevision") is not None:
        out["revenue_attribution_revision"] = data["RevenueAttributionRevision"]
    else:
        out["revenue_attribution_revision"] = ""
    if data.get("RevenueShareAllocations") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list

        out["revenue_share_allocations"] = (
            capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list.deserialize_cbor(
                data["RevenueShareAllocations"]
            )
        )
    else:
        out["revenue_share_allocations"] = []
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(
    value: StartRevenueAttributionAllocationsTaskInput,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "revenue_share_allocations" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list

        out["revenue_share_allocations"] = (
            capo_partnercentral_revenue_measurement.types.revenue_share_allocation_change_list.redact_sensitive(
                value["revenue_share_allocations"]
            )
        )
    return out
