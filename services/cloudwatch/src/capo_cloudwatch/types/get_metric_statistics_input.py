"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricStatisticsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dimensions
    import capo_cloudwatch.types.extended_statistics
    import capo_cloudwatch.types.metric_name
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.statistics
    import capo_cloudwatch.types.timestamp


class GetMetricStatisticsInput(TypedDict, closed=True):
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace of the metric, with or without spaces.</p>"""
    metric_name: NotRequired["capo_cloudwatch.types.metric_name.MetricName"]
    """<p>The name of the metric, with or without spaces.</p>"""
    dimensions: NotRequired["capo_cloudwatch.types.dimensions.Dimensions"]
    """<p>The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can't retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations">Dimension Combinations</a> in the <i>Amazon CloudWatch User Guide</i>. For more information about specifying dimensions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html">Publishing Metrics</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""
    start_time: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.</p> <p>The value specified is inclusive; results include data points with the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).</p> <p>CloudWatch rounds the specified time stamp as follows:</p> <ul> <li> <p>Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.</p> </li> <li> <p>Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.</p> </li> <li> <p>Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.</p> </li> </ul> <p>If you set <code>Period</code> to 5, 10, 20, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, 20-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. </p>"""
    end_time: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp that determines the last data point to return.</p> <p>The value specified is exclusive; results include data points up to the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).</p>"""
    period: NotRequired["capo_cloudwatch.types.period.Period"]
    """<p>The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a <code>PutMetricData</code> call that includes a <code>StorageResolution</code> of 1 second.</p> <p>If the <code>StartTime</code> parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:</p> <ul> <li> <p>Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).</p> </li> <li> <p>Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).</p> </li> <li> <p>Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).</p> </li> </ul>"""
    statistics: NotRequired["capo_cloudwatch.types.statistics.Statistics"]
    """<p>The metric statistics, other than percentile. For percentile statistics, use <code>ExtendedStatistics</code>. When calling <code>GetMetricStatistics</code>, you must specify either <code>Statistics</code> or <code>ExtendedStatistics</code>, but not both.</p>"""
    extended_statistics: NotRequired[
        "capo_cloudwatch.types.extended_statistics.ExtendedStatistics"
    ]
    """<p>The percentile statistics. Specify values between p0.0 and p100. When calling <code>GetMetricStatistics</code>, you must specify either <code>Statistics</code> or <code>ExtendedStatistics</code>, but not both. Percentile statistics are not available for metrics when any of the metric values are negative numbers.</p>"""
    unit: NotRequired["capo_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>The unit for a given metric. If you omit <code>Unit</code>, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricStatisticsInput) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        out["Dimensions"] = capo_cloudwatch.types.dimensions.serialize_aws_json_1_0(
            value["dimensions"]
        )
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        out["StartTime"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        out["EndTime"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["end_time"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "statistics" in value:
        import capo_cloudwatch.types.statistics

        out["Statistics"] = capo_cloudwatch.types.statistics.serialize_aws_json_1_0(
            value["statistics"]
        )
    if "extended_statistics" in value:
        import capo_cloudwatch.types.extended_statistics

        out["ExtendedStatistics"] = (
            capo_cloudwatch.types.extended_statistics.serialize_aws_json_1_0(
                value["extended_statistics"]
            )
        )
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricStatisticsInput:
    out: GetMetricStatisticsInput = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_aws_json_1_0(
            data["Dimensions"]
        )
    if data.get("StartTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["EndTime"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("Statistics") is not None:
        import capo_cloudwatch.types.statistics

        out["statistics"] = capo_cloudwatch.types.statistics.deserialize_aws_json_1_0(
            data["Statistics"]
        )
    if data.get("ExtendedStatistics") is not None:
        import capo_cloudwatch.types.extended_statistics

        out["extended_statistics"] = (
            capo_cloudwatch.types.extended_statistics.deserialize_aws_json_1_0(
                data["ExtendedStatistics"]
            )
        )
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricStatisticsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import capo_cloudwatch.types.dimensions

        capo_cloudwatch.types.dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "start_time" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "statistics" in value:
        import capo_cloudwatch.types.statistics

        capo_cloudwatch.types.statistics.serialize_query(
            value["statistics"], pairs, f"{key_prefix}Statistics"
        )
    if "extended_statistics" in value:
        import capo_cloudwatch.types.extended_statistics

        capo_cloudwatch.types.extended_statistics.serialize_query(
            value["extended_statistics"], pairs, f"{key_prefix}ExtendedStatistics"
        )
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        capo_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{key_prefix}Unit"
        )


def deserialize_query(el: Element) -> GetMetricStatisticsInput:
    out: GetMetricStatisticsInput = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_cloudwatch.types.dimensions

        out["dimensions"] = capo_cloudwatch.types.dimensions.deserialize_query(
            child_dimensions
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_cloudwatch.types.timestamp

        out["start_time"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_cloudwatch.types.timestamp

        out["end_time"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_end_time
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_statistics = el.find("Statistics")
    if child_statistics is not None:
        import capo_cloudwatch.types.statistics

        out["statistics"] = capo_cloudwatch.types.statistics.deserialize_query(
            child_statistics
        )
    child_extended_statistics = el.find("ExtendedStatistics")
    if child_extended_statistics is not None:
        import capo_cloudwatch.types.extended_statistics

        out["extended_statistics"] = (
            capo_cloudwatch.types.extended_statistics.deserialize_query(
                child_extended_statistics
            )
        )
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_query(child_unit)
    return out
