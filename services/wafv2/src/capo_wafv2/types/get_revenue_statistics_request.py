"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRevenueStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.currency
    import capo_wafv2.types.group_by_type
    import capo_wafv2.types.monetization_filter_list
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.path_statistics_limit
    import capo_wafv2.types.ranking_sort_by
    import capo_wafv2.types.ranking_statistic_type
    import capo_wafv2.types.scope
    import capo_wafv2.types.sort_order
    import capo_wafv2.types.time_window


class GetRevenueStatisticsRequest(TypedDict, closed=True):
    statistic_type: "capo_wafv2.types.ranking_statistic_type.RankingStatisticType"
    """<p> <code>TOP_SOURCES_BY_REVENUE</code> ranks revenue from AI bot traffic, grouped by the dimension you specify in the <code>GroupBy</code> parameter (<code>NAME</code>, <code>CATEGORY</code>, <code>INTENT</code>, <code>ORGANIZATION</code>, or <code>WEBACL</code>); <code>GroupBy</code> is required for this statistic type. <code>TOP_PATHS_BY_REVENUE</code> ranks revenue by path.</p>"""
    time_window: "capo_wafv2.types.time_window.TimeWindow"
    """<p>The time range for the query. Specify start and end timestamps.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>).</p>"""
    currency: "capo_wafv2.types.currency.Currency"
    """<p>The currency for the revenue amounts in the response.</p>"""
    group_by: NotRequired["capo_wafv2.types.group_by_type.GroupByType"]
    """<p>The dimension to group results by: <code>NAME</code>, <code>CATEGORY</code>, <code>INTENT</code>, <code>ORGANIZATION</code>, or <code>WEBACL</code>. Required when <code>StatisticType</code> is <code>TOP_SOURCES_BY_REVENUE</code>. Not required for <code>TOP_PATHS_BY_REVENUE</code>, where results are grouped by content path. If <code>StatisticType</code> is <code>TOP_SOURCES_BY_REVENUE</code> and <code>GroupBy</code> is omitted, the request is rejected with a <code>WAFInvalidParameterException</code>.</p>"""
    filters: NotRequired[
        "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
    ]
    """<p>Optional filters to narrow the results.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you get a paginated response, this marker indicates that additional results are available. Use it in a subsequent request to retrieve the next page of results.</p>"""
    limit: NotRequired["capo_wafv2.types.path_statistics_limit.PathStatisticsLimit"]
    """<p>The maximum number of results to return.</p>"""
    sort_by: NotRequired["capo_wafv2.types.ranking_sort_by.RankingSortBy"]
    """<p>The field to sort results by: <code>REVENUE</code>, <code>PERCENTAGE</code>, or <code>NAME</code>.</p>"""
    sort_order: NotRequired["capo_wafv2.types.sort_order.SortOrder"]
    """<p>The sort order: <code>ASC</code> for ascending or <code>DESC</code> for descending.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRevenueStatisticsRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.ranking_statistic_type

    out["StatisticType"] = (
        capo_wafv2.types.ranking_statistic_type.serialize_aws_json_1_1(
            value["statistic_type"]
        )
    )
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
    if "group_by" in value:
        import capo_wafv2.types.group_by_type

        out["GroupBy"] = capo_wafv2.types.group_by_type.serialize_aws_json_1_1(
            value["group_by"]
        )
    if "filters" in value:
        import capo_wafv2.types.monetization_filter_list

        out["Filters"] = (
            capo_wafv2.types.monetization_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "sort_by" in value:
        import capo_wafv2.types.ranking_sort_by

        out["SortBy"] = capo_wafv2.types.ranking_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_wafv2.types.sort_order

        out["SortOrder"] = capo_wafv2.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRevenueStatisticsRequest:
    out: GetRevenueStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatisticType") is not None:
        import capo_wafv2.types.ranking_statistic_type

        out["statistic_type"] = (
            capo_wafv2.types.ranking_statistic_type.deserialize_aws_json_1_1(
                data["StatisticType"]
            )
        )
    else:
        import typing

        out["statistic_type"] = typing.cast(
            "capo_wafv2.types.ranking_statistic_type.RankingStatisticType", ""
        )
    if data.get("TimeWindow") is not None:
        import capo_wafv2.types.time_window

        out["time_window"] = capo_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError("GetRevenueStatisticsRequest.time_window required")
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
    if data.get("GroupBy") is not None:
        import capo_wafv2.types.group_by_type

        out["group_by"] = capo_wafv2.types.group_by_type.deserialize_aws_json_1_1(
            data["GroupBy"]
        )
    if data.get("Filters") is not None:
        import capo_wafv2.types.monetization_filter_list

        out["filters"] = (
            capo_wafv2.types.monetization_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("SortBy") is not None:
        import capo_wafv2.types.ranking_sort_by

        out["sort_by"] = capo_wafv2.types.ranking_sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if data.get("SortOrder") is not None:
        import capo_wafv2.types.sort_order

        out["sort_order"] = capo_wafv2.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
