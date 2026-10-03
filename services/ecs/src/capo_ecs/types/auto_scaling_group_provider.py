"""Generated from Smithy shape ``com.amazonaws.ecs#AutoScalingGroupProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.managed_draining
    import capo_ecs.types.managed_scaling
    import capo_ecs.types.managed_termination_protection
    import capo_ecs.types.string


class AutoScalingGroupProvider(TypedDict, closed=True):
    auto_scaling_group_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) that identifies the Auto Scaling group, or the Auto Scaling group name.</p>"""
    managed_scaling: NotRequired["capo_ecs.types.managed_scaling.ManagedScaling"]
    """<p>The managed scaling settings for the Auto Scaling group capacity provider.</p>"""
    managed_termination_protection: NotRequired[
        "capo_ecs.types.managed_termination_protection.ManagedTerminationProtection"
    ]
    """<p>The managed termination protection setting to use for the Auto Scaling group capacity provider. This determines whether the Auto Scaling group has managed termination protection. The default is off.</p> <important> <p>When using managed termination protection, managed scaling must also be used otherwise managed termination protection doesn't work.</p> </important> <p>When managed termination protection is on, Amazon ECS prevents the Amazon EC2 instances in an Auto Scaling group that contain tasks from being terminated during a scale-in action. The Auto Scaling group and each instance in the Auto Scaling group must have instance protection from scale-in actions on as well. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection">Instance Protection</a> in the <i>Auto Scaling User Guide</i>.</p> <p>When managed termination protection is off, your Amazon EC2 instances aren't protected from termination when the Auto Scaling group scales in.</p>"""
    managed_draining: NotRequired["capo_ecs.types.managed_draining.ManagedDraining"]
    """<p>The managed draining option for the Auto Scaling group capacity provider. When you enable this, Amazon ECS manages and gracefully drains the EC2 container instances that are in the Auto Scaling group capacity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingGroupProvider) -> dict:
    out: dict = {}
    out["autoScalingGroupArn"] = value["auto_scaling_group_arn"]
    if "managed_scaling" in value:
        import capo_ecs.types.managed_scaling

        out["managedScaling"] = capo_ecs.types.managed_scaling.serialize_aws_json_1_1(
            value["managed_scaling"]
        )
    if "managed_termination_protection" in value:
        import capo_ecs.types.managed_termination_protection

        out["managedTerminationProtection"] = (
            capo_ecs.types.managed_termination_protection.serialize_aws_json_1_1(
                value["managed_termination_protection"]
            )
        )
    if "managed_draining" in value:
        import capo_ecs.types.managed_draining

        out["managedDraining"] = capo_ecs.types.managed_draining.serialize_aws_json_1_1(
            value["managed_draining"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoScalingGroupProvider:
    out: AutoScalingGroupProvider = {}  # type: ignore[typeddict-item]
    if data.get("autoScalingGroupArn") is not None:
        out["auto_scaling_group_arn"] = data["autoScalingGroupArn"]
    else:
        raise DeserializationError(
            "AutoScalingGroupProvider.auto_scaling_group_arn required"
        )
    if data.get("managedScaling") is not None:
        import capo_ecs.types.managed_scaling

        out["managed_scaling"] = (
            capo_ecs.types.managed_scaling.deserialize_aws_json_1_1(
                data["managedScaling"]
            )
        )
    if data.get("managedTerminationProtection") is not None:
        import capo_ecs.types.managed_termination_protection

        out["managed_termination_protection"] = (
            capo_ecs.types.managed_termination_protection.deserialize_aws_json_1_1(
                data["managedTerminationProtection"]
            )
        )
    if data.get("managedDraining") is not None:
        import capo_ecs.types.managed_draining

        out["managed_draining"] = (
            capo_ecs.types.managed_draining.deserialize_aws_json_1_1(
                data["managedDraining"]
            )
        )
    return out
