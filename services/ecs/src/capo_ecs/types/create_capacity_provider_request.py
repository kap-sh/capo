"""Generated from Smithy shape ``com.amazonaws.ecs#CreateCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.auto_scaling_group_provider
    import capo_ecs.types.create_managed_instances_provider_configuration
    import capo_ecs.types.string
    import capo_ecs.types.tags


class CreateCapacityProviderRequest(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    """<p>The name of the capacity provider. Up to 255 characters are allowed. They include letters (both upper and lowercase letters), numbers, underscores (_), and hyphens (-). The name can't be prefixed with "<code>aws</code>", "<code>ecs</code>", or "<code>fargate</code>".</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the cluster to associate with the capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>"""
    auto_scaling_group_provider: NotRequired[
        "capo_ecs.types.auto_scaling_group_provider.AutoScalingGroupProvider"
    ]
    """<p>The details of the Auto Scaling group for the capacity provider.</p>"""
    managed_instances_provider: NotRequired[
        "capo_ecs.types.create_managed_instances_provider_configuration.CreateManagedInstancesProviderConfiguration"
    ]
    """<p>The configuration for the Amazon ECS Managed Instances provider. This configuration specifies how Amazon ECS manages Amazon EC2 instances on your behalf, including the infrastructure role, instance launch template, and tag propagation settings.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the capacity provider to categorize and organize them more conveniently. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCapacityProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "auto_scaling_group_provider" in value:
        import capo_ecs.types.auto_scaling_group_provider

        out["autoScalingGroupProvider"] = (
            capo_ecs.types.auto_scaling_group_provider.serialize_aws_json_1_1(
                value["auto_scaling_group_provider"]
            )
        )
    if "managed_instances_provider" in value:
        import capo_ecs.types.create_managed_instances_provider_configuration

        out["managedInstancesProvider"] = (
            capo_ecs.types.create_managed_instances_provider_configuration.serialize_aws_json_1_1(
                value["managed_instances_provider"]
            )
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCapacityProviderRequest:
    out: CreateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCapacityProviderRequest.name required")
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("autoScalingGroupProvider") is not None:
        import capo_ecs.types.auto_scaling_group_provider

        out["auto_scaling_group_provider"] = (
            capo_ecs.types.auto_scaling_group_provider.deserialize_aws_json_1_1(
                data["autoScalingGroupProvider"]
            )
        )
    if data.get("managedInstancesProvider") is not None:
        import capo_ecs.types.create_managed_instances_provider_configuration

        out["managed_instances_provider"] = (
            capo_ecs.types.create_managed_instances_provider_configuration.deserialize_aws_json_1_1(
                data["managedInstancesProvider"]
            )
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
