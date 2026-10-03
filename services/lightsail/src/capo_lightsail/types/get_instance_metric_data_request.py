"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.instance_metric_name
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic_list
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.timestamp


class GetInstanceMetricDataRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance for which you want to get metrics data.</p>"""
    metric_name: "capo_lightsail.types.instance_metric_name.InstanceMetricName"
    """<p>The metric for which you want to return information.</p> <p>Valid instance metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value.</p> <ul> <li> <p> <b> <code>BurstCapacityPercentage</code> </b> - The percentage of CPU performance available for your instance to burst above its baseline. Your instance continuously accrues and consumes burst capacity. Burst capacity stops accruing when your instance's <code>BurstCapacityPercentage</code> reaches 100%. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-burst-capacity">Viewing instance burst capacity in Amazon Lightsail</a>.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>BurstCapacityTime</code> </b> - The available amount of time for your instance to burst at 100% CPU utilization. Your instance continuously accrues and consumes burst capacity. Burst capacity time stops accruing when your instance's <code>BurstCapacityPercentage</code> metric reaches 100%.</p> <p>Burst capacity time is consumed at the full rate only when your instance operates at 100% CPU utilization. For example, if your instance operates at 50% CPU utilization in the burstable zone for a 5-minute period, then it consumes CPU burst capacity minutes at a 50% rate in that period. Your instance consumed 2 minutes and 30 seconds of CPU burst capacity minutes in the 5-minute period. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-burst-capacity">Viewing instance burst capacity in Amazon Lightsail</a>.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Seconds</code>.</p> </li> <li> <p> <b> <code>CPUUtilization</code> </b> - The percentage of allocated compute units that are currently in use on the instance. This metric identifies the processing power to run the applications on the instance. Tools in your operating system can show a lower percentage than Lightsail when the instance is not allocated a full processor core.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>NetworkIn</code> </b> - The number of bytes received on all network interfaces by the instance. This metric identifies the volume of incoming network traffic to the instance. The number reported is the number of bytes received during the period. Because this metric is reported in 5-minute intervals, divide the reported number by 300 to find Bytes/second.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>NetworkOut</code> </b> - The number of bytes sent out on all network interfaces by the instance. This metric identifies the volume of outgoing network traffic from the instance. The number reported is the number of bytes sent during the period. Because this metric is reported in 5-minute intervals, divide the reported number by 300 to find Bytes/second.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>StatusCheckFailed</code> </b> - Reports whether the instance passed or failed both the instance status check and the system status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>StatusCheckFailed_Instance</code> </b> - Reports whether the instance passed or failed the instance status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>StatusCheckFailed_System</code> </b> - Reports whether the instance passed or failed the system status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>MetadataNoToken</code> </b> - Reports the number of times that the instance metadata service was successfully accessed without a token. This metric determines if there are any processes accessing instance metadata by using Instance Metadata Service Version 1, which doesn't use a token. If all requests use token-backed sessions, such as Instance Metadata Service Version 2, then the value is 0.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> </ul>"""
    period: "capo_lightsail.types.metric_period.MetricPeriod"
    """<p>The granularity, in seconds, of the returned data points.</p> <p>The <code>StatusCheckFailed</code>, <code>StatusCheckFailed_Instance</code>, and <code>StatusCheckFailed_System</code> instance metric data is available in 1-minute (60 seconds) granularity. All other instance metric data is available in 5-minute (300 seconds) granularity.</p>"""
    start_time: "capo_lightsail.types.timestamp.timestamp"
    """<p>The start time of the time period.</p>"""
    end_time: "capo_lightsail.types.timestamp.timestamp"
    """<p>The end time of the time period.</p>"""
    unit: "capo_lightsail.types.metric_unit.MetricUnit"
    """<p>The unit for the metric data request. Valid units depend on the metric data being requested. For the valid units to specify with each available metric, see the <code>metricName</code> parameter.</p>"""
    statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList"
    """<p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceMetricDataRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    import capo_lightsail.types.instance_metric_name

    out["metricName"] = (
        capo_lightsail.types.instance_metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    )
    out["period"] = value["period"]
    import capo_lightsail.types.timestamp

    out["startTime"] = capo_lightsail.types.timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_lightsail.types.timestamp

    out["endTime"] = capo_lightsail.types.timestamp.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> GetInstanceMetricDataRequest:
    out: GetInstanceMetricDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError(
            "GetInstanceMetricDataRequest.instance_name required"
        )
    if data.get("metricName") is not None:
        import capo_lightsail.types.instance_metric_name

        out["metric_name"] = (
            capo_lightsail.types.instance_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    else:
        raise DeserializationError("GetInstanceMetricDataRequest.metric_name required")
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        raise DeserializationError("GetInstanceMetricDataRequest.period required")
    if data.get("startTime") is not None:
        import capo_lightsail.types.timestamp

        out["start_time"] = capo_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    else:
        raise DeserializationError("GetInstanceMetricDataRequest.start_time required")
    if data.get("endTime") is not None:
        import capo_lightsail.types.timestamp

        out["end_time"] = capo_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    else:
        raise DeserializationError("GetInstanceMetricDataRequest.end_time required")
    if data.get("unit") is not None:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    else:
        raise DeserializationError("GetInstanceMetricDataRequest.unit required")
    if data.get("statistics") is not None:
        import capo_lightsail.types.metric_statistic_list

        out["statistics"] = (
            capo_lightsail.types.metric_statistic_list.deserialize_aws_json_1_1(
                data["statistics"]
            )
        )
    else:
        raise DeserializationError("GetInstanceMetricDataRequest.statistics required")
    return out
