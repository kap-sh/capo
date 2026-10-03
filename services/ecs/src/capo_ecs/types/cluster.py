"""Generated from Smithy shape ``com.amazonaws.ecs#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.attachments
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.cluster_configuration
    import capo_ecs.types.cluster_service_connect_defaults
    import capo_ecs.types.cluster_settings
    import capo_ecs.types.integer
    import capo_ecs.types.statistics
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags


class Cluster(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the cluster. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    cluster_name: NotRequired["capo_ecs.types.string.String"]
    """<p>A user-generated string that you use to identify your cluster.</p>"""
    configuration: NotRequired[
        "capo_ecs.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>The execute command and managed storage configuration for the cluster.</p>"""
    status: NotRequired["capo_ecs.types.string.String"]
    """<p>The status of the cluster. The following are the possible states that are returned.</p> <dl> <dt>ACTIVE</dt> <dd> <p>The cluster is ready to accept tasks and if applicable you can register container instances with the cluster.</p> </dd> <dt>PROVISIONING</dt> <dd> <p>The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being created.</p> </dd> <dt>DEPROVISIONING</dt> <dd> <p>The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being deleted.</p> </dd> <dt>FAILED</dt> <dd> <p>The cluster has capacity providers that are associated with it and the resources needed for the capacity provider have failed to create.</p> </dd> <dt>INACTIVE</dt> <dd> <p>The cluster has been deleted. Clusters with an <code>INACTIVE</code> status may remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> clusters persisting.</p> </dd> </dl>"""
    registered_container_instances_count: "capo_ecs.types.integer.Integer"
    """<p>The number of container instances registered into the cluster. This includes container instances in both <code>ACTIVE</code> and <code>DRAINING</code> status.</p>"""
    running_tasks_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>RUNNING</code> state.</p>"""
    pending_tasks_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks in the cluster that are in the <code>PENDING</code> state.</p>"""
    active_services_count: "capo_ecs.types.integer.Integer"
    """<p>The number of services that are running on the cluster in an <code>ACTIVE</code> state. You can view these services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>.</p>"""
    statistics: NotRequired["capo_ecs.types.statistics.Statistics"]
    """<p>Additional information about your clusters that are separated by launch type. They include the following:</p> <ul> <li> <p>runningEC2TasksCount</p> </li> <li> <p>RunningFargateTasksCount</p> </li> <li> <p>pendingEC2TasksCount</p> </li> <li> <p>pendingFargateTasksCount</p> </li> <li> <p>activeEC2ServiceCount</p> </li> <li> <p>activeFargateServiceCount</p> </li> <li> <p>drainingEC2ServiceCount</p> </li> <li> <p>drainingFargateServiceCount</p> </li> </ul>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    settings: NotRequired["capo_ecs.types.cluster_settings.ClusterSettings"]
    """<p>The settings for the cluster. This parameter indicates whether CloudWatch Container Insights is on or off for a cluster.</p>"""
    capacity_providers: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The capacity providers associated with the cluster.</p>"""
    default_capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The default capacity provider strategy for the cluster. When services or tasks are run in the cluster with no launch type or capacity provider strategy specified, the default capacity provider strategy is used.</p>"""
    attachments: NotRequired["capo_ecs.types.attachments.Attachments"]
    """<p>The resources attached to a cluster. When using a capacity provider with a cluster, the capacity provider and associated resources are returned as cluster attachments.</p>"""
    attachments_status: NotRequired["capo_ecs.types.string.String"]
    """<p>The status of the capacity providers associated with the cluster. The following are the states that are returned.</p> <dl> <dt>UPDATE_IN_PROGRESS</dt> <dd> <p>The available capacity providers for the cluster are updating.</p> </dd> <dt>UPDATE_COMPLETE</dt> <dd> <p>The capacity providers have successfully updated.</p> </dd> <dt>UPDATE_FAILED</dt> <dd> <p>The capacity provider updates failed.</p> </dd> </dl>"""
    service_connect_defaults: NotRequired[
        "capo_ecs.types.cluster_service_connect_defaults.ClusterServiceConnectDefaults"
    ]
    """<p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cluster) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "configuration" in value:
        import capo_ecs.types.cluster_configuration

        out["configuration"] = (
            capo_ecs.types.cluster_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    out["registeredContainerInstancesCount"] = value.get(
        "registered_container_instances_count", 0
    )
    out["runningTasksCount"] = value.get("running_tasks_count", 0)
    out["pendingTasksCount"] = value.get("pending_tasks_count", 0)
    out["activeServicesCount"] = value.get("active_services_count", 0)
    if "statistics" in value:
        import capo_ecs.types.statistics

        out["statistics"] = capo_ecs.types.statistics.serialize_aws_json_1_1(
            value["statistics"]
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "settings" in value:
        import capo_ecs.types.cluster_settings

        out["settings"] = capo_ecs.types.cluster_settings.serialize_aws_json_1_1(
            value["settings"]
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
    if "attachments" in value:
        import capo_ecs.types.attachments

        out["attachments"] = capo_ecs.types.attachments.serialize_aws_json_1_1(
            value["attachments"]
        )
    if "attachments_status" in value:
        out["attachmentsStatus"] = value["attachments_status"]
    if "service_connect_defaults" in value:
        import capo_ecs.types.cluster_service_connect_defaults

        out["serviceConnectDefaults"] = (
            capo_ecs.types.cluster_service_connect_defaults.serialize_aws_json_1_1(
                value["service_connect_defaults"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("configuration") is not None:
        import capo_ecs.types.cluster_configuration

        out["configuration"] = (
            capo_ecs.types.cluster_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("registeredContainerInstancesCount") is not None:
        out["registered_container_instances_count"] = data[
            "registeredContainerInstancesCount"
        ]
    else:
        out["registered_container_instances_count"] = 0
    if data.get("runningTasksCount") is not None:
        out["running_tasks_count"] = data["runningTasksCount"]
    else:
        out["running_tasks_count"] = 0
    if data.get("pendingTasksCount") is not None:
        out["pending_tasks_count"] = data["pendingTasksCount"]
    else:
        out["pending_tasks_count"] = 0
    if data.get("activeServicesCount") is not None:
        out["active_services_count"] = data["activeServicesCount"]
    else:
        out["active_services_count"] = 0
    if data.get("statistics") is not None:
        import capo_ecs.types.statistics

        out["statistics"] = capo_ecs.types.statistics.deserialize_aws_json_1_1(
            data["statistics"]
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("settings") is not None:
        import capo_ecs.types.cluster_settings

        out["settings"] = capo_ecs.types.cluster_settings.deserialize_aws_json_1_1(
            data["settings"]
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
    if data.get("attachments") is not None:
        import capo_ecs.types.attachments

        out["attachments"] = capo_ecs.types.attachments.deserialize_aws_json_1_1(
            data["attachments"]
        )
    if data.get("attachmentsStatus") is not None:
        out["attachments_status"] = data["attachmentsStatus"]
    if data.get("serviceConnectDefaults") is not None:
        import capo_ecs.types.cluster_service_connect_defaults

        out["service_connect_defaults"] = (
            capo_ecs.types.cluster_service_connect_defaults.deserialize_aws_json_1_1(
                data["serviceConnectDefaults"]
            )
        )
    return out
