"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ListRevenueAttributionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_partnercentral_revenue_measurement.types.attribution_sort_by
    import capo_partnercentral_revenue_measurement.types.catalog_name
    import capo_partnercentral_revenue_measurement.types.next_token
    import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list
    import capo_partnercentral_revenue_measurement.types.sort_order


class ListRevenueAttributionsInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_revenue_measurement.types.catalog_name.CatalogName"
    """<p>The catalog to list revenue attributions from.</p>"""
    identifiers: NotRequired[
        "capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list.RevenueAttributionIdentifierList"
    ]
    """<p>Filter results to only include revenue attributions with the specified identifiers.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>Filter results to only include revenue attributions created after this timestamp.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>Filter results to only include revenue attributions created before this timestamp.</p>"""
    sort_by: NotRequired[
        "capo_partnercentral_revenue_measurement.types.attribution_sort_by.AttributionSortBy"
    ]
    """<p>The field to sort revenue attributions by.</p>"""
    sort_order: NotRequired[
        "capo_partnercentral_revenue_measurement.types.sort_order.SortOrder"
    ]
    """<p>The direction to sort results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired[
        "capo_partnercentral_revenue_measurement.types.next_token.NextToken"
    ]
    """<p>Token for pagination. Use the value returned in the previous response to retrieve the next page.</p>"""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRevenueAttributionsInput) -> dict:
    out: dict = {}
    import capo_partnercentral_revenue_measurement.types.catalog_name

    out["Catalog"] = (
        capo_partnercentral_revenue_measurement.types.catalog_name.serialize_cbor(
            value["catalog"]
        )
    )
    if "identifiers" in value:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list

        out["Identifiers"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list.serialize_cbor(
                value["identifiers"]
            )
        )
    if "created_after" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["CreatedAfter"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["created_after"]
            )
        )
    if "created_before" in value:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["CreatedBefore"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.serialize_cbor(
                value["created_before"]
            )
        )
    if "sort_by" in value:
        import capo_partnercentral_revenue_measurement.types.attribution_sort_by

        out["SortBy"] = (
            capo_partnercentral_revenue_measurement.types.attribution_sort_by.serialize_cbor(
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
    return out


def deserialize_cbor(data: dict) -> ListRevenueAttributionsInput:
    out: ListRevenueAttributionsInput = {}  # type: ignore[typeddict-item]
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
    if data.get("Identifiers") is not None:
        import capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list

        out["identifiers"] = (
            capo_partnercentral_revenue_measurement.types.revenue_attribution_identifier_list.deserialize_cbor(
                data["Identifiers"]
            )
        )
    if data.get("CreatedAfter") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_after"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedAfter"]
            )
        )
    if data.get("CreatedBefore") is not None:
        import capo_partnercentral_revenue_measurement.types._prelude.timestamp

        out["created_before"] = (
            capo_partnercentral_revenue_measurement.types._prelude.timestamp.deserialize_cbor(
                data["CreatedBefore"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_partnercentral_revenue_measurement.types.attribution_sort_by

        out["sort_by"] = (
            capo_partnercentral_revenue_measurement.types.attribution_sort_by.deserialize_cbor(
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
    return out
