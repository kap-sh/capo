"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric
    import capo_cloudwatch.types.period
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.stat


class MetricStat(TypedDict, closed=True):
    metric: NotRequired["capo_cloudwatch.types.metric.Metric"]
    """<p>The metric to return, including the metric name, namespace, and dimensions.</p>"""
    period: NotRequired["capo_cloudwatch.types.period.Period"]
    """<p>The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a <code>PutMetricData</code> call that includes a <code>StorageResolution</code> of 1 second.</p> <p>If the <code>StartTime</code> parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:</p> <ul> <li> <p>Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).</p> </li> <li> <p>Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).</p> </li> <li> <p>Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).</p> </li> </ul>"""
    stat: NotRequired["capo_cloudwatch.types.stat.Stat"]
    """<p>The statistic to return. It can include any CloudWatch statistic or extended statistic.</p>"""
    unit: NotRequired["capo_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>When you are using a <code>Put</code> operation, this defines what unit you want to use when storing the metric.</p> <p>In a <code>Get</code> operation, if you omit <code>Unit</code> then all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStat) -> dict:
    out: dict = {}
    if "metric" in value:
        import capo_cloudwatch.types.metric

        out["Metric"] = capo_cloudwatch.types.metric.serialize_aws_json_1_0(
            value["metric"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricStat:
    out: MetricStat = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        import capo_cloudwatch.types.metric

        out["metric"] = capo_cloudwatch.types.metric.deserialize_aws_json_1_0(
            data["Metric"]
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("Stat") is not None:
        out["stat"] = data["Stat"]
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric" in value:
        import capo_cloudwatch.types.metric

        capo_cloudwatch.types.metric.serialize_query(
            value["metric"], pairs, f"{key_prefix}Metric"
        )
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "stat" in value:
        pairs.append((f"{key_prefix}Stat", str(value["stat"])))
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        capo_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{key_prefix}Unit"
        )


def deserialize_query(el: Element) -> MetricStat:
    out: MetricStat = {}  # type: ignore[typeddict-item]
    child_metric = el.find("Metric")
    if child_metric is not None:
        import capo_cloudwatch.types.metric

        out["metric"] = capo_cloudwatch.types.metric.deserialize_query(child_metric)
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_stat = el.find("Stat")
    if child_stat is not None:
        out["stat"] = str(child_stat.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_query(child_unit)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStat) -> dict:
    out: dict = {}
    if "metric" in value:
        import capo_cloudwatch.types.metric

        out["Metric"] = capo_cloudwatch.types.metric.serialize_cbor(value["metric"])
    if "period" in value:
        out["Period"] = value["period"]
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_cbor(value["unit"])
    return out


def deserialize_cbor(data: dict) -> MetricStat:
    out: MetricStat = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        import capo_cloudwatch.types.metric

        out["metric"] = capo_cloudwatch.types.metric.deserialize_cbor(data["Metric"])
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    if data.get("Stat") is not None:
        out["stat"] = data["Stat"]
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_cbor(data["Unit"])
    return out
