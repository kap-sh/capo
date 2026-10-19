"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#TargetTrackingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.cooldown
    import capo_auto_scaling_plans.types.customized_scaling_metric_specification
    import capo_auto_scaling_plans.types.disable_scale_in
    import capo_auto_scaling_plans.types.metric_scale
    import capo_auto_scaling_plans.types.predefined_scaling_metric_specification


class TargetTrackingConfiguration(TypedDict, closed=True):
    predefined_scaling_metric_specification: NotRequired[
        "capo_auto_scaling_plans.types.predefined_scaling_metric_specification.PredefinedScalingMetricSpecification"
    ]
    """<p>A predefined metric. You can specify either a predefined metric or a customized metric.</p>"""
    customized_scaling_metric_specification: NotRequired[
        "capo_auto_scaling_plans.types.customized_scaling_metric_specification.CustomizedScalingMetricSpecification"
    ]
    """<p>A customized metric. You can specify either a predefined metric or a customized metric. </p>"""
    target_value: "capo_auto_scaling_plans.types.metric_scale.MetricScale"
    """<p>The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360.</p>"""
    disable_scale_in: NotRequired[
        "capo_auto_scaling_plans.types.disable_scale_in.DisableScaleIn"
    ]
    """<p>Indicates whether scale in by the target tracking scaling policy is disabled. If the value is <code>true</code>, scale in is disabled and the target tracking scaling policy doesn't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable resource. </p> <p>The default value is <code>false</code>.</p>"""
    scale_out_cooldown: NotRequired["capo_auto_scaling_plans.types.cooldown.Cooldown"]
    """<p>The amount of time, in seconds, to wait for a previous scale-out activity to take effect. This property is not used if the scalable resource is an Auto Scaling group.</p> <p>With the <i>scale-out cooldown period</i>, the intention is to continuously (but not excessively) scale out. After Auto Scaling successfully scales out using a target tracking scaling policy, it starts to calculate the cooldown time. The scaling policy won't increase the desired capacity again unless either a larger scale out is triggered or the cooldown period ends.</p>"""
    scale_in_cooldown: NotRequired["capo_auto_scaling_plans.types.cooldown.Cooldown"]
    """<p>The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. This property is not used if the scalable resource is an Auto Scaling group.</p> <p>With the <i>scale-in cooldown period</i>, the intention is to scale in conservatively to protect your application’s availability, so scale-in activities are blocked until the cooldown period has expired. However, if another alarm triggers a scale-out activity during the scale-in cooldown period, Auto Scaling scales out the target immediately. In this case, the scale-in cooldown period stops and doesn't complete.</p>"""
    estimated_instance_warmup: NotRequired[
        "capo_auto_scaling_plans.types.cooldown.Cooldown"
    ]
    """<p>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. This value is used only if the resource is an Auto Scaling group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingConfiguration) -> dict:
    out: dict = {}
    if "predefined_scaling_metric_specification" in value:
        import capo_auto_scaling_plans.types.predefined_scaling_metric_specification

        out["PredefinedScalingMetricSpecification"] = (
            capo_auto_scaling_plans.types.predefined_scaling_metric_specification.serialize_aws_json_1_1(
                value["predefined_scaling_metric_specification"]
            )
        )
    if "customized_scaling_metric_specification" in value:
        import capo_auto_scaling_plans.types.customized_scaling_metric_specification

        out["CustomizedScalingMetricSpecification"] = (
            capo_auto_scaling_plans.types.customized_scaling_metric_specification.serialize_aws_json_1_1(
                value["customized_scaling_metric_specification"]
            )
        )
    out["TargetValue"] = (
        "NaN"
        if value["target_value"] != value["target_value"]
        else "Infinity"
        if value["target_value"] == float("inf")
        else "-Infinity"
        if value["target_value"] == float("-inf")
        else value["target_value"]
    )
    if "disable_scale_in" in value:
        out["DisableScaleIn"] = value["disable_scale_in"]
    if "scale_out_cooldown" in value:
        out["ScaleOutCooldown"] = value["scale_out_cooldown"]
    if "scale_in_cooldown" in value:
        out["ScaleInCooldown"] = value["scale_in_cooldown"]
    if "estimated_instance_warmup" in value:
        out["EstimatedInstanceWarmup"] = value["estimated_instance_warmup"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingConfiguration:
    out: TargetTrackingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PredefinedScalingMetricSpecification") is not None:
        import capo_auto_scaling_plans.types.predefined_scaling_metric_specification

        out["predefined_scaling_metric_specification"] = (
            capo_auto_scaling_plans.types.predefined_scaling_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedScalingMetricSpecification"]
            )
        )
    if data.get("CustomizedScalingMetricSpecification") is not None:
        import capo_auto_scaling_plans.types.customized_scaling_metric_specification

        out["customized_scaling_metric_specification"] = (
            capo_auto_scaling_plans.types.customized_scaling_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedScalingMetricSpecification"]
            )
        )
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    else:
        out["target_value"] = 0.0
    if data.get("DisableScaleIn") is not None:
        out["disable_scale_in"] = data["DisableScaleIn"]
    if data.get("ScaleOutCooldown") is not None:
        out["scale_out_cooldown"] = data["ScaleOutCooldown"]
    if data.get("ScaleInCooldown") is not None:
        out["scale_in_cooldown"] = data["ScaleInCooldown"]
    if data.get("EstimatedInstanceWarmup") is not None:
        out["estimated_instance_warmup"] = data["EstimatedInstanceWarmup"]
    return out
