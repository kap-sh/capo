"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic_list
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.relational_database_metric_name
    import capo_lightsail.types.resource_name


class GetRelationalDatabaseMetricDataRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database from which to get metric data.</p>"""
    metric_name: "capo_lightsail.types.relational_database_metric_name.RelationalDatabaseMetricName"
    """<p>The metric for which you want to return information.</p> <p>Valid relational database metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value. All relational database metric data is available in 1-minute (60 seconds) granularity.</p> <ul> <li> <p> <b> <code>CPUUtilization</code> </b> - The percentage of CPU utilization currently in use on the database.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>DatabaseConnections</code> </b> - The number of database connections in use.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>DiskQueueDepth</code> </b> - The number of outstanding IOs (read/write requests) that are waiting to access the disk.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>FreeStorageSpace</code> </b> - The amount of available storage space.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>NetworkReceiveThroughput</code> </b> - The incoming (Receive) network traffic on the database, including both customer database traffic and AWS traffic used for monitoring and replication.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes/Second</code>.</p> </li> <li> <p> <b> <code>NetworkTransmitThroughput</code> </b> - The outgoing (Transmit) network traffic on the database, including both customer database traffic and AWS traffic used for monitoring and replication.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes/Second</code>.</p> </li> </ul>"""
    period: "capo_lightsail.types.metric_period.MetricPeriod"
    """<p>The granularity, in seconds, of the returned data points.</p> <p>All relational database metric data is available in 1-minute (60 seconds) granularity.</p>"""
    start_time: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The start of the time interval from which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the start time.</p> </li> </ul>"""
    end_time: "capo_lightsail.types.iso_date.IsoDate"
    """<p>The end of the time interval from which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the end time.</p> </li> </ul>"""
    unit: "capo_lightsail.types.metric_unit.MetricUnit"
    """<p>The unit for the metric data request. Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>"""
    statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList"
    """<p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseMetricDataRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    import capo_lightsail.types.relational_database_metric_name

    out["metricName"] = (
        capo_lightsail.types.relational_database_metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    )
    out["period"] = value["period"]
    import capo_lightsail.types.iso_date

    out["startTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_lightsail.types.iso_date

    out["endTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
        value["end_time"]
    )
    import capo_lightsail.types.metric_unit

    out["unit"] = capo_lightsail.types.metric_unit.serialize_aws_json_1_1(value["unit"])
    import capo_lightsail.types.metric_statistic_list

    out["statistics"] = (
        capo_lightsail.types.metric_statistic_list.serialize_aws_json_1_1(
            value["statistics"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseMetricDataRequest:
    out: GetRelationalDatabaseMetricDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        out["relational_database_name"] = ""
    if data.get("metricName") is not None:
        import capo_lightsail.types.relational_database_metric_name

        out["metric_name"] = (
            capo_lightsail.types.relational_database_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    else:
        import typing

        out["metric_name"] = typing.cast(
            "capo_lightsail.types.relational_database_metric_name.RelationalDatabaseMetricName",
            "",
        )
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        out["period"] = 0
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
    if data.get("unit") is not None:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast("capo_lightsail.types.metric_unit.MetricUnit", "")
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
