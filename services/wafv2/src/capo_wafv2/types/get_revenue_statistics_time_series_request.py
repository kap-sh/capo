"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRevenueStatisticsTimeSeriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.currency
    import capo_wafv2.types.group_by_type
    import capo_wafv2.types.interval_type
    import capo_wafv2.types.max_data_points
    import capo_wafv2.types.monetization_filter_list
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.scope
    import capo_wafv2.types.time_series_statistic_type
    import capo_wafv2.types.time_window


class GetRevenueStatisticsTimeSeriesRequest(TypedDict, closed=True):
    statistic_type: (
        "capo_wafv2.types.time_series_statistic_type.TimeSeriesStatisticType"
    )
    """<p>The type of time series data to retrieve: <code>DATE_HISTOGRAM</code> for revenue over time, or <code>PAYMENT_TRAFFIC</code> for payment traffic patterns.</p>"""
    time_window: "capo_wafv2.types.time_window.TimeWindow"
    """<p>The time range for the query. Specify start and end timestamps.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a Amazon CloudFront distribution (<code>CLOUDFRONT</code>) or for a regional application (<code>REGIONAL</code>).</p>"""
    interval: "capo_wafv2.types.interval_type.IntervalType"
    """<p>The time interval for aggregating data points: <code>MINUTELY</code>, <code>FIVE_MINUTELY</code>, <code>HOURLY</code>, or <code>DAILY</code>.</p>"""
    currency: "capo_wafv2.types.currency.Currency"
    """<p>The currency for the amounts in the response.</p>"""
    group_by: NotRequired["capo_wafv2.types.group_by_type.GroupByType"]
    """<p>The dimension to group results by.</p>"""
    filters: NotRequired[
        "capo_wafv2.types.monetization_filter_list.MonetizationFilterList"
    ]
    """<p>Optional filters to narrow the results.</p>"""
    limit: NotRequired["capo_wafv2.types.max_data_points.MaxDataPoints"]
    """<p>The maximum number of data points to return. Minimum: 1. Maximum: 10000.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you get a paginated response, this marker indicates that additional results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRevenueStatisticsTimeSeriesRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.time_series_statistic_type

    out["StatisticType"] = (
        capo_wafv2.types.time_series_statistic_type.serialize_aws_json_1_1(
            value["statistic_type"]
        )
    )
    import capo_wafv2.types.time_window

    out["TimeWindow"] = capo_wafv2.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import capo_wafv2.types.interval_type

    out["Interval"] = capo_wafv2.types.interval_type.serialize_aws_json_1_1(
        value["interval"]
    )
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
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRevenueStatisticsTimeSeriesRequest:
    out: GetRevenueStatisticsTimeSeriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatisticType") is not None:
        import capo_wafv2.types.time_series_statistic_type

        out["statistic_type"] = (
            capo_wafv2.types.time_series_statistic_type.deserialize_aws_json_1_1(
                data["StatisticType"]
            )
        )
    else:
        import typing

        out["statistic_type"] = typing.cast(
            "capo_wafv2.types.time_series_statistic_type.TimeSeriesStatisticType", ""
        )
    if data.get("TimeWindow") is not None:
        import capo_wafv2.types.time_window

        out["time_window"] = capo_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError(
            "GetRevenueStatisticsTimeSeriesRequest.time_window required"
        )
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("Interval") is not None:
        import capo_wafv2.types.interval_type

        out["interval"] = capo_wafv2.types.interval_type.deserialize_aws_json_1_1(
            data["Interval"]
        )
    else:
        import typing

        out["interval"] = typing.cast("capo_wafv2.types.interval_type.IntervalType", "")
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
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
