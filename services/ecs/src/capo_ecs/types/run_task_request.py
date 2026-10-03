"""Generated from Smithy shape ``com.amazonaws.ecs#RunTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.launch_type
    import capo_ecs.types.network_configuration
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.task_override
    import capo_ecs.types.task_volume_configurations


class RunTaskRequest(TypedDict, closed=True):
    capacity_provider_strategy: NotRequired[
        "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.</p> <p>Each account receives a default cluster the first time you use the service, but you may also create other clusters.</p>"""
    count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.</p>"""
    enable_ecs_managed_tags: "capo_ecs.types.boolean.Boolean"
    """<p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the execute command functionality for the containers in this task. If <code>true</code>, this enables execute command functionality on all containers in the task.</p> <p>If <code>true</code>, then the task definition must have a task role, or you must provide one as an override.</p>"""
    group: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, <code>family:my-family-name</code>).</p>"""
    launch_type: NotRequired["capo_ecs.types.launch_type.LaunchType"]
    """<p>The infrastructure to run your standalone task on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A task can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the task. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    overrides: NotRequired["capo_ecs.types.task_override.TaskOverride"]
    """<p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p>"""
    placement_constraints: NotRequired[
        "capo_ecs.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).</p>"""
    placement_strategy: NotRequired[
        "capo_ecs.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.</p>"""
    platform_version: NotRequired["capo_ecs.types.string.String"]
    """<p>The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_tags.PropagateTags"]
    """<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the<a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <note> <p>An error will be received if you specify the <code>SERVICE</code> option when running a task.</p> </note>"""
    reference_id: NotRequired["capo_ecs.types.string.String"]
    """<p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>"""
    started_by: NotRequired["capo_ecs.types.string.String"]
    """<p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, then the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    task_definition: "capo_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>The full ARN value must match the value that you specified as the <code>Resource</code> of the principal's permissions policy.</p> <p>When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.</p> <p>To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2</code>.</p> <p>To specify all revisions, use the wildcard (*) in the ARN. For example, to specify all revisions, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">Policy Resources for Amazon ECS</a> in the Amazon Elastic Container Service Developer Guide.</p>"""
    client_token: NotRequired["capo_ecs.types.string.String"]
    """<p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html">Ensuring idempotency</a>.</p>"""
    volume_configurations: NotRequired[
        "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
    ]
    """<p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunTaskRequest) -> dict:
    out: dict = {}
    if "capacity_provider_strategy" in value:
        import capo_ecs.types.capacity_provider_strategy

        out["capacityProviderStrategy"] = (
            capo_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "count" in value:
        out["count"] = value["count"]
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    if "group" in value:
        out["group"] = value["group"]
    if "launch_type" in value:
        import capo_ecs.types.launch_type

        out["launchType"] = capo_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "network_configuration" in value:
        import capo_ecs.types.network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "overrides" in value:
        import capo_ecs.types.task_override

        out["overrides"] = capo_ecs.types.task_override.serialize_aws_json_1_1(
            value["overrides"]
        )
    if "placement_constraints" in value:
        import capo_ecs.types.placement_constraints

        out["placementConstraints"] = (
            capo_ecs.types.placement_constraints.serialize_aws_json_1_1(
                value["placement_constraints"]
            )
        )
    if "placement_strategy" in value:
        import capo_ecs.types.placement_strategies

        out["placementStrategy"] = (
            capo_ecs.types.placement_strategies.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_tags

        out["propagateTags"] = capo_ecs.types.propagate_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    if "reference_id" in value:
        out["referenceId"] = value["reference_id"]
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    out["taskDefinition"] = value["task_definition"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "volume_configurations" in value:
        import capo_ecs.types.task_volume_configurations

        out["volumeConfigurations"] = (
            capo_ecs.types.task_volume_configurations.serialize_aws_json_1_1(
                value["volume_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunTaskRequest:
    out: RunTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderStrategy") is not None:
        import capo_ecs.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["capacityProviderStrategy"]
            )
        )
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("enableECSManagedTags") is not None:
        out["enable_ecs_managed_tags"] = data["enableECSManagedTags"]
    else:
        out["enable_ecs_managed_tags"] = False
    if data.get("enableExecuteCommand") is not None:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if data.get("group") is not None:
        out["group"] = data["group"]
    if data.get("launchType") is not None:
        import capo_ecs.types.launch_type

        out["launch_type"] = capo_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.network_configuration

        out["network_configuration"] = (
            capo_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("overrides") is not None:
        import capo_ecs.types.task_override

        out["overrides"] = capo_ecs.types.task_override.deserialize_aws_json_1_1(
            data["overrides"]
        )
    if data.get("placementConstraints") is not None:
        import capo_ecs.types.placement_constraints

        out["placement_constraints"] = (
            capo_ecs.types.placement_constraints.deserialize_aws_json_1_1(
                data["placementConstraints"]
            )
        )
    if data.get("placementStrategy") is not None:
        import capo_ecs.types.placement_strategies

        out["placement_strategy"] = (
            capo_ecs.types.placement_strategies.deserialize_aws_json_1_1(
                data["placementStrategy"]
            )
        )
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_tags

        out["propagate_tags"] = capo_ecs.types.propagate_tags.deserialize_aws_json_1_1(
            data["propagateTags"]
        )
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    if data.get("startedBy") is not None:
        out["started_by"] = data["startedBy"]
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("taskDefinition") is not None:
        out["task_definition"] = data["taskDefinition"]
    else:
        raise DeserializationError("RunTaskRequest.task_definition required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("volumeConfigurations") is not None:
        import capo_ecs.types.task_volume_configurations

        out["volume_configurations"] = (
            capo_ecs.types.task_volume_configurations.deserialize_aws_json_1_1(
                data["volumeConfigurations"]
            )
        )
    return out
