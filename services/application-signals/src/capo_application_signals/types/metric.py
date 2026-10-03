"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Metric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.dimensions
    import capo_application_signals.types.metric_name
    import capo_application_signals.types.namespace


class Metric(TypedDict, closed=True):
    namespace: NotRequired["capo_application_signals.types.namespace.Namespace"]
    """<p>The namespace of the metric. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace">Namespaces</a>.</p>"""
    metric_name: NotRequired["capo_application_signals.types.metric_name.MetricName"]
    """<p>The name of the metric to use.</p>"""
    dimensions: NotRequired["capo_application_signals.types.dimensions.Dimensions"]
    """<p>An array of one or more dimensions to use to define the metric that you want to use. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension">Dimensions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Metric) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "dimensions" in value:
        import capo_application_signals.types.dimensions

        out["Dimensions"] = capo_application_signals.types.dimensions.serialize_json(
            value["dimensions"]
        )
    return out


def deserialize_json(data: dict) -> Metric:
    out: Metric = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Dimensions") is not None:
        import capo_application_signals.types.dimensions

        out["dimensions"] = capo_application_signals.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    return out
