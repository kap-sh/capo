"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#StepScalingPolicyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.adjustment_type
    import capo_application_auto_scaling.types.cooldown
    import capo_application_auto_scaling.types.metric_aggregation_type
    import capo_application_auto_scaling.types.min_adjustment_magnitude
    import capo_application_auto_scaling.types.step_adjustments


class StepScalingPolicyConfiguration(TypedDict, closed=True):
    adjustment_type: NotRequired[
        "capo_application_auto_scaling.types.adjustment_type.AdjustmentType"
    ]
    """<p>Specifies how the <code>ScalingAdjustment</code> value in a <a href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepAdjustment.html">StepAdjustment</a> is interpreted (for example, an absolute number or a percentage). The valid values are <code>ChangeInCapacity</code>, <code>ExactCapacity</code>, and <code>PercentChangeInCapacity</code>. </p> <p> <code>AdjustmentType</code> is required if you are adding a new step scaling policy configuration.</p>"""
    step_adjustments: NotRequired[
        "capo_application_auto_scaling.types.step_adjustments.StepAdjustments"
    ]
    """<p>A set of adjustments that enable you to scale based on the size of the alarm breach.</p> <p>At least one step adjustment is required if you are adding a new step scaling policy configuration.</p>"""
    min_adjustment_magnitude: NotRequired[
        "capo_application_auto_scaling.types.min_adjustment_magnitude.MinAdjustmentMagnitude"
    ]
    """<p>The minimum value to scale by when the adjustment type is <code>PercentChangeInCapacity</code>. For example, suppose that you create a step scaling policy to scale out an Amazon ECS service by 25 percent and you specify a <code>MinAdjustmentMagnitude</code> of 2. If the service has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a <code>MinAdjustmentMagnitude</code> of 2, Application Auto Scaling scales out the service by 2 tasks.</p>"""
    cooldown: NotRequired["capo_application_auto_scaling.types.cooldown.Cooldown"]
    """<p>The amount of time, in seconds, to wait for a previous scaling activity to take effect. If not specified, the default value is 300. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/step-scaling-policy-overview.html#step-scaling-cooldown">Cooldown period</a> in the <i>Application Auto Scaling User Guide</i>.</p>"""
    metric_aggregation_type: NotRequired[
        "capo_application_auto_scaling.types.metric_aggregation_type.MetricAggregationType"
    ]
    """<p>The aggregation type for the CloudWatch metrics. Valid values are <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code>. If the aggregation type is null, the value is treated as <code>Average</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepScalingPolicyConfiguration) -> dict:
    out: dict = {}
    if "adjustment_type" in value:
        import capo_application_auto_scaling.types.adjustment_type

        out["AdjustmentType"] = (
            capo_application_auto_scaling.types.adjustment_type.serialize_aws_json_1_1(
                value["adjustment_type"]
            )
        )
    if "step_adjustments" in value:
        import capo_application_auto_scaling.types.step_adjustments

        out["StepAdjustments"] = (
            capo_application_auto_scaling.types.step_adjustments.serialize_aws_json_1_1(
                value["step_adjustments"]
            )
        )
    if "min_adjustment_magnitude" in value:
        out["MinAdjustmentMagnitude"] = value["min_adjustment_magnitude"]
    if "cooldown" in value:
        out["Cooldown"] = value["cooldown"]
    if "metric_aggregation_type" in value:
        import capo_application_auto_scaling.types.metric_aggregation_type

        out["MetricAggregationType"] = (
            capo_application_auto_scaling.types.metric_aggregation_type.serialize_aws_json_1_1(
                value["metric_aggregation_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StepScalingPolicyConfiguration:
    out: StepScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AdjustmentType") is not None:
        import capo_application_auto_scaling.types.adjustment_type

        out["adjustment_type"] = (
            capo_application_auto_scaling.types.adjustment_type.deserialize_aws_json_1_1(
                data["AdjustmentType"]
            )
        )
    if data.get("StepAdjustments") is not None:
        import capo_application_auto_scaling.types.step_adjustments

        out["step_adjustments"] = (
            capo_application_auto_scaling.types.step_adjustments.deserialize_aws_json_1_1(
                data["StepAdjustments"]
            )
        )
    if data.get("MinAdjustmentMagnitude") is not None:
        out["min_adjustment_magnitude"] = data["MinAdjustmentMagnitude"]
    if data.get("Cooldown") is not None:
        out["cooldown"] = data["Cooldown"]
    if data.get("MetricAggregationType") is not None:
        import capo_application_auto_scaling.types.metric_aggregation_type

        out["metric_aggregation_type"] = (
            capo_application_auto_scaling.types.metric_aggregation_type.deserialize_aws_json_1_1(
                data["MetricAggregationType"]
            )
        )
    return out
