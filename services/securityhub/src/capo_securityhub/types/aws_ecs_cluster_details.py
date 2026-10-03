"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ecs_cluster_cluster_settings_list
    import capo_securityhub.types.aws_ecs_cluster_configuration_details
    import capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEcsClusterDetails(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) that identifies the cluster. </p>"""
    active_services_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of services that are running on the cluster in an <code>ACTIVE</code> state. You can view these services with the Amazon ECS <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html"> <code>ListServices</code> </a> API operation. </p>"""
    capacity_providers: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The short name of one or more capacity providers to associate with the cluster.</p>"""
    cluster_settings: NotRequired[
        "capo_securityhub.types.aws_ecs_cluster_cluster_settings_list.AwsEcsClusterClusterSettingsList"
    ]
    """<p>The setting to use to create the cluster. Specifically used to configure whether to enable CloudWatch Container Insights for the cluster.</p>"""
    configuration: NotRequired[
        "capo_securityhub.types.aws_ecs_cluster_configuration_details.AwsEcsClusterConfigurationDetails"
    ]
    """<p>The run command configuration for the cluster.</p>"""
    default_capacity_provider_strategy: NotRequired[
        "capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list.AwsEcsClusterDefaultCapacityProviderStrategyList"
    ]
    """<p>The default capacity provider strategy for the cluster. The default capacity provider strategy is used when services or tasks are run without a specified launch type or capacity provider strategy.</p>"""
    cluster_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A name that you use to identify your cluster. </p>"""
    registered_container_instances_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of container instances registered into the cluster. This includes container instances in both <code>ACTIVE</code> and <code>DRAINING</code> status. </p>"""
    running_tasks_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of tasks in the cluster that are in the <code>RUNNING</code> state. </p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the cluster. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsClusterDetails) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "active_services_count" in value:
        out["ActiveServicesCount"] = value["active_services_count"]
    if "capacity_providers" in value:
        import capo_securityhub.types.non_empty_string_list

        out["CapacityProviders"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["capacity_providers"]
            )
        )
    if "cluster_settings" in value:
        import capo_securityhub.types.aws_ecs_cluster_cluster_settings_list

        out["ClusterSettings"] = (
            capo_securityhub.types.aws_ecs_cluster_cluster_settings_list.serialize_json(
                value["cluster_settings"]
            )
        )
    if "configuration" in value:
        import capo_securityhub.types.aws_ecs_cluster_configuration_details

        out["Configuration"] = (
            capo_securityhub.types.aws_ecs_cluster_configuration_details.serialize_json(
                value["configuration"]
            )
        )
    if "default_capacity_provider_strategy" in value:
        import capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list

        out["DefaultCapacityProviderStrategy"] = (
            capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list.serialize_json(
                value["default_capacity_provider_strategy"]
            )
        )
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "registered_container_instances_count" in value:
        out["RegisteredContainerInstancesCount"] = value[
            "registered_container_instances_count"
        ]
    if "running_tasks_count" in value:
        out["RunningTasksCount"] = value["running_tasks_count"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsEcsClusterDetails:
    out: AwsEcsClusterDetails = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("ActiveServicesCount") is not None:
        out["active_services_count"] = data["ActiveServicesCount"]
    if data.get("CapacityProviders") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["capacity_providers"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["CapacityProviders"]
            )
        )
    if data.get("ClusterSettings") is not None:
        import capo_securityhub.types.aws_ecs_cluster_cluster_settings_list

        out["cluster_settings"] = (
            capo_securityhub.types.aws_ecs_cluster_cluster_settings_list.deserialize_json(
                data["ClusterSettings"]
            )
        )
    if data.get("Configuration") is not None:
        import capo_securityhub.types.aws_ecs_cluster_configuration_details

        out["configuration"] = (
            capo_securityhub.types.aws_ecs_cluster_configuration_details.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("DefaultCapacityProviderStrategy") is not None:
        import capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list

        out["default_capacity_provider_strategy"] = (
            capo_securityhub.types.aws_ecs_cluster_default_capacity_provider_strategy_list.deserialize_json(
                data["DefaultCapacityProviderStrategy"]
            )
        )
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("RegisteredContainerInstancesCount") is not None:
        out["registered_container_instances_count"] = data[
            "RegisteredContainerInstancesCount"
        ]
    if data.get("RunningTasksCount") is not None:
        out["running_tasks_count"] = data["RunningTasksCount"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out
