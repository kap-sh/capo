"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric
    import capo_auto_scaling.types.metric_unit
    import capo_auto_scaling.types.xml_string_metric_stat


class MetricStat(TypedDict, closed=True):
    metric: NotRequired["capo_auto_scaling.types.metric.Metric"]
    """<p>The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html">Metric</a> object that is returned by a call to <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html">ListMetrics</a>.</p>"""
    stat: NotRequired[
        "capo_auto_scaling.types.xml_string_metric_stat.XmlStringMetricStat"
    ]
    """<p>The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic">Statistics</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>The most commonly used metrics for predictive scaling are <code>Average</code> and <code>Sum</code>.</p>"""
    unit: NotRequired["capo_auto_scaling.types.metric_unit.MetricUnit"]
    """<p>The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html">MetricDatum</a> data type in the <i>Amazon CloudWatch API Reference</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric" in value:
        import capo_auto_scaling.types.metric

        capo_auto_scaling.types.metric.serialize_query(
            value["metric"], pairs, f"{key_prefix}Metric"
        )
    if "stat" in value:
        pairs.append((f"{key_prefix}Stat", str(value["stat"])))
    if "unit" in value:
        pairs.append((f"{key_prefix}Unit", str(value["unit"])))


def deserialize_query(el: Element) -> MetricStat:
    out: MetricStat = {}  # type: ignore[typeddict-item]
    child_metric = el.find("Metric")
    if child_metric is not None:
        import capo_auto_scaling.types.metric

        out["metric"] = capo_auto_scaling.types.metric.deserialize_query(child_metric)
    child_stat = el.find("Stat")
    if child_stat is not None:
        out["stat"] = str(child_stat.text or "")
    child_unit = el.find("Unit")
    if child_unit is not None:
        out["unit"] = str(child_unit.text or "")
    return out
