"""Generated from Smithy shape ``com.amazonaws.autoscaling#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_dimensions
    import capo_auto_scaling.types.metric_name
    import capo_auto_scaling.types.metric_namespace


class Metric(TypedDict, closed=True):
    namespace: NotRequired["capo_auto_scaling.types.metric_namespace.MetricNamespace"]
    """<p>The namespace of the metric. For more information, see the table in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html">Amazon Web Services services that publish CloudWatch metrics </a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""
    metric_name: NotRequired["capo_auto_scaling.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    dimensions: NotRequired[
        "capo_auto_scaling.types.metric_dimensions.MetricDimensions"
    ]
    """<p>The dimensions for the metric. For the list of available dimensions, see the Amazon Web Services documentation available from the table in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html">Amazon Web Services services that publish CloudWatch metrics </a> in the <i>Amazon CloudWatch User Guide</i>. </p> <p>Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Metric, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_name" in value:
        pairs.append((f"{key_prefix}MetricName", str(value["metric_name"])))
    if "dimensions" in value:
        import capo_auto_scaling.types.metric_dimensions

        capo_auto_scaling.types.metric_dimensions.serialize_query(
            value["dimensions"], pairs, f"{key_prefix}Dimensions"
        )


def deserialize_query(el: Element) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_auto_scaling.types.metric_dimensions

        out["dimensions"] = capo_auto_scaling.types.metric_dimensions.deserialize_query(
            child_dimensions
        )
    return out
