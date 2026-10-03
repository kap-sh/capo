"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.distribution_metric_name
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic_list
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.timestamp


class GetDistributionMetricDataRequest(TypedDict, closed=True):
    distribution_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the distribution for which to get metric data.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""
    metric_name: "capo_lightsail.types.distribution_metric_name.DistributionMetricName"
    """<p>The metric for which you want to return information.</p> <p>Valid distribution metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value.</p> <ul> <li> <p> <b> <code>Requests</code> </b> - The total number of viewer requests received by your Lightsail distribution, for all HTTP methods, and for both HTTP and HTTPS requests.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>None</code>.</p> </li> <li> <p> <b> <code>BytesDownloaded</code> </b> - The number of bytes downloaded by viewers for GET, HEAD, and OPTIONS requests.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>None</code>.</p> </li> <li> <p> <b> <code>BytesUploaded </code> </b> - The number of bytes uploaded to your origin by your Lightsail distribution, using POST and PUT requests.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>None</code>.</p> </li> <li> <p> <b> <code>TotalErrorRate</code> </b> - The percentage of all viewer requests for which the response's HTTP status code was 4xx or 5xx.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>4xxErrorRate</code> </b> - The percentage of all viewer requests for which the response's HTTP status cod was 4xx. In these cases, the client or client viewer may have made an error. For example, a status code of 404 (Not Found) means that the client requested an object that could not be found.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>5xxErrorRate</code> </b> - The percentage of all viewer requests for which the response's HTTP status code was 5xx. In these cases, the origin server did not satisfy the requests. For example, a status code of 503 (Service Unavailable) means that the origin server is currently unavailable.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> </ul>"""
    start_time: "capo_lightsail.types.timestamp.timestamp"
    """<p>The start of the time interval for which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>"""
    end_time: "capo_lightsail.types.timestamp.timestamp"
    """<p>The end of the time interval for which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>"""
    period: "capo_lightsail.types.metric_period.MetricPeriod"
    """<p>The granularity, in seconds, for the metric data points that will be returned.</p>"""
    unit: "capo_lightsail.types.metric_unit.MetricUnit"
    """<p>The unit for the metric data request.</p> <p>Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>"""
    statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList"
    """<p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionMetricDataRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    import capo_lightsail.types.distribution_metric_name

    out["metricName"] = (
        capo_lightsail.types.distribution_metric_name.serialize_aws_json_1_1(
            value["metric_name"]
        )
    )
    import capo_lightsail.types.timestamp

    out["startTime"] = capo_lightsail.types.timestamp.serialize_aws_json_1_1(
        value["start_time"]
    )
    import capo_lightsail.types.timestamp

    out["endTime"] = capo_lightsail.types.timestamp.serialize_aws_json_1_1(
        value["end_time"]
    )
    out["period"] = value["period"]
    import capo_lightsail.types.metric_unit

    out["unit"] = capo_lightsail.types.metric_unit.serialize_aws_json_1_1(value["unit"])
    import capo_lightsail.types.metric_statistic_list

    out["statistics"] = (
        capo_lightsail.types.metric_statistic_list.serialize_aws_json_1_1(
            value["statistics"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionMetricDataRequest:
    out: GetDistributionMetricDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("distributionName") is not None:
        out["distribution_name"] = data["distributionName"]
    else:
        raise DeserializationError(
            "GetDistributionMetricDataRequest.distribution_name required"
        )
    if data.get("metricName") is not None:
        import capo_lightsail.types.distribution_metric_name

        out["metric_name"] = (
            capo_lightsail.types.distribution_metric_name.deserialize_aws_json_1_1(
                data["metricName"]
            )
        )
    else:
        raise DeserializationError(
            "GetDistributionMetricDataRequest.metric_name required"
        )
    if data.get("startTime") is not None:
        import capo_lightsail.types.timestamp

        out["start_time"] = capo_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    else:
        raise DeserializationError(
            "GetDistributionMetricDataRequest.start_time required"
        )
    if data.get("endTime") is not None:
        import capo_lightsail.types.timestamp

        out["end_time"] = capo_lightsail.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    else:
        raise DeserializationError("GetDistributionMetricDataRequest.end_time required")
    if data.get("period") is not None:
        out["period"] = data["period"]
    else:
        raise DeserializationError("GetDistributionMetricDataRequest.period required")
    if data.get("unit") is not None:
        import capo_lightsail.types.metric_unit

        out["unit"] = capo_lightsail.types.metric_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    else:
        raise DeserializationError("GetDistributionMetricDataRequest.unit required")
    if data.get("statistics") is not None:
        import capo_lightsail.types.metric_statistic_list

        out["statistics"] = (
            capo_lightsail.types.metric_statistic_list.deserialize_aws_json_1_1(
                data["statistics"]
            )
        )
    else:
        raise DeserializationError(
            "GetDistributionMetricDataRequest.statistics required"
        )
    return out
