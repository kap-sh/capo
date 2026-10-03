"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.alarms
    import capo_auto_scaling.types.cooldown
    import capo_auto_scaling.types.estimated_instance_warmup
    import capo_auto_scaling.types.min_adjustment_magnitude
    import capo_auto_scaling.types.min_adjustment_step
    import capo_auto_scaling.types.policy_increment
    import capo_auto_scaling.types.predictive_scaling_configuration
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.scaling_policy_enabled
    import capo_auto_scaling.types.step_adjustments
    import capo_auto_scaling.types.target_tracking_configuration
    import capo_auto_scaling.types.xml_string_max_len32
    import capo_auto_scaling.types.xml_string_max_len64
    import capo_auto_scaling.types.xml_string_max_len255


class ScalingPolicy(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    policy_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the scaling policy.</p>"""
    policy_arn: NotRequired["capo_auto_scaling.types.resource_name.ResourceName"]
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    policy_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p>One of the following policy types: </p> <ul> <li> <p> <code>TargetTrackingScaling</code> </p> </li> <li> <p> <code>StepScaling</code> </p> </li> <li> <p> <code>SimpleScaling</code> (default)</p> </li> <li> <p> <code>PredictiveScaling</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html">Target tracking scaling policies</a> and <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html">Step and simple scaling policies</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    adjustment_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>Specifies how the scaling adjustment is interpreted (for example, an absolute number or a percentage). The valid values are <code>ChangeInCapacity</code>, <code>ExactCapacity</code>, and <code>PercentChangeInCapacity</code>.</p>"""
    min_adjustment_step: NotRequired[
        "capo_auto_scaling.types.min_adjustment_step.MinAdjustmentStep"
    ]
    """<p>Available for backward compatibility. Use <code>MinAdjustmentMagnitude</code> instead.</p>"""
    min_adjustment_magnitude: NotRequired[
        "capo_auto_scaling.types.min_adjustment_magnitude.MinAdjustmentMagnitude"
    ]
    """<p>The minimum value to scale by when the adjustment type is <code>PercentChangeInCapacity</code>. </p>"""
    scaling_adjustment: NotRequired[
        "capo_auto_scaling.types.policy_increment.PolicyIncrement"
    ]
    """<p>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity.</p>"""
    cooldown: NotRequired["capo_auto_scaling.types.cooldown.Cooldown"]
    """<p>The duration of the policy's cooldown period, in seconds.</p>"""
    step_adjustments: NotRequired[
        "capo_auto_scaling.types.step_adjustments.StepAdjustments"
    ]
    """<p>A set of adjustments that enable you to scale based on the size of the alarm breach.</p>"""
    metric_aggregation_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len32.XmlStringMaxLen32"
    ]
    """<p>The aggregation type for the CloudWatch metrics. The valid values are <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code>.</p>"""
    estimated_instance_warmup: NotRequired[
        "capo_auto_scaling.types.estimated_instance_warmup.EstimatedInstanceWarmup"
    ]
    """<p>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics.</p>"""
    alarms: NotRequired["capo_auto_scaling.types.alarms.Alarms"]
    """<p>The CloudWatch alarms related to the policy.</p>"""
    target_tracking_configuration: NotRequired[
        "capo_auto_scaling.types.target_tracking_configuration.TargetTrackingConfiguration"
    ]
    """<p>A target tracking scaling policy.</p>"""
    enabled: NotRequired[
        "capo_auto_scaling.types.scaling_policy_enabled.ScalingPolicyEnabled"
    ]
    """<p>Indicates whether the policy is enabled (<code>true</code>) or disabled (<code>false</code>).</p>"""
    predictive_scaling_configuration: NotRequired[
        "capo_auto_scaling.types.predictive_scaling_configuration.PredictiveScalingConfiguration"
    ]
    """<p>A predictive scaling policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "policy_name" in value:
        pairs.append((f"{key_prefix}PolicyName", str(value["policy_name"])))
    if "policy_arn" in value:
        pairs.append((f"{key_prefix}PolicyARN", str(value["policy_arn"])))
    if "policy_type" in value:
        pairs.append((f"{key_prefix}PolicyType", str(value["policy_type"])))
    if "adjustment_type" in value:
        pairs.append((f"{key_prefix}AdjustmentType", str(value["adjustment_type"])))
    if "min_adjustment_step" in value:
        pairs.append(
            (f"{key_prefix}MinAdjustmentStep", str(value["min_adjustment_step"]))
        )
    if "min_adjustment_magnitude" in value:
        pairs.append(
            (
                f"{key_prefix}MinAdjustmentMagnitude",
                str(value["min_adjustment_magnitude"]),
            )
        )
    if "scaling_adjustment" in value:
        pairs.append(
            (f"{key_prefix}ScalingAdjustment", str(value["scaling_adjustment"]))
        )
    if "cooldown" in value:
        pairs.append((f"{key_prefix}Cooldown", str(value["cooldown"])))
    if "step_adjustments" in value:
        import capo_auto_scaling.types.step_adjustments

        capo_auto_scaling.types.step_adjustments.serialize_query(
            value["step_adjustments"], pairs, f"{key_prefix}StepAdjustments"
        )
    if "metric_aggregation_type" in value:
        pairs.append(
            (
                f"{key_prefix}MetricAggregationType",
                str(value["metric_aggregation_type"]),
            )
        )
    if "estimated_instance_warmup" in value:
        pairs.append(
            (
                f"{key_prefix}EstimatedInstanceWarmup",
                str(value["estimated_instance_warmup"]),
            )
        )
    if "alarms" in value:
        import capo_auto_scaling.types.alarms

        capo_auto_scaling.types.alarms.serialize_query(
            value["alarms"], pairs, f"{key_prefix}Alarms"
        )
    if "target_tracking_configuration" in value:
        import capo_auto_scaling.types.target_tracking_configuration

        capo_auto_scaling.types.target_tracking_configuration.serialize_query(
            value["target_tracking_configuration"],
            pairs,
            f"{key_prefix}TargetTrackingConfiguration",
        )
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))
    if "predictive_scaling_configuration" in value:
        import capo_auto_scaling.types.predictive_scaling_configuration

        capo_auto_scaling.types.predictive_scaling_configuration.serialize_query(
            value["predictive_scaling_configuration"],
            pairs,
            f"{key_prefix}PredictiveScalingConfiguration",
        )


def deserialize_query(el: Element) -> ScalingPolicy:
    out: ScalingPolicy = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_policy_name = el.find("PolicyName")
    if child_policy_name is not None:
        out["policy_name"] = str(child_policy_name.text or "")
    child_policy_arn = el.find("PolicyARN")
    if child_policy_arn is not None:
        out["policy_arn"] = str(child_policy_arn.text or "")
    child_policy_type = el.find("PolicyType")
    if child_policy_type is not None:
        out["policy_type"] = str(child_policy_type.text or "")
    child_adjustment_type = el.find("AdjustmentType")
    if child_adjustment_type is not None:
        out["adjustment_type"] = str(child_adjustment_type.text or "")
    child_min_adjustment_step = el.find("MinAdjustmentStep")
    if child_min_adjustment_step is not None:
        out["min_adjustment_step"] = int(child_min_adjustment_step.text or "")
    child_min_adjustment_magnitude = el.find("MinAdjustmentMagnitude")
    if child_min_adjustment_magnitude is not None:
        out["min_adjustment_magnitude"] = int(child_min_adjustment_magnitude.text or "")
    child_scaling_adjustment = el.find("ScalingAdjustment")
    if child_scaling_adjustment is not None:
        out["scaling_adjustment"] = int(child_scaling_adjustment.text or "")
    child_cooldown = el.find("Cooldown")
    if child_cooldown is not None:
        out["cooldown"] = int(child_cooldown.text or "")
    child_step_adjustments = el.find("StepAdjustments")
    if child_step_adjustments is not None:
        import capo_auto_scaling.types.step_adjustments

        out["step_adjustments"] = (
            capo_auto_scaling.types.step_adjustments.deserialize_query(
                child_step_adjustments
            )
        )
    child_metric_aggregation_type = el.find("MetricAggregationType")
    if child_metric_aggregation_type is not None:
        out["metric_aggregation_type"] = str(child_metric_aggregation_type.text or "")
    child_estimated_instance_warmup = el.find("EstimatedInstanceWarmup")
    if child_estimated_instance_warmup is not None:
        out["estimated_instance_warmup"] = int(
            child_estimated_instance_warmup.text or ""
        )
    child_alarms = el.find("Alarms")
    if child_alarms is not None:
        import capo_auto_scaling.types.alarms

        out["alarms"] = capo_auto_scaling.types.alarms.deserialize_query(child_alarms)
    child_target_tracking_configuration = el.find("TargetTrackingConfiguration")
    if child_target_tracking_configuration is not None:
        import capo_auto_scaling.types.target_tracking_configuration

        out["target_tracking_configuration"] = (
            capo_auto_scaling.types.target_tracking_configuration.deserialize_query(
                child_target_tracking_configuration
            )
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_predictive_scaling_configuration = el.find("PredictiveScalingConfiguration")
    if child_predictive_scaling_configuration is not None:
        import capo_auto_scaling.types.predictive_scaling_configuration

        out["predictive_scaling_configuration"] = (
            capo_auto_scaling.types.predictive_scaling_configuration.deserialize_query(
                child_predictive_scaling_configuration
            )
        )
    return out
