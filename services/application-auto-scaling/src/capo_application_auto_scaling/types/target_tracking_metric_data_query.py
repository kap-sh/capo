"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TargetTrackingMetricDataQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.expression
    import capo_application_auto_scaling.types.id
    import capo_application_auto_scaling.types.return_data
    import capo_application_auto_scaling.types.target_tracking_metric_stat
    import capo_application_auto_scaling.types.xml_string


class TargetTrackingMetricDataQuery(TypedDict, closed=True):
    expression: NotRequired["capo_application_auto_scaling.types.expression.Expression"]
    """<p>The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the <code>Id</code> of the other metrics to refer to those metrics, and can also use the <code>Id</code> of other expressions to use the result of those expressions. </p> <p>Conditional: Within each <code>TargetTrackingMetricDataQuery</code> object, you must specify either <code>Expression</code> or <code>MetricStat</code>, but not both.</p>"""
    id: "capo_application_auto_scaling.types.id.Id"
    """<p>A short name that identifies the object's results in the response. This name must be unique among all <code>MetricDataQuery</code> objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter. </p>"""
    label: NotRequired["capo_application_auto_scaling.types.xml_string.XmlString"]
    """<p>A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.</p>"""
    metric_stat: NotRequired[
        "capo_application_auto_scaling.types.target_tracking_metric_stat.TargetTrackingMetricStat"
    ]
    """<p>Information about the metric data to return.</p> <p>Conditional: Within each <code>MetricDataQuery</code> object, you must specify either <code>Expression</code> or <code>MetricStat</code>, but not both.</p>"""
    return_data: NotRequired[
        "capo_application_auto_scaling.types.return_data.ReturnData"
    ]
    """<p>Indicates whether to return the timestamps and raw data values of this metric. </p> <p>If you use any math expressions, specify <code>true</code> for this value for only the final math expression that the metric specification is based on. You must specify <code>false</code> for <code>ReturnData</code> for all the other metrics and expressions used in the metric specification.</p> <p>If you are only retrieving metrics and not performing any math expressions, do not specify anything for <code>ReturnData</code>. This sets it to its default (<code>true</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingMetricDataQuery) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    out["Id"] = value["id"]
    if "label" in value:
        out["Label"] = value["label"]
    if "metric_stat" in value:
        import capo_application_auto_scaling.types.target_tracking_metric_stat

        out["MetricStat"] = (
            capo_application_auto_scaling.types.target_tracking_metric_stat.serialize_aws_json_1_1(
                value["metric_stat"]
            )
        )
    if "return_data" in value:
        out["ReturnData"] = value["return_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingMetricDataQuery:
    out: TargetTrackingMetricDataQuery = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("MetricStat") is not None:
        import capo_application_auto_scaling.types.target_tracking_metric_stat

        out["metric_stat"] = (
            capo_application_auto_scaling.types.target_tracking_metric_stat.deserialize_aws_json_1_1(
                data["MetricStat"]
            )
        )
    if data.get("ReturnData") is not None:
        out["return_data"] = data["ReturnData"]
    return out
