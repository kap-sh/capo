"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#TargetTrackingScalingPolicyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.cooldown
    import capo_application_auto_scaling.types.customized_metric_specification
    import capo_application_auto_scaling.types.disable_scale_in
    import capo_application_auto_scaling.types.metric_scale
    import capo_application_auto_scaling.types.predefined_metric_specification


class TargetTrackingScalingPolicyConfiguration(TypedDict, closed=True):
    target_value: "capo_application_auto_scaling.types.metric_scale.MetricScale"
    """<p>The target value for the metric. Although this property accepts numbers of type Double, it won't accept values that are either too small or too large. Values must be in the range of -2^360 to 2^360. The value must be a valid number based on the choice of metric. For example, if the metric is CPU utilization, then the target value is a percent value that represents how much of the CPU can be used before scaling out. </p> <note> <p>If the scaling policy specifies the <code>ALBRequestCountPerTarget</code> predefined metric, specify the target utilization as the optimal average request count per target during any one-minute interval.</p> </note>"""
    predefined_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.predefined_metric_specification.PredefinedMetricSpecification"
    ]
    """<p>A predefined metric. You can specify either a predefined metric or a customized metric.</p>"""
    customized_metric_specification: NotRequired[
        "capo_application_auto_scaling.types.customized_metric_specification.CustomizedMetricSpecification"
    ]
    """<p>A customized metric. You can specify either a predefined metric or a customized metric.</p>"""
    scale_out_cooldown: NotRequired[
        "capo_application_auto_scaling.types.cooldown.Cooldown"
    ]
    """<p>The amount of time, in seconds, to wait for a previous scale-out activity to take effect. For more information and for default values, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown">Define cooldown periods</a> in the <i>Application Auto Scaling User Guide</i>.</p>"""
    scale_in_cooldown: NotRequired[
        "capo_application_auto_scaling.types.cooldown.Cooldown"
    ]
    """<p>The amount of time, in seconds, after a scale-in activity completes before another scale-in activity can start. For more information and for default values, see <a href="https://docs.aws.amazon.com/autoscaling/application/userguide/target-tracking-scaling-policy-overview.html#target-tracking-cooldown">Define cooldown periods</a> in the <i>Application Auto Scaling User Guide</i>.</p>"""
    disable_scale_in: NotRequired[
        "capo_application_auto_scaling.types.disable_scale_in.DisableScaleIn"
    ]
    """<p>Indicates whether scale in by the target tracking scaling policy is disabled. If the value is <code>true</code>, scale in is disabled and the target tracking scaling policy won't remove capacity from the scalable target. Otherwise, scale in is enabled and the target tracking scaling policy can remove capacity from the scalable target. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingScalingPolicyConfiguration) -> dict:
    out: dict = {}
    out["TargetValue"] = (
        "NaN"
        if value["target_value"] != value["target_value"]
        else "Infinity"
        if value["target_value"] == float("inf")
        else "-Infinity"
        if value["target_value"] == float("-inf")
        else value["target_value"]
    )
    if "predefined_metric_specification" in value:
        import capo_application_auto_scaling.types.predefined_metric_specification

        out["PredefinedMetricSpecification"] = (
            capo_application_auto_scaling.types.predefined_metric_specification.serialize_aws_json_1_1(
                value["predefined_metric_specification"]
            )
        )
    if "customized_metric_specification" in value:
        import capo_application_auto_scaling.types.customized_metric_specification

        out["CustomizedMetricSpecification"] = (
            capo_application_auto_scaling.types.customized_metric_specification.serialize_aws_json_1_1(
                value["customized_metric_specification"]
            )
        )
    if "scale_out_cooldown" in value:
        out["ScaleOutCooldown"] = value["scale_out_cooldown"]
    if "scale_in_cooldown" in value:
        out["ScaleInCooldown"] = value["scale_in_cooldown"]
    if "disable_scale_in" in value:
        out["DisableScaleIn"] = value["disable_scale_in"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingScalingPolicyConfiguration:
    out: TargetTrackingScalingPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    else:
        raise DeserializationError(
            "TargetTrackingScalingPolicyConfiguration.target_value required"
        )
    if data.get("PredefinedMetricSpecification") is not None:
        import capo_application_auto_scaling.types.predefined_metric_specification

        out["predefined_metric_specification"] = (
            capo_application_auto_scaling.types.predefined_metric_specification.deserialize_aws_json_1_1(
                data["PredefinedMetricSpecification"]
            )
        )
    if data.get("CustomizedMetricSpecification") is not None:
        import capo_application_auto_scaling.types.customized_metric_specification

        out["customized_metric_specification"] = (
            capo_application_auto_scaling.types.customized_metric_specification.deserialize_aws_json_1_1(
                data["CustomizedMetricSpecification"]
            )
        )
    if data.get("ScaleOutCooldown") is not None:
        out["scale_out_cooldown"] = data["ScaleOutCooldown"]
    if data.get("ScaleInCooldown") is not None:
        out["scale_in_cooldown"] = data["ScaleInCooldown"]
    if data.get("DisableScaleIn") is not None:
        out["disable_scale_in"] = data["DisableScaleIn"]
    return out
