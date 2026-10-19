"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateCapacityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.auto_scaling_group_provider_update
    import capo_ecs.types.string
    import capo_ecs.types.update_managed_instances_provider_configuration


class UpdateCapacityProviderRequest(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    """<p>The name of the capacity provider to update.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the cluster that contains the capacity provider to update. Managed instances capacity providers are cluster-scoped and can only be updated within their associated cluster.</p>"""
    auto_scaling_group_provider: NotRequired[
        "capo_ecs.types.auto_scaling_group_provider_update.AutoScalingGroupProviderUpdate"
    ]
    """<p>An object that represent the parameters to update for the Auto Scaling group capacity provider.</p>"""
    managed_instances_provider: NotRequired[
        "capo_ecs.types.update_managed_instances_provider_configuration.UpdateManagedInstancesProviderConfiguration"
    ]
    """<p>The updated configuration for the Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes take effect for new instances launched after the update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCapacityProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "auto_scaling_group_provider" in value:
        import capo_ecs.types.auto_scaling_group_provider_update

        out["autoScalingGroupProvider"] = (
            capo_ecs.types.auto_scaling_group_provider_update.serialize_aws_json_1_1(
                value["auto_scaling_group_provider"]
            )
        )
    if "managed_instances_provider" in value:
        import capo_ecs.types.update_managed_instances_provider_configuration

        out["managedInstancesProvider"] = (
            capo_ecs.types.update_managed_instances_provider_configuration.serialize_aws_json_1_1(
                value["managed_instances_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCapacityProviderRequest:
    out: UpdateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("autoScalingGroupProvider") is not None:
        import capo_ecs.types.auto_scaling_group_provider_update

        out["auto_scaling_group_provider"] = (
            capo_ecs.types.auto_scaling_group_provider_update.deserialize_aws_json_1_1(
                data["autoScalingGroupProvider"]
            )
        )
    if data.get("managedInstancesProvider") is not None:
        import capo_ecs.types.update_managed_instances_provider_configuration

        out["managed_instances_provider"] = (
            capo_ecs.types.update_managed_instances_provider_configuration.deserialize_aws_json_1_1(
                data["managedInstancesProvider"]
            )
        )
    return out
