"""Generated from Smithy shape ``com.amazonaws.wafv2#ListSettlementRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.currency
    import capo_wafv2.types.monetization_filter_list
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.scope
    import capo_wafv2.types.settlement_record_limit
    import capo_wafv2.types.settlement_sort_by
    import capo_wafv2.types.sort_order
    import capo_wafv2.types.time_window


class ListSettlementRecordsRequest(TypedDict, closed=True):
    time_window: "capo_wafv2.types.time_window.TimeWindow"
    """<p>The time range for the query. Specify start and end timestamps.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>).</p>"""
    currency: "capo_wafv2.types.currency.Currency"
    """<p>The currency for the amounts in the response.</p>"""
    filters: NotRequired[
        "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
    ]
    """<p>Optional filters to narrow the results. You can filter by payer address, status, source name, network, or other settlement fields.</p>"""
    sort_by: NotRequired["capo_wafv2.types.settlement_sort_by.SettlementSortBy"]
    """<p>The field to sort settlement records by: <code>TIMESTAMP</code>, <code>AMOUNT</code>, <code>NAME</code>, or <code>STATUS</code>.</p>"""
    sort_order: NotRequired["capo_wafv2.types.sort_order.SortOrder"]
    """<p>The sort order: <code>ASC</code> for ascending or <code>DESC</code> for descending.</p>"""
    limit: NotRequired["capo_wafv2.types.settlement_record_limit.SettlementRecordLimit"]
    """<p>The maximum number of settlement records to return. Minimum: 1. Maximum: 100.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you get a paginated response, this marker indicates that additional results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSettlementRecordsRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.time_window

    out["TimeWindow"] = capo_wafv2.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import capo_wafv2.types.currency

    out["Currency"] = capo_wafv2.types.currency.serialize_aws_json_1_1(
        value["currency"]
    )
    if "filters" in value:
        import capo_wafv2.types.monetization_filter_list

        out["Filters"] = (
            capo_wafv2.types.monetization_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "sort_by" in value:
        import capo_wafv2.types.settlement_sort_by

        out["SortBy"] = capo_wafv2.types.settlement_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_wafv2.types.sort_order

        out["SortOrder"] = capo_wafv2.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSettlementRecordsRequest:
    out: ListSettlementRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TimeWindow") is not None:
        import capo_wafv2.types.time_window

        out["time_window"] = capo_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError("ListSettlementRecordsRequest.time_window required")
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("Currency") is not None:
        import capo_wafv2.types.currency

        out["currency"] = capo_wafv2.types.currency.deserialize_aws_json_1_1(
            data["Currency"]
        )
    else:
        import typing

        out["currency"] = typing.cast("capo_wafv2.types.currency.Currency", "")
    if data.get("Filters") is not None:
        import capo_wafv2.types.monetization_filter_list

        out["filters"] = (
            capo_wafv2.types.monetization_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_wafv2.types.settlement_sort_by

        out["sort_by"] = capo_wafv2.types.settlement_sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if data.get("SortOrder") is not None:
        import capo_wafv2.types.sort_order

        out["sort_order"] = capo_wafv2.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
