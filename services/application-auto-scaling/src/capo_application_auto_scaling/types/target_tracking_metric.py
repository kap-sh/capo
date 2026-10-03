"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TargetTrackingMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.target_tracking_metric_dimensions
    import capo_application_auto_scaling.types.target_tracking_metric_name
    import capo_application_auto_scaling.types.target_tracking_metric_namespace


class TargetTrackingMetric(TypedDict, closed=True):
    dimensions: NotRequired[
        "capo_application_auto_scaling.types.target_tracking_metric_dimensions.TargetTrackingMetricDimensions"
    ]
    """<p>The dimensions for the metric. For the list of available dimensions, see the Amazon Web Services documentation available from the table in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html">Amazon Web Services services that publish CloudWatch metrics </a> in the <i>Amazon CloudWatch User Guide</i>. </p> <p>Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.</p>"""
    metric_name: NotRequired[
        "capo_application_auto_scaling.types.target_tracking_metric_name.TargetTrackingMetricName"
    ]
    """<p>The name of the metric.</p>"""
    namespace: NotRequired[
        "capo_application_auto_scaling.types.target_tracking_metric_namespace.TargetTrackingMetricNamespace"
    ]
    """<p>The namespace of the metric. For more information, see the table in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html">Amazon Web Services services that publish CloudWatch metrics </a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingMetric) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_application_auto_scaling.types.target_tracking_metric_dimensions

        out["Dimensions"] = (
            capo_application_auto_scaling.types.target_tracking_metric_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingMetric:
    out: TargetTrackingMetric = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_application_auto_scaling.types.target_tracking_metric_dimensions

        out["dimensions"] = (
            capo_application_auto_scaling.types.target_tracking_metric_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    return out
