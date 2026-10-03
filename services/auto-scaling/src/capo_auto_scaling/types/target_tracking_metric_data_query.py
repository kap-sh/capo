"""Generated from Smithy shape ``com.amazonaws.autoscaling#TargetTrackingMetricDataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_granularity_in_seconds
    import capo_auto_scaling.types.return_data
    import capo_auto_scaling.types.target_tracking_metric_stat
    import capo_auto_scaling.types.xml_string_max_len64
    import capo_auto_scaling.types.xml_string_max_len2047
    import capo_auto_scaling.types.xml_string_metric_label


class TargetTrackingMetricDataQuery(TypedDict, closed=True):
    id: NotRequired["capo_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"]
    """<p>A short name that identifies the object's results in the response. This name must be unique among all <code>TargetTrackingMetricDataQuery</code> objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter. </p>"""
    expression: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len2047.XmlStringMaxLen2047"
    ]
    """<p>The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the <code>Id</code> of the other metrics to refer to those metrics, and can also use the <code>Id</code> of other expressions to use the result of those expressions. </p> <p>Conditional: Within each <code>TargetTrackingMetricDataQuery</code> object, you must specify either <code>Expression</code> or <code>MetricStat</code>, but not both.</p>"""
    metric_stat: NotRequired[
        "capo_auto_scaling.types.target_tracking_metric_stat.TargetTrackingMetricStat"
    ]
    """<p>Information about the metric data to return.</p> <p>Conditional: Within each <code>TargetTrackingMetricDataQuery</code> object, you must specify either <code>Expression</code> or <code>MetricStat</code>, but not both.</p>"""
    label: NotRequired[
        "capo_auto_scaling.types.xml_string_metric_label.XmlStringMetricLabel"
    ]
    """<p>A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.</p>"""
    period: NotRequired[
        "capo_auto_scaling.types.metric_granularity_in_seconds.MetricGranularityInSeconds"
    ]
    """<p> The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html">Create a target tracking policy using high-resolution metrics for faster response</a>. </p>"""
    return_data: NotRequired["capo_auto_scaling.types.return_data.ReturnData"]
    """<p>Indicates whether to return the timestamps and raw data values of this metric. </p> <p>If you use any math expressions, specify <code>true</code> for this value for only the final math expression that the metric specification is based on. You must specify <code>false</code> for <code>ReturnData</code> for all the other metrics and expressions used in the metric specification.</p> <p>If you are only retrieving metrics and not performing any math expressions, do not specify anything for <code>ReturnData</code>. This sets it to its default (<code>true</code>).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetTrackingMetricDataQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "expression" in value:
        pairs.append((f"{key_prefix}Expression", str(value["expression"])))
    if "metric_stat" in value:
        import capo_auto_scaling.types.target_tracking_metric_stat

        capo_auto_scaling.types.target_tracking_metric_stat.serialize_query(
            value["metric_stat"], pairs, f"{key_prefix}MetricStat"
        )
    if "label" in value:
        pairs.append((f"{key_prefix}Label", str(value["label"])))
    if "period" in value:
        pairs.append((f"{key_prefix}Period", str(value["period"])))
    if "return_data" in value:
        pairs.append(
            (f"{key_prefix}ReturnData", "true" if value["return_data"] else "false")
        )


def deserialize_query(el: Element) -> TargetTrackingMetricDataQuery:
    out: TargetTrackingMetricDataQuery = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_expression = el.find("Expression")
    if child_expression is not None:
        out["expression"] = str(child_expression.text or "")
    child_metric_stat = el.find("MetricStat")
    if child_metric_stat is not None:
        import capo_auto_scaling.types.target_tracking_metric_stat

        out["metric_stat"] = (
            capo_auto_scaling.types.target_tracking_metric_stat.deserialize_query(
                child_metric_stat
            )
        )
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    child_return_data = el.find("ReturnData")
    if child_return_data is not None:
        out["return_data"] = (child_return_data.text or "").lower() == "true"
    return out
