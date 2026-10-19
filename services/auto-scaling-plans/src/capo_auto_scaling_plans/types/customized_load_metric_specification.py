"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#CustomizedLoadMetricSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.metric_dimensions
    import capo_auto_scaling_plans.types.metric_name
    import capo_auto_scaling_plans.types.metric_namespace
    import capo_auto_scaling_plans.types.metric_statistic
    import capo_auto_scaling_plans.types.metric_unit


class CustomizedLoadMetricSpecification(TypedDict, closed=True):
    metric_name: "capo_auto_scaling_plans.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    namespace: "capo_auto_scaling_plans.types.metric_namespace.MetricNamespace"
    """<p>The namespace of the metric.</p>"""
    dimensions: NotRequired[
        "capo_auto_scaling_plans.types.metric_dimensions.MetricDimensions"
    ]
    """<p>The dimensions of the metric.</p> <p>Conditional: If you published your metric with dimensions, you must specify the same dimensions in your customized load metric specification.</p>"""
    statistic: "capo_auto_scaling_plans.types.metric_statistic.MetricStatistic"
    """<p>The statistic of the metric. The only valid value is <code>Sum</code>.</p>"""
    unit: NotRequired["capo_auto_scaling_plans.types.metric_unit.MetricUnit"]
    """<p>The unit of the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizedLoadMetricSpecification) -> dict:
    out: dict = {}
    out["MetricName"] = value["metric_name"]
    out["Namespace"] = value["namespace"]
    if "dimensions" in value:
        import capo_auto_scaling_plans.types.metric_dimensions

        out["Dimensions"] = (
            capo_auto_scaling_plans.types.metric_dimensions.serialize_aws_json_1_1(
                value["dimensions"]
            )
        )
    import capo_auto_scaling_plans.types.metric_statistic

    out["Statistic"] = (
        capo_auto_scaling_plans.types.metric_statistic.serialize_aws_json_1_1(
            value["statistic"]
        )
    )
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizedLoadMetricSpecification:
    out: CustomizedLoadMetricSpecification = {}  # type: ignore[typeddict-item]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        out["metric_name"] = ""
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        out["namespace"] = ""
    if data.get("Dimensions") is not None:
        import capo_auto_scaling_plans.types.metric_dimensions

        out["dimensions"] = (
            capo_auto_scaling_plans.types.metric_dimensions.deserialize_aws_json_1_1(
                data["Dimensions"]
            )
        )
    if data.get("Statistic") is not None:
        import capo_auto_scaling_plans.types.metric_statistic

        out["statistic"] = (
            capo_auto_scaling_plans.types.metric_statistic.deserialize_aws_json_1_1(
                data["Statistic"]
            )
        )
    else:
        import typing

        out["statistic"] = typing.cast(
            "capo_auto_scaling_plans.types.metric_statistic.MetricStatistic", ""
        )
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out
