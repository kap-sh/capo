"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.auto_repair_configuration
    import capo_ecs.types.infrastructure_optimization
    import capo_ecs.types.instance_launch_template
    import capo_ecs.types.propagate_mi_tags
    import capo_ecs.types.string


class ManagedInstancesProvider(TypedDict, closed=True):
    infrastructure_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS assumes to manage instances. This role must include permissions for Amazon EC2 instance lifecycle management, networking, and any additional Amazon Web Services services required for your workloads.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    instance_launch_template: NotRequired[
        "capo_ecs.types.instance_launch_template.InstanceLaunchTemplate"
    ]
    """<p>The launch template that defines how Amazon ECS launches Amazon ECS Managed Instances. This includes the instance profile for your tasks, network and storage configuration, and instance requirements that determine which Amazon EC2 instance types can be used.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html">Store instance launch parameters in Amazon EC2 launch templates</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_mi_tags.PropagateMITags"]
    """<p>Determines whether tags from the capacity provider are automatically applied to Amazon ECS Managed Instances. This helps with cost allocation and resource management by ensuring consistent tagging across your infrastructure.</p>"""
    infrastructure_optimization: NotRequired[
        "capo_ecs.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Configure it to turn on or off the infrastructure optimization in your capacity provider, and to control the idle or underutilized EC2 instances optimization delay.</p>"""
    auto_repair_configuration: NotRequired[
        "capo_ecs.types.auto_repair_configuration.AutoRepairConfiguration"
    ]
    """<p>The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Indicates whether Amazon ECS automatically replaces container instances that are detected as unhealthy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstancesProvider) -> dict:
    out: dict = {}
    if "infrastructure_role_arn" in value:
        out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
    if "instance_launch_template" in value:
        import capo_ecs.types.instance_launch_template

        out["instanceLaunchTemplate"] = (
            capo_ecs.types.instance_launch_template.serialize_aws_json_1_1(
                value["instance_launch_template"]
            )
        )
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_mi_tags

        out["propagateTags"] = capo_ecs.types.propagate_mi_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    if "infrastructure_optimization" in value:
        import capo_ecs.types.infrastructure_optimization

        out["infrastructureOptimization"] = (
            capo_ecs.types.infrastructure_optimization.serialize_aws_json_1_1(
                value["infrastructure_optimization"]
            )
        )
    if "auto_repair_configuration" in value:
        import capo_ecs.types.auto_repair_configuration

        out["autoRepairConfiguration"] = (
            capo_ecs.types.auto_repair_configuration.serialize_aws_json_1_1(
                value["auto_repair_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedInstancesProvider:
    out: ManagedInstancesProvider = {}  # type: ignore[typeddict-item]
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    if data.get("instanceLaunchTemplate") is not None:
        import capo_ecs.types.instance_launch_template

        out["instance_launch_template"] = (
            capo_ecs.types.instance_launch_template.deserialize_aws_json_1_1(
                data["instanceLaunchTemplate"]
            )
        )
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_mi_tags

        out["propagate_tags"] = (
            capo_ecs.types.propagate_mi_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    if data.get("infrastructureOptimization") is not None:
        import capo_ecs.types.infrastructure_optimization

        out["infrastructure_optimization"] = (
            capo_ecs.types.infrastructure_optimization.deserialize_aws_json_1_1(
                data["infrastructureOptimization"]
            )
        )
    if data.get("autoRepairConfiguration") is not None:
        import capo_ecs.types.auto_repair_configuration

        out["auto_repair_configuration"] = (
            capo_ecs.types.auto_repair_configuration.deserialize_aws_json_1_1(
                data["autoRepairConfiguration"]
            )
        )
    return out
