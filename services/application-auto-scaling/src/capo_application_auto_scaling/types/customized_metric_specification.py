"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#CustomizedMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_dimensions
    import capo_application_auto_scaling.types.metric_name
    import capo_application_auto_scaling.types.metric_namespace
    import capo_application_auto_scaling.types.metric_statistic
    import capo_application_auto_scaling.types.metric_unit
    import capo_application_auto_scaling.types.target_tracking_metric_data_queries


class CustomizedMetricSpecification(TypedDict, closed=True):
    metric_name: NotRequired[
        "capo_application_auto_scaling.types.metric_name.MetricName"
    ]
    """<p>The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html">Metric</a> object that's returned by a call to <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html">ListMetrics</a>.</p>"""
    namespace: NotRequired[
        "capo_application_auto_scaling.types.metric_namespace.MetricNamespace"
    ]
    """<p>The namespace of the metric.</p>"""
    dimensions: NotRequired[
        "capo_application_auto_scaling.types.metric_dimensions.MetricDimensions"
    ]
    """<p>The dimensions of the metric. </p> <p>Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.</p>"""
    statistic: NotRequired[
        "capo_application_auto_scaling.types.metric_statistic.MetricStatistic"
    ]
    """<p>The statistic of the metric.</p>"""
    unit: NotRequired["capo_application_auto_scaling.types.metric_unit.MetricUnit"]
    """<p>The unit of the metric. For a complete list of the units that CloudWatch supports, see the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html">MetricDatum</a> data type in the <i>Amazon CloudWatch API Reference</i>.</p>"""
    metrics: NotRequired[
        "capo_application_auto_scaling.types.target_tracking_metric_data_queries.TargetTrackingMetricDataQueries"
    ]
    """<p>The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizedMetricSpecification) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "dimensions" in value:
        import capo_application_auto_scaling.types.metric_dimensions

        out["Dimensions"] = (
            capo_application_auto_scaling.types.metric_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "statistic" in value:
        import capo_application_auto_scaling.types.metric_statistic

        out["Statistic"] = (
            capo_application_auto_scaling.types.metric_statistic.serialize_aws_json_1_1(
                value["statistic"]
            )
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "metrics" in value:
        import capo_application_auto_scaling.types.target_tracking_metric_data_queries

        out["Metrics"] = (
            capo_application_auto_scaling.types.target_tracking_metric_data_queries.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizedMetricSpecification:
    out: CustomizedMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("Dimensions") is not None:
        import capo_application_auto_scaling.types.metric_dimensions

        out["dimensions"] = (
            capo_application_auto_scaling.types.metric_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("Statistic") is not None:
        import capo_application_auto_scaling.types.metric_statistic

        out["statistic"] = (
            capo_application_auto_scaling.types.metric_statistic.deserialize_aws_json_1_1(
                data["Statistic"]
            )
        )
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    if data.get("Metrics") is not None:
        import capo_application_auto_scaling.types.target_tracking_metric_data_queries

        out["metrics"] = (
            capo_application_auto_scaling.types.target_tracking_metric_data_queries.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    return out
