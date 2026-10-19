"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#StepAdjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.metric_scale
    import capo_application_auto_scaling.types.scaling_adjustment


class StepAdjustment(TypedDict, closed=True):
    metric_interval_lower_bound: NotRequired[
        "capo_application_auto_scaling.types.metric_scale.MetricScale"
    ]
    """<p>The lower bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the lower bound is inclusive (the metric must be greater than or equal to the threshold plus the lower bound). Otherwise, it's exclusive (the metric must be greater than the threshold plus the lower bound). A null value indicates negative infinity.</p>"""
    metric_interval_upper_bound: NotRequired[
        "capo_application_auto_scaling.types.metric_scale.MetricScale"
    ]
    """<p>The upper bound for the difference between the alarm threshold and the CloudWatch metric. If the metric value is above the breach threshold, the upper bound is exclusive (the metric must be less than the threshold plus the upper bound). Otherwise, it's inclusive (the metric must be less than or equal to the threshold plus the upper bound). A null value indicates positive infinity.</p> <p>The upper bound must be greater than the lower bound.</p>"""
    scaling_adjustment: (
        "capo_application_auto_scaling.types.scaling_adjustment.ScalingAdjustment"
    )
    """<p>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a non-negative value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepAdjustment) -> dict:
    out: dict = {}
    if "metric_interval_lower_bound" in value:
        out["MetricIntervalLowerBound"] = (
            "NaN"
            if value["metric_interval_lower_bound"]
            != value["metric_interval_lower_bound"]
            else "Infinity"
            if value["metric_interval_lower_bound"] == float("inf")
            else "-Infinity"
            if value["metric_interval_lower_bound"] == float("-inf")
            else value["metric_interval_lower_bound"]
        )
    if "metric_interval_upper_bound" in value:
        out["MetricIntervalUpperBound"] = (
            "NaN"
            if value["metric_interval_upper_bound"]
            != value["metric_interval_upper_bound"]
            else "Infinity"
            if value["metric_interval_upper_bound"] == float("inf")
            else "-Infinity"
            if value["metric_interval_upper_bound"] == float("-inf")
            else value["metric_interval_upper_bound"]
        )
    out["ScalingAdjustment"] = value["scaling_adjustment"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StepAdjustment:
    out: StepAdjustment = {}  # type: ignore[typeddict-item]
    if data.get("MetricIntervalLowerBound") is not None:
        out["metric_interval_lower_bound"] = float(data["MetricIntervalLowerBound"])
    if data.get("MetricIntervalUpperBound") is not None:
        out["metric_interval_upper_bound"] = float(data["MetricIntervalUpperBound"])
    if data.get("ScalingAdjustment") is not None:
        out["scaling_adjustment"] = data["ScalingAdjustment"]
    else:
        out["scaling_adjustment"] = 0
    return out
