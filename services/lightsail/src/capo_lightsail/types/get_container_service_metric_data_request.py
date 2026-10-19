"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServiceMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_metric_name
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic_list


class GetContainerServiceMetricDataRequest(TypedDict, closed=True):
    service_name: "capo_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to get metric data.</p>"""
    metric_name: (
        "capo_lightsail.types.container_service_metric_name.ContainerServiceMetricName"
    )
    """<p>The metric for which you want to return information.</p> <p>Valid container service metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.</p> <ul> <li> <p> <code>CPUUtilization</code> - The average percentage of compute units that are currently in use across all nodes of the container service. This metric identifies the processing power required to run containers on each node of the container service.</p> <p>Statistics: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p>Unit: The published unit is <code>Percent</code>.</p> </li> <li> <p> <code>MemoryUtilization</code> - The average percentage of available memory that is currently in use across all nodes of the container service. This metric identifies the memory required to run containers on each node of the container service.</p> <p>Statistics: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p>Unit: The published unit is <code>Percent</code>.</p> </li> </ul>"""
    start_time: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The start time of the time period.</p>"""
    end_time: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The end time of the time period.</p>"""
    period: "capo_lightsail.types.metric_period.MetricPeriod"
    """<p>The granularity, in seconds, of the returned data points.</p> <p>All container service metric data is available in 5-minute (300 seconds) granularity.</p>"""
    statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList"
    """<p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of <code>Sum</code> / <code>SampleCount</code> during the specified period. By comparing this statistic with the <code>Minimum</code> and <code>Maximum</code> values, you can determine the full scope of a metric and how close the average use is to the <code>Minimum</code> and <code>Maximum</code> values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServiceMetricDataRequest) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    import capo_lightsail.types.container_service_metric_name

    out["metricName"] = (
        capo_lightsail.types.container_service_metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    )
    import capo_lightsail.types.iso_date

    out["startTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_lightsail.types.iso_date

    out["endTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["end_time"]
    )
    out["period"] = value["period"]
    import capo_lightsail.types.metric_statistic_list

    out["statistics"] = (
        capo_lightsail.types.metric_statistic_list.serialize_aws_json_1_1(
            value["statistics"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServiceMetricDataRequest:
    out: GetContainerServiceMetricDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    else:
        out["service_name"] = ""
    if data.get("metricName") is not None:
        import capo_lightsail.types.container_service_metric_name

        out["metric_name"] = (
            capo_lightsail.types.container_service_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    else:
        import typing

        out["metric_name"] = typing.cast(
            "capo_lightsail.types.container_service_metric_name.ContainerServiceMetricName",
            "",
        )
    if data.get("startTime") is not None:
        import capo_lightsail.types.iso_date

        out["start_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_lightsail.types.iso_date

        out["end_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        out["period"] = 0
    if data.get("statistics") is not None:
        import capo_lightsail.types.metric_statistic_list

        out["statistics"] = (
            capo_lightsail.types.metric_statistic_list.deserialize_aws_json_1_1(
                data["statistics"]
            )
        )
    else:
        out["statistics"] = []
    return out
