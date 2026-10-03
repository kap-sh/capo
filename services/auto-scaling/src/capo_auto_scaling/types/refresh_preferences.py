"""Generated from Smithy shape ``com.amazonaws.autoscaling#RefreshPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.alarm_specification
    import capo_auto_scaling.types.auto_rollback
    import capo_auto_scaling.types.bake_time
    import capo_auto_scaling.types.checkpoint_delay
    import capo_auto_scaling.types.checkpoint_percentages
    import capo_auto_scaling.types.int_percent
    import capo_auto_scaling.types.int_percent100_to200
    import capo_auto_scaling.types.refresh_instance_warmup
    import capo_auto_scaling.types.scale_in_protected_instances
    import capo_auto_scaling.types.skip_matching
    import capo_auto_scaling.types.standby_instances


class RefreshPreferences(TypedDict, closed=True):
    min_healthy_percentage: NotRequired[
        "capo_auto_scaling.types.int_percent.IntPercent"
    ]
    """<p>Specifies the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload to allow the operation to continue. The value is expressed as a percentage of the desired capacity of the Auto Scaling group. Value range is 0 to 100.</p> <p>If you do not specify this property, the default is 90 percent, or the percentage set in the instance maintenance policy for the Auto Scaling group, if defined.</p>"""
    instance_warmup: NotRequired[
        "capo_auto_scaling.types.refresh_instance_warmup.RefreshInstanceWarmup"
    ]
    """<p>A time period, in seconds, during which an instance refresh waits before moving on to replacing the next instance after a new instance enters the <code>InService</code> state.</p> <p>This property is not required for normal usage. Instead, use the <code>DefaultInstanceWarmup</code> property of the Auto Scaling group. The <code>InstanceWarmup</code> and <code>DefaultInstanceWarmup</code> properties work the same way. Only specify this property if you must override the <code>DefaultInstanceWarmup</code> property. </p> <p> If you do not specify this property, the instance warmup by default is the value of the <code>DefaultInstanceWarmup</code> property, if defined (which is recommended in all cases), or the <code>HealthCheckGracePeriod</code> property otherwise.</p>"""
    checkpoint_percentages: NotRequired[
        "capo_auto_scaling.types.checkpoint_percentages.CheckpointPercentages"
    ]
    """<p>(Optional) Threshold values for each checkpoint in ascending order. Each number must be unique. To replace all instances in the Auto Scaling group, the last number in the array must be <code>100</code>.</p> <p>For usage examples, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-adding-checkpoints-instance-refresh.html">Add checkpoints to an instance refresh</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    checkpoint_delay: NotRequired[
        "capo_auto_scaling.types.checkpoint_delay.CheckpointDelay"
    ]
    """<p>(Optional) The amount of time, in seconds, to wait after a checkpoint before continuing. This property is optional, but if you specify a value for it, you must also specify a value for <code>CheckpointPercentages</code>. If you specify a value for <code>CheckpointPercentages</code> and not for <code>CheckpointDelay</code>, the <code>CheckpointDelay</code> defaults to <code>3600</code> (1 hour). </p>"""
    skip_matching: NotRequired["capo_auto_scaling.types.skip_matching.SkipMatching"]
    """<p>(Optional) Indicates whether skip matching is enabled. If enabled (<code>true</code>), then Amazon EC2 Auto Scaling skips replacing instances that match the desired configuration. If no desired configuration is specified, then it skips replacing instances that have the same launch template and instance types that the Auto Scaling group was using before the start of the instance refresh. The default is <code>false</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh-skip-matching.html">Use an instance refresh with skip matching</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    auto_rollback: NotRequired["capo_auto_scaling.types.auto_rollback.AutoRollback"]
    """<p>(Optional) Indicates whether to roll back the Auto Scaling group to its previous configuration if the instance refresh fails or a CloudWatch alarm threshold is met. The default is <code>false</code>.</p> <p>A rollback is not supported in the following situations: </p> <ul> <li> <p>There is no desired configuration specified for the instance refresh.</p> </li> <li> <p>The Auto Scaling group has a launch template that uses an Amazon Web Services Systems Manager parameter instead of an AMI ID for the <code>ImageId</code> property.</p> </li> <li> <p>The Auto Scaling group uses the launch template's <code>$Latest</code> or <code>$Default</code> version.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-rollback.html">Undo changes with a rollback</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    scale_in_protected_instances: NotRequired[
        "capo_auto_scaling.types.scale_in_protected_instances.ScaleInProtectedInstances"
    ]
    """<p>Choose the behavior that you want Amazon EC2 Auto Scaling to use if instances protected from scale in are found. </p> <p>The following lists the valid values:</p> <dl> <dt>Refresh</dt> <dd> <p>Amazon EC2 Auto Scaling replaces instances that are protected from scale in.</p> </dd> <dt>Ignore</dt> <dd> <p>Amazon EC2 Auto Scaling ignores instances that are protected from scale in and continues to replace instances that are not protected.</p> </dd> <dt>Wait (default)</dt> <dd> <p>Amazon EC2 Auto Scaling waits one hour for you to remove scale-in protection. Otherwise, the instance refresh will fail.</p> </dd> </dl>"""
    standby_instances: NotRequired[
        "capo_auto_scaling.types.standby_instances.StandbyInstances"
    ]
    """<p>Choose the behavior that you want Amazon EC2 Auto Scaling to use if instances in <code>Standby</code> state are found.</p> <p>The following lists the valid values:</p> <dl> <dt>Terminate</dt> <dd> <p>Amazon EC2 Auto Scaling terminates instances that are in <code>Standby</code>.</p> </dd> <dt>Ignore</dt> <dd> <p>Amazon EC2 Auto Scaling ignores instances that are in <code>Standby</code> and continues to replace instances that are in the <code>InService</code> state.</p> </dd> <dt>Wait (default)</dt> <dd> <p>Amazon EC2 Auto Scaling waits one hour for you to return the instances to service. Otherwise, the instance refresh will fail.</p> </dd> </dl>"""
    alarm_specification: NotRequired[
        "capo_auto_scaling.types.alarm_specification.AlarmSpecification"
    ]
    """<p>(Optional) The CloudWatch alarm specification. CloudWatch alarms can be used to identify any issues and fail the operation if an alarm threshold is met.</p>"""
    max_healthy_percentage: NotRequired[
        "capo_auto_scaling.types.int_percent100_to200.IntPercent100To200"
    ]
    """<p>Specifies the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. The value is expressed as a percentage of the desired capacity of the Auto Scaling group. Value range is 100 to 200.</p> <p>If you specify <code>MaxHealthyPercentage</code>, you must also specify <code>MinHealthyPercentage</code>, and the difference between them cannot be greater than 100. A larger range increases the number of instances that can be replaced at the same time.</p> <p>If you do not specify this property, the default is 100 percent, or the percentage set in the instance maintenance policy for the Auto Scaling group, if defined.</p> <important> <p>Explicitly setting <code>MaxHealthyPercentage</code> to 100 is not equivalent to omitting it. When <code>MaxHealthyPercentage</code> is explicitly set and it is mathematically impossible to replace instances while honoring both <code>MinHealthyPercentage</code> and <code>MaxHealthyPercentage</code> bounds simultaneously, Auto Scaling launches a new instance before terminating an old one (temporarily exceeding the desired capacity). When <code>MaxHealthyPercentage</code> is omitted, Auto Scaling terminates an instance and launches its replacement simultaneously. This behavioral difference can affect workflows that depend on instance replacement ordering.</p> </important>"""
    bake_time: NotRequired["capo_auto_scaling.types.bake_time.BakeTime"]
    """<p> The amount of time, in seconds, to wait at the end of an instance refresh before the instance refresh is considered complete. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RefreshPreferences, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min_healthy_percentage" in value:
        pairs.append(
            (f"{key_prefix}MinHealthyPercentage", str(value["min_healthy_percentage"]))
        )
    if "instance_warmup" in value:
        pairs.append((f"{key_prefix}InstanceWarmup", str(value["instance_warmup"])))
    if "checkpoint_percentages" in value:
        import capo_auto_scaling.types.checkpoint_percentages

        capo_auto_scaling.types.checkpoint_percentages.serialize_query(
            value["checkpoint_percentages"], pairs, f"{key_prefix}CheckpointPercentages"
        )
    if "checkpoint_delay" in value:
        pairs.append((f"{key_prefix}CheckpointDelay", str(value["checkpoint_delay"])))
    if "skip_matching" in value:
        pairs.append(
            (f"{key_prefix}SkipMatching", "true" if value["skip_matching"] else "false")
        )
    if "auto_rollback" in value:
        pairs.append(
            (f"{key_prefix}AutoRollback", "true" if value["auto_rollback"] else "false")
        )
    if "scale_in_protected_instances" in value:
        import capo_auto_scaling.types.scale_in_protected_instances

        capo_auto_scaling.types.scale_in_protected_instances.serialize_query(
            value["scale_in_protected_instances"],
            pairs,
            f"{key_prefix}ScaleInProtectedInstances",
        )
    if "standby_instances" in value:
        import capo_auto_scaling.types.standby_instances

        capo_auto_scaling.types.standby_instances.serialize_query(
            value["standby_instances"], pairs, f"{key_prefix}StandbyInstances"
        )
    if "alarm_specification" in value:
        import capo_auto_scaling.types.alarm_specification

        capo_auto_scaling.types.alarm_specification.serialize_query(
            value["alarm_specification"], pairs, f"{key_prefix}AlarmSpecification"
        )
    if "max_healthy_percentage" in value:
        pairs.append(
            (f"{key_prefix}MaxHealthyPercentage", str(value["max_healthy_percentage"]))
        )
    if "bake_time" in value:
        pairs.append((f"{key_prefix}BakeTime", str(value["bake_time"])))


def deserialize_query(el: Element) -> RefreshPreferences:
    out: RefreshPreferences = {}  # type: ignore[typeddict-item]
    child_min_healthy_percentage = el.find("MinHealthyPercentage")
    if child_min_healthy_percentage is not None:
        out["min_healthy_percentage"] = int(child_min_healthy_percentage.text or "")
    child_instance_warmup = el.find("InstanceWarmup")
    if child_instance_warmup is not None:
        out["instance_warmup"] = int(child_instance_warmup.text or "")
    child_checkpoint_percentages = el.find("CheckpointPercentages")
    if child_checkpoint_percentages is not None:
        import capo_auto_scaling.types.checkpoint_percentages

        out["checkpoint_percentages"] = (
            capo_auto_scaling.types.checkpoint_percentages.deserialize_query(
                child_checkpoint_percentages
            )
        )
    child_checkpoint_delay = el.find("CheckpointDelay")
    if child_checkpoint_delay is not None:
        out["checkpoint_delay"] = int(child_checkpoint_delay.text or "")
    child_skip_matching = el.find("SkipMatching")
    if child_skip_matching is not None:
        out["skip_matching"] = (child_skip_matching.text or "").lower() == "true"
    child_auto_rollback = el.find("AutoRollback")
    if child_auto_rollback is not None:
        out["auto_rollback"] = (child_auto_rollback.text or "").lower() == "true"
    child_scale_in_protected_instances = el.find("ScaleInProtectedInstances")
    if child_scale_in_protected_instances is not None:
        import capo_auto_scaling.types.scale_in_protected_instances

        out["scale_in_protected_instances"] = (
            capo_auto_scaling.types.scale_in_protected_instances.deserialize_query(
                child_scale_in_protected_instances
            )
        )
    child_standby_instances = el.find("StandbyInstances")
    if child_standby_instances is not None:
        import capo_auto_scaling.types.standby_instances

        out["standby_instances"] = (
            capo_auto_scaling.types.standby_instances.deserialize_query(
                child_standby_instances
            )
        )
    child_alarm_specification = el.find("AlarmSpecification")
    if child_alarm_specification is not None:
        import capo_auto_scaling.types.alarm_specification

        out["alarm_specification"] = (
            capo_auto_scaling.types.alarm_specification.deserialize_query(
                child_alarm_specification
            )
        )
    child_max_healthy_percentage = el.find("MaxHealthyPercentage")
    if child_max_healthy_percentage is not None:
        out["max_healthy_percentage"] = int(child_max_healthy_percentage.text or "")
    child_bake_time = el.find("BakeTime")
    if child_bake_time is not None:
        out["bake_time"] = int(child_bake_time.text or "")
    return out
