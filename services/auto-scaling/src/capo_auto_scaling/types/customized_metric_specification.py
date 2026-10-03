"""Generated from Smithy shape ``com.amazonaws.autoscaling#CustomizedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_dimensions
    import capo_auto_scaling.types.metric_granularity_in_seconds
    import capo_auto_scaling.types.metric_name
    import capo_auto_scaling.types.metric_namespace
    import capo_auto_scaling.types.metric_statistic
    import capo_auto_scaling.types.metric_unit
    import capo_auto_scaling.types.target_tracking_metric_data_queries


class CustomizedMetricSpecification(TypedDict, closed=True):
    metric_name: NotRequired["capo_auto_scaling.types.metric_name.MetricName"]
    """<p>The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html">Metric</a> object that is returned by a call to <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html">ListMetrics</a>.</p>"""
    namespace: NotRequired["capo_auto_scaling.types.metric_namespace.MetricNamespace"]
    """<p>The namespace of the metric.</p>"""
    dimensions: NotRequired[
        "capo_auto_scaling.types.metric_dimensions.MetricDimensions"
    ]
    """<p>The dimensions of the metric.</p> <p>Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.</p>"""
    statistic: NotRequired["capo_auto_scaling.types.metric_statistic.MetricStatistic"]
    """<p>The statistic of the metric.</p>"""
    unit: NotRequired["capo_auto_scaling.types.metric_unit.MetricUnit"]
    """<p>The unit of the metric. For a complete list of the units that CloudWatch supports, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html">MetricDatum</a> data type in the <i>Amazon CloudWatch API Reference</i>.</p>"""
    period: NotRequired[
        "capo_auto_scaling.types.metric_granularity_in_seconds.MetricGranularityInSeconds"
    ]
    """<p> The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html">Create a target tracking policy using high-resolution metrics for faster response</a>. </p>"""
    metrics: NotRequired[
        "capo_auto_scaling.types.target_tracking_metric_data_queries.TargetTrackingMetricDataQueries"
    ]
    """<p>The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomizedMetricSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "dimensions" in value:
        import capo_auto_scaling.types.metric_dimensions

        capo_auto_scaling.types.metric_dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )
    if "statistic" in value:
        import capo_auto_scaling.types.metric_statistic

        capo_auto_scaling.types.metric_statistic.serialize_query(
            value["statistic"], pairs, f"{key_prefix}Statistic"
        )
    if "unit" in value:
        pairs.append((f"{key_prefix}Unit", str(value["unit"])))
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "metrics" in value:
        import capo_auto_scaling.types.target_tracking_metric_data_queries

        capo_auto_scaling.types.target_tracking_metric_data_queries.serialize_query(
            value["metrics"], pairs, f"{key_prefix}Metrics"
        )


def deserialize_query(el: Element) -> CustomizedMetricSpecification:
    out: CustomizedMetricSpecification = {}  # type: ignore[typeddict-item]
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_auto_scaling.types.metric_dimensions

        out["dimensions"] = capo_auto_scaling.types.metric_dimensions.deserialize_query(
            child_dimensions
        )
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import capo_auto_scaling.types.metric_statistic

        out["statistic"] = capo_auto_scaling.types.metric_statistic.deserialize_query(
            child_statistic
        )
    child_unit = el.find("Unit")
    if child_unit is not None:
        out["unit"] = str(child_unit.text or "")
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_metrics = el.find("Metrics")
    if child_metrics is not None:
        import capo_auto_scaling.types.target_tracking_metric_data_queries

        out["metrics"] = (
            capo_auto_scaling.types.target_tracking_metric_data_queries.deserialize_query(
                child_metrics
            )
        )
    return out
