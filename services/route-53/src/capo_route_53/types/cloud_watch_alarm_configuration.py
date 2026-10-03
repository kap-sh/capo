"""Generated from Smithy shape ``com.amazonaws.route53#CloudWatchAlarmConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.comparison_operator
    import capo_route_53.types.dimension_list
    import capo_route_53.types.evaluation_periods
    import capo_route_53.types.metric_name
    import capo_route_53.types.namespace
    import capo_route_53.types.period
    import capo_route_53.types.statistic
    import capo_route_53.types.threshold


class CloudWatchAlarmConfiguration(TypedDict, closed=True):
    evaluation_periods: "capo_route_53.types.evaluation_periods.EvaluationPeriods"
    """<p>For the metric that the CloudWatch alarm is associated with, the number of periods that the metric is compared to the threshold.</p>"""
    threshold: "capo_route_53.types.threshold.Threshold"
    """<p>For the metric that the CloudWatch alarm is associated with, the value the metric is compared with.</p>"""
    comparison_operator: "capo_route_53.types.comparison_operator.ComparisonOperator"
    """<p>For the metric that the CloudWatch alarm is associated with, the arithmetic operation that is used for the comparison.</p>"""
    period: "capo_route_53.types.period.Period"
    """<p>For the metric that the CloudWatch alarm is associated with, the duration of one evaluation period in seconds.</p>"""
    metric_name: "capo_route_53.types.metric_name.MetricName"
    """<p>The name of the CloudWatch metric that the alarm is associated with.</p>"""
    namespace: "capo_route_53.types.namespace.Namespace"
    """<p>The namespace of the metric that the alarm is associated with. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""
    statistic: "capo_route_53.types.statistic.Statistic"
    """<p>For the metric that the CloudWatch alarm is associated with, the statistic that is applied to the metric.</p>"""
    dimensions: NotRequired["capo_route_53.types.dimension_list.DimensionList"]
    """<p>For the metric that the CloudWatch alarm is associated with, a complex type that contains information about the dimensions for the metric. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html">Amazon CloudWatch Namespaces, Dimensions, and Metrics Reference</a> in the <i>Amazon CloudWatch User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CloudWatchAlarmConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "EvaluationPeriods").text = str(value["evaluation_periods"])
    SubElement(el, "Threshold").text = (
        "NaN"
        if value["threshold"] != value["threshold"]
        else "Infinity"
        if value["threshold"] == float("inf")
        else "-Infinity"
        if value["threshold"] == float("-inf")
        else str(value["threshold"])
    )
    import capo_route_53.types.comparison_operator

    capo_route_53.types.comparison_operator.serialize_xml(
        value["comparison_operator"], el, "ComparisonOperator"
    )
    SubElement(el, "Period").text = str(value["period"])
    SubElement(el, "MetricName").text = str(value["metric_name"])
    SubElement(el, "Namespace").text = str(value["namespace"])
    import capo_route_53.types.statistic

    capo_route_53.types.statistic.serialize_xml(value["statistic"], el, "Statistic")
    if "dimensions" in value:
        import capo_route_53.types.dimension_list

        capo_route_53.types.dimension_list.serialize_xml(
            value["dimensions"], el, "Dimensions"
        )


def deserialize_xml(el: Element) -> CloudWatchAlarmConfiguration:
    out: CloudWatchAlarmConfiguration = {}  # type: ignore[typeddict-item]
    child_evaluation_periods = el.find("EvaluationPeriods")
    if child_evaluation_periods is not None:
        out["evaluation_periods"] = int(child_evaluation_periods.text or "")
    else:
        raise DeserializationError(
            "CloudWatchAlarmConfiguration.evaluation_periods required"
        )
    child_threshold = el.find("Threshold")
    if child_threshold is not None:
        out["threshold"] = float(child_threshold.text or "")
    else:
        raise DeserializationError("CloudWatchAlarmConfiguration.threshold required")
    child_comparison_operator = el.find("ComparisonOperator")
    if child_comparison_operator is not None:
        import capo_route_53.types.comparison_operator

        out["comparison_operator"] = (
            capo_route_53.types.comparison_operator.deserialize_xml(
                child_comparison_operator
            )
        )
    else:
        raise DeserializationError(
            "CloudWatchAlarmConfiguration.comparison_operator required"
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    else:
        raise DeserializationError("CloudWatchAlarmConfiguration.period required")
    child_metric_name = el.find("MetricName")
    if child_metric_name is not None:
        out["metric_name"] = str(child_metric_name.text or "")
    else:
        raise DeserializationError("CloudWatchAlarmConfiguration.metric_name required")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    else:
        raise DeserializationError("CloudWatchAlarmConfiguration.namespace required")
    child_statistic = el.find("Statistic")
    if child_statistic is not None:
        import capo_route_53.types.statistic

        out["statistic"] = capo_route_53.types.statistic.deserialize_xml(
            child_statistic
        )
    else:
        raise DeserializationError("CloudWatchAlarmConfiguration.statistic required")
    child_dimensions = el.find("Dimensions")
    if child_dimensions is not None:
        import capo_route_53.types.dimension_list

        out["dimensions"] = capo_route_53.types.dimension_list.deserialize_xml(
            child_dimensions
        )
    return out
