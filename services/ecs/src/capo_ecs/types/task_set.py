"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.deployment_ephemeral_storage
    import capo_ecs.types.integer
    import capo_ecs.types.launch_type
    import capo_ecs.types.load_balancers
    import capo_ecs.types.network_configuration
    import capo_ecs.types.scale
    import capo_ecs.types.service_registries
    import capo_ecs.types.stability_status
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.timestamp


class TaskSet(TypedDict, closed=True):
    id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the task set.</p>"""
    task_set_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task set.</p>"""
    service_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service the task set exists in.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.</p>"""
    started_by: NotRequired["capo_ecs.types.string.String"]
    """<p>The tag specified when a task set is started. If an CodeDeploy deployment created the task set, the <code>startedBy</code> parameter is <code>CODE_DEPLOY</code>. If an external deployment created the task set, the <code>startedBy</code> field isn't used.</p>"""
    external_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The external ID associated with the task set.</p> <p>If an CodeDeploy deployment created a task set, the <code>externalId</code> parameter contains the CodeDeploy deployment ID.</p> <p>If a task set is created for an external deployment and is associated with a service discovery registry, the <code>externalId</code> parameter contains the <code>ECS_TASK_SET_EXTERNAL_ID</code> Cloud Map attribute.</p>"""
    status: NotRequired["capo_ecs.types.string.String"]
    """<p>The status of the task set. The following describes each state.</p> <dl> <dt>PRIMARY</dt> <dd> <p>The task set is serving production traffic.</p> </dd> <dt>ACTIVE</dt> <dd> <p>The task set isn't serving production traffic.</p> </dd> <dt>DRAINING</dt> <dd> <p>The tasks in the task set are being stopped, and their corresponding targets are being deregistered from their target group.</p> </dd> </dl>"""
    task_definition: NotRequired["capo_ecs.types.string.String"]
    """<p>The task definition that the task set is using.</p>"""
    computed_desired_count: "capo_ecs.types.integer.Integer"
    """<p>The computed desired count for the task set. This is calculated by multiplying the service's <code>desiredCount</code> by the task set's <code>scale</code> percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.</p>"""
    pending_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks in the task set that are in the <code>PENDING</code> status during a deployment. A task in the <code>PENDING</code> state is preparing to enter the <code>RUNNING</code> state. A task set enters the <code>PENDING</code> status when it launches for the first time or when it's restarted after being in the <code>STOPPED</code> state.</p>"""
    running_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks in the task set that are in the <code>RUNNING</code> status during a deployment. A task in the <code>RUNNING</code> state is running and ready for use.</p>"""
    created_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task set was created.</p>"""
    updated_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task set was last updated.</p>"""
    launch_type: NotRequired["capo_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the tasks in the task set are using. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy that are associated with the task set.</p>"""
    platform_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The Fargate platform version where the tasks in the task set are running. A platform version is only specified for tasks run on Fargate. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_family: NotRequired["capo_ecs.types.string.String"]
    """<p>The operating system that your tasks in the set are running on. A platform family is specified only for tasks that use the Fargate launch type. </p> <p> All tasks in the set must have the same value.</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the task set.</p>"""
    load_balancers: NotRequired["capo_ecs.types.load_balancers.LoadBalancers"]
    """<p>Details on a load balancer that are used with a task set.</p>"""
    service_registries: NotRequired[
        "capo_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The details for the service discovery registries to assign to this task set. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service discovery</a>.</p>"""
    scale: NotRequired["capo_ecs.types.scale.Scale"]
    """<p>A floating-point percentage of your desired number of tasks to place and keep running in the task set.</p>"""
    stability_status: NotRequired["capo_ecs.types.stability_status.StabilityStatus"]
    """<p>The stability status. This indicates whether the task set has reached a steady state. If the following conditions are met, the task set are in <code>STEADY_STATE</code>:</p> <ul> <li> <p>The task <code>runningCount</code> is equal to the <code>computedDesiredCount</code>.</p> </li> <li> <p>The <code>pendingCount</code> is <code>0</code>.</p> </li> <li> <p>There are no tasks that are running on container instances in the <code>DRAINING</code> status.</p> </li> <li> <p>All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks.</p> </li> </ul> <p>If any of those conditions aren't met, the stability status returns <code>STABILIZING</code>.</p>"""
    stability_status_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task set stability status was retrieved.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    fargate_ephemeral_storage: NotRequired[
        "capo_ecs.types.deployment_ephemeral_storage.DeploymentEphemeralStorage"
    ]
    """<p>The Fargate ephemeral storage settings for the task set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "task_set_arn" in value:
        out["taskSetArn"] = value["task_set_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    out["computedDesiredCount"] = value.get("computed_desired_count", 0)
    out["pendingCount"] = value.get("pending_count", 0)
    out["runningCount"] = value.get("running_count", 0)
    if "created_at" in value:
        import capo_ecs.types.timestamp

        out["createdAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_ecs.types.timestamp

        out["updatedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "launch_type" in value:
        import capo_ecs.types.launch_type

        out["launchType"] = capo_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "capacity_provider_strategy" in value:
        import capo_ecs.types.capacity_provider_strategy

        out["capacityProviderStrategy"] = (
            capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "platform_family" in value:
        out["platformFamily"] = value["platform_family"]
    if "network_configuration" in value:
        import capo_ecs.types.network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "load_balancers" in value:
        import capo_ecs.types.load_balancers

        out["loadBalancers"] = capo_ecs.types.load_balancers.serialize_aws_json_1_1(
            value["load_balancers"]
        )
    if "service_registries" in value:
        import capo_ecs.types.service_registries

        out["serviceRegistries"] = (
            capo_ecs.types.service_registries.serialize_aws_json_1_1(
                value["service_registries"]
            )
        )
    if "scale" in value:
        import capo_ecs.types.scale

        out["scale"] = capo_ecs.types.scale.serialize_aws_json_1_1(value["scale"])
    if "stability_status" in value:
        import capo_ecs.types.stability_status

        out["stabilityStatus"] = capo_ecs.types.stability_status.serialize_aws_json_1_1(
            value["stability_status"]
        )
    if "stability_status_at" in value:
        import capo_ecs.types.timestamp

        out["stabilityStatusAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["stability_status_at"]
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "fargate_ephemeral_storage" in value:
        import capo_ecs.types.deployment_ephemeral_storage

        out["fargateEphemeralStorage"] = (
            capo_ecs.types.deployment_ephemeral_storage.serialize_aws_json_1_1(
                value["fargate_ephemeral_storage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskSet:
    out: TaskSet = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("taskSetArn") is not None:
        out["task_set_arn"] = data["taskSetArn"]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("startedBy") is not None:
        out["started_by"] = data["startedBy"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    if data.get("computedDesiredCount") is not None:
        out["computed_desired_count"] = data["computedDesiredCount"]
    else:
        out["computed_desired_count"] = 0
    if data.get("pendingCount") is not None:
        out["pending_count"] = data["pendingCount"]
    else:
        out["pending_count"] = 0
    if data.get("runningCount") is not None:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    if data.get("createdAt") is not None:
        import capo_ecs.types.timestamp

        out["created_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_ecs.types.timestamp

        out["updated_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
    if data.get("launchType") is not None:
        import capo_ecs.types.launch_type

        out["launch_type"] = capo_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if data.get("capacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["capacityProviderStrategy"]
            )
        )
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("platformFamily") is not None:
        out["platform_family"] = data["platformFamily"]
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.network_configuration

        out["network_configuration"] = (
            capo_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("loadBalancers") is not None:
        import capo_ecs.types.load_balancers

        out["load_balancers"] = capo_ecs.types.load_balancers.deserialize_aws_json_1_1(
            data["loadBalancers"]
        )
    if data.get("serviceRegistries") is not None:
        import capo_ecs.types.service_registries

        out["service_registries"] = (
            capo_ecs.types.service_registries.deserialize_aws_json_1_1(
                data["serviceRegistries"]
            )
        )
    if data.get("scale") is not None:
        import capo_ecs.types.scale

        out["scale"] = capo_ecs.types.scale.deserialize_aws_json_1_1(data["scale"])
    if data.get("stabilityStatus") is not None:
        import capo_ecs.types.stability_status

        out["stability_status"] = (
            capo_ecs.types.stability_status.deserialize_aws_json_1_1(
                data["stabilityStatus"]
            )
        )
    if data.get("stabilityStatusAt") is not None:
        import capo_ecs.types.timestamp

        out["stability_status_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["stabilityStatusAt"]
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("fargateEphemeralStorage") is not None:
        import capo_ecs.types.deployment_ephemeral_storage

        out["fargate_ephemeral_storage"] = (
            capo_ecs.types.deployment_ephemeral_storage.deserialize_aws_json_1_1(
                data["fargateEphemeralStorage"]
            )
        )
    return out
