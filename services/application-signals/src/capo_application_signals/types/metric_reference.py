"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.dimensions
    import capo_application_signals.types.metric_name
    import capo_application_signals.types.metric_type
    import capo_application_signals.types.namespace


class MetricReference(TypedDict, closed=True):
    namespace: "capo_application_signals.types.namespace.Namespace"
    """<p>The namespace of the metric. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace">CloudWatchNamespaces</a>.</p>"""
    metric_type: "capo_application_signals.types.metric_type.MetricType"
    """<p>Used to display the appropriate statistics in the CloudWatch console.</p>"""
    dimensions: NotRequired["capo_application_signals.types.dimensions.Dimensions"]
    """<p>An array of one or more dimensions that further define the metric. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension">CloudWatchDimensions</a>.</p>"""
    metric_name: "capo_application_signals.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    account_id: NotRequired[
        "capo_application_signals.types.aws_account_id.AwsAccountId"
    ]
    """<p>Amazon Web Services account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricReference) -> dict:
    out: dict = {}
    out["Namespace"] = value["namespace"]
    out["MetricType"] = value["metric_type"]
    if "dimensions" in value:
        import capo_application_signals.types.dimensions

        out["Dimensions"] = capo_application_signals.types.dimensions.serialize_json(
            value["dimensions"]
        )
    out["MetricName"] = value["metric_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> MetricReference:
    out: MetricReference = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError("MetricReference.namespace required")
    if data.get("MetricType") is not None:
        out["metric_type"] = data["MetricType"]
    else:
        raise DeserializationError("MetricReference.metric_type required")
    if data.get("Dimensions") is not None:
        import capo_application_signals.types.dimensions

        out["dimensions"] = capo_application_signals.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("MetricReference.metric_name required")
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
