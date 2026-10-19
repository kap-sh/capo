"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.event_type
    import capo_personalize.types.metric_expression
    import capo_personalize.types.metric_name


class MetricAttribute(TypedDict, closed=True):
    event_type: "capo_personalize.types.event_type.EventType"
    """<p>The metric's event type.</p>"""
    metric_name: "capo_personalize.types.metric_name.MetricName"
    """<p>The metric's name. The name helps you identify the metric in Amazon CloudWatch or Amazon S3.</p>"""
    expression: "capo_personalize.types.metric_expression.MetricExpression"
    """<p>The attribute's expression. Available functions are <code>SUM()</code> or <code>SAMPLECOUNT()</code>. For SUM() functions, provide the dataset type (either Interactions or Items) and column to sum as a parameter. For example SUM(Items.PRICE).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttribute) -> dict:
    out: dict = {}
    out["eventType"] = value["event_type"]
    out["metricName"] = value["metric_name"]
    out["expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricAttribute:
    out: MetricAttribute = {}  # type: ignore[typeddict-item]
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("metricName") is not None:
        out["metric_name"] = data["metricName"]
    else:
        out["metric_name"] = ""
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out
