"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricTransformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.default_value
    import capo_cloudwatch_logs.types.dimensions
    import capo_cloudwatch_logs.types.metric_name
    import capo_cloudwatch_logs.types.metric_namespace
    import capo_cloudwatch_logs.types.metric_value
    import capo_cloudwatch_logs.types.standard_unit


class MetricTransformation(TypedDict, closed=True):
    metric_name: "capo_cloudwatch_logs.types.metric_name.MetricName"
    """<p>The name of the CloudWatch metric.</p>"""
    metric_namespace: "capo_cloudwatch_logs.types.metric_namespace.MetricNamespace"
    """<p>A custom namespace to contain your metric in CloudWatch. Use namespaces to group together metrics that are similar. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace">Namespaces</a>.</p>"""
    metric_value: "capo_cloudwatch_logs.types.metric_value.MetricValue"
    """<p>The value to publish to the CloudWatch metric when a filter pattern matches a log event.</p>"""
    default_value: NotRequired["capo_cloudwatch_logs.types.default_value.DefaultValue"]
    """<p>(Optional) The value to emit when a filter pattern does not match a log event. This value can be null.</p>"""
    dimensions: NotRequired["capo_cloudwatch_logs.types.dimensions.Dimensions"]
    """<p>The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions.</p> <important> <p>Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as <code>IPAddress</code> or <code>requestID</code> as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric. </p> <p>CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.</p> <p>You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html"> Creating a Billing Alarm to Monitor Your Estimated Amazon Web Services Charges</a>. </p> </important>"""
    unit: NotRequired["capo_cloudwatch_logs.types.standard_unit.StandardUnit"]
    """<p>The unit to assign to the metric. If you omit this, the unit is set as <code>None</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricTransformation) -> dict:
    out: dict = {}
    out["metricName"] = value["metric_name"]
    out["metricNamespace"] = value["metric_namespace"]
    out["metricValue"] = value["metric_value"]
    if "default_value" in value:
        out["defaultValue"] = (
            "NaN"
            if value["default_value"] != value["default_value"]
            else "Infinity"
            if value["default_value"] == float("inf")
            else "-Infinity"
            if value["default_value"] == float("-inf")
            else value["default_value"]
        )
    if "dimensions" in value:
        import capo_cloudwatch_logs.types.dimensions

        out["dimensions"] = (
            capo_cloudwatch_logs.types.dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    if "unit" in value:
        import capo_cloudwatch_logs.types.standard_unit

        out["unit"] = capo_cloudwatch_logs.types.standard_unit.serialize_aws_json_1_1(
            value["unit"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricTransformation:
    out: MetricTransformation = {}  # type: ignore[typeddict-item]
    if data.get("metricName") is not None:
        out["metric_name"] = data["metricName"]
    else:
        raise DeserializationError("MetricTransformation.metric_name required")
    if data.get("metricNamespace") is not None:
        out["metric_namespace"] = data["metricNamespace"]
    else:
        raise DeserializationError("MetricTransformation.metric_namespace required")
    if data.get("metricValue") is not None:
        out["metric_value"] = data["metricValue"]
    else:
        raise DeserializationError("MetricTransformation.metric_value required")
    if data.get("defaultValue") is not None:
        out["default_value"] = float(data["defaultValue"])
    if data.get("dimensions") is not None:
        import capo_cloudwatch_logs.types.dimensions

        out["dimensions"] = (
            capo_cloudwatch_logs.types.dimensions.deserialize_aws_json_1_1(
                data["dimensions"]
            )
        )
    if data.get("unit") is not None:
        import capo_cloudwatch_logs.types.standard_unit

        out["unit"] = capo_cloudwatch_logs.types.standard_unit.deserialize_aws_json_1_1(
            data["unit"]
        )
    return out
