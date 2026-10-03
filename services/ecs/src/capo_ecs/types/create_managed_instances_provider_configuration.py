"""Generated from Smithy shape ``com.amazonaws.ecs#CreateManagedInstancesProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.auto_repair_configuration
    import capo_ecs.types.infrastructure_optimization
    import capo_ecs.types.instance_launch_template
    import capo_ecs.types.propagate_mi_tags
    import capo_ecs.types.string


class CreateManagedInstancesProviderConfiguration(TypedDict, closed=True):
    infrastructure_role_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS uses to manage instances on your behalf. This role must have permissions to launch, terminate, and manage Amazon EC2 instances, as well as access to other Amazon Web Services services required for Amazon ECS Managed Instances functionality.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>. </p>"""
    instance_launch_template: (
        "capo_ecs.types.instance_launch_template.InstanceLaunchTemplate"
    )
    """<p>The launch template configuration that specifies how Amazon ECS should launch Amazon EC2 instances. This includes the instance profile, network configuration, storage settings, and instance requirements for attribute-based instance type selection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html">Store instance launch parameters in Amazon EC2 launch templates</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_mi_tags.PropagateMITags"]
    """<p>Specifies whether to propagate tags from the capacity provider to the Amazon ECS Managed Instances. When enabled, tags applied to the capacity provider are automatically applied to all instances launched by this provider.</p>"""
    infrastructure_optimization: NotRequired[
        "capo_ecs.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Provides control over the delay between when EC2 instances become idle or underutilized and when Amazon ECS optimizes them.</p>"""
    auto_repair_configuration: NotRequired[
        "capo_ecs.types.auto_repair_configuration.AutoRepairConfiguration"
    ]
    """<p>The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Use this to enable or disable automatic replacement of container instances that are detected as unhealthy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateManagedInstancesProviderConfiguration) -> dict:
    out: dict = {}
    out["infrastructureRoleArn"] = value["infrastructure_role_arn"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateManagedInstancesProviderConfiguration:
    out: CreateManagedInstancesProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("infrastructureRoleArn") is not None:
        out["infrastructure_role_arn"] = data["infrastructureRoleArn"]
    else:
        raise DeserializationError(
            "CreateManagedInstancesProviderConfiguration.infrastructure_role_arn required"
        )
    if data.get("instanceLaunchTemplate") is not None:
        import capo_ecs.types.instance_launch_template

        out["instance_launch_template"] = (
            capo_ecs.types.instance_launch_template.deserialize_aws_json_1_1(
                data["instanceLaunchTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateManagedInstancesProviderConfiguration.instance_launch_template required"
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
