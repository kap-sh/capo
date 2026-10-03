"""Generated from Smithy shape ``com.amazonaws.ecs#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.cluster_configuration
    import capo_ecs.types.cluster_service_connect_defaults_request
    import capo_ecs.types.cluster_settings
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags


class CreateClusterRequest(TypedDict, closed=True):
    cluster_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of your cluster. If you don't specify a name for your cluster, you create a cluster that's named <code>default</code>. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. </p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    settings: NotRequired["capo_ecs.types.cluster_settings.ClusterSettings"]
    """<p>The setting to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p>"""
    configuration: NotRequired[
        "capo_ecs.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>The <code>execute</code> command configuration for the cluster.</p>"""
    capacity_providers: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The short name of one or more capacity providers to associate with the cluster. A capacity provider must be associated with a cluster before it can be included as part of the default capacity provider strategy of the cluster or used in a capacity provider strategy when calling the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> actions.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must be created but not associated with another cluster. New Auto Scaling group capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutCapacityProvider.html">PutCapacityProvider</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>"""
    default_capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to set as the default for the cluster. After a default capacity provider strategy is set for a cluster, when you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> APIs with no capacity provider strategy or launch type specified, the default capacity provider strategy for the cluster is used.</p> <p>If a default capacity provider strategy isn't defined for a cluster when it was created, it can be defined later with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API operation.</p>"""
    service_connect_defaults: NotRequired[
        "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
    ]
    """<p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "settings" in value:
        import capo_ecs.types.cluster_settings

        out["settings"] = capo_ecs.types.cluster_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    if "configuration" in value:
        import capo_ecs.types.cluster_configuration

        out["configuration"] = (
            capo_ecs.types.cluster_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "capacity_providers" in value:
        import capo_ecs.types.string_list

        out["capacityProviders"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["capacity_providers"]
        )
    if "default_capacity_provider_strategy" in value:
        import capo_ecs.types.capacity_provider_strategy

        out["defaultCapacityProviderStrategy"] = (
            capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["default_capacity_provider_strategy"]
            )
        )
    if "service_connect_defaults" in value:
        import capo_ecs.types.cluster_service_connect_defaults_request

        out["serviceConnectDefaults"] = (
            capo_ecs.types.cluster_service_connect_defaults_request.serialize_aws_json_1_1(
                value["service_connect_defaults"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("settings") is not None:
        import capo_ecs.types.cluster_settings

        out["settings"] = capo_ecs.types.cluster_settings.deserialize_aws_json_1_1(
            data["settings"]
        )
    if data.get("configuration") is not None:
        import capo_ecs.types.cluster_configuration

        out["configuration"] = (
            capo_ecs.types.cluster_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("capacityProviders") is not None:
        import capo_ecs.types.string_list

        out["capacity_providers"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["capacityProviders"]
        )
    if data.get("defaultCapacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["default_capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["defaultCapacityProviderStrategy"]
            )
        )
    if data.get("serviceConnectDefaults") is not None:
        import capo_ecs.types.cluster_service_connect_defaults_request

        out["service_connect_defaults"] = (
            capo_ecs.types.cluster_service_connect_defaults_request.deserialize_aws_json_1_1(
                data["serviceConnectDefaults"]
            )
        )
    return out
