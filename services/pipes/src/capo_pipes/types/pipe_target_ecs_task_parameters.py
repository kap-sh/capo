"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetEcsTaskParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.arn_or_json_path
    import capo_pipes.types.boolean
    import capo_pipes.types.capacity_provider_strategy
    import capo_pipes.types.ecs_task_override
    import capo_pipes.types.launch_type
    import capo_pipes.types.limit_min1
    import capo_pipes.types.network_configuration
    import capo_pipes.types.placement_constraints
    import capo_pipes.types.placement_strategies
    import capo_pipes.types.propagate_tags
    import capo_pipes.types.reference_id
    import capo_pipes.types.string
    import capo_pipes.types.tag_list


class PipeTargetEcsTaskParameters(TypedDict, closed=True):
    task_definition_arn: "capo_pipes.types.arn_or_json_path.ArnOrJsonPath"
    """<p>The ARN of the task definition to use if the event target is an Amazon ECS task. </p>"""
    task_count: NotRequired["capo_pipes.types.limit_min1.LimitMin1"]
    """<p>The number of tasks to create based on <code>TaskDefinition</code>. The default is 1.</p>"""
    launch_type: NotRequired["capo_pipes.types.launch_type.LaunchType"]
    """<p>Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The <code>FARGATE</code> value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html">Fargate on Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    network_configuration: NotRequired[
        "capo_pipes.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Use this structure if the Amazon ECS task uses the <code>awsvpc</code> network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if <code>LaunchType</code> is <code>FARGATE</code> because the <code>awsvpc</code> mode is required for Fargate tasks.</p> <p>If you specify <code>NetworkConfiguration</code> when the target ECS task does not use the <code>awsvpc</code> network mode, the task fails.</p>"""
    platform_version: NotRequired["capo_pipes.types.string.String"]
    """<p>Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as <code>1.1.0</code>.</p> <p>This structure is used only if <code>LaunchType</code> is <code>FARGATE</code>. For more information about valid platform versions, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    group: NotRequired["capo_pipes.types.string.String"]
    """<p>Specifies an Amazon ECS task group for the task. The maximum length is 255 characters.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_pipes.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or launchType is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used. </p>"""
    enable_ecs_managed_tags: "capo_pipes.types.boolean.Boolean"
    """<p>Specifies whether to enable Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the Amazon Elastic Container Service Developer Guide. </p>"""
    enable_execute_command: "capo_pipes.types.boolean.Boolean"
    """<p>Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.</p>"""
    placement_constraints: NotRequired[
        "capo_pipes.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).</p>"""
    placement_strategy: NotRequired[
        "capo_pipes.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task. </p>"""
    propagate_tags: NotRequired["capo_pipes.types.propagate_tags.PropagateTags"]
    """<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the <code>TagResource</code> API action. </p>"""
    reference_id: NotRequired["capo_pipes.types.reference_id.ReferenceId"]
    """<p>The reference ID to use for the task.</p>"""
    overrides: NotRequired["capo_pipes.types.ecs_task_override.EcsTaskOverride"]
    """<p>The overrides that are associated with a task.</p>"""
    tags: NotRequired["capo_pipes.types.tag_list.TagList"]
    """<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags">RunTask</a> in the Amazon ECS API Reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetEcsTaskParameters) -> dict:
    out: dict = {}
    out["TaskDefinitionArn"] = value["task_definition_arn"]
    if "task_count" in value:
        out["TaskCount"] = value["task_count"]
    if "launch_type" in value:
        out["LaunchType"] = value["launch_type"]
    if "network_configuration" in value:
        import capo_pipes.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_pipes.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "group" in value:
        out["Group"] = value["group"]
    if "capacity_provider_strategy" in value:
        import capo_pipes.types.capacity_provider_strategy

        out["CapacityProviderStrategy"] = (
            capo_pipes.types.capacity_provider_strategy.serialize_json(
                value["capacity_provider_strategy"]
            )
        )
    out["EnableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["EnableExecuteCommand"] = value.get("enable_execute_command", False)
    if "placement_constraints" in value:
        import capo_pipes.types.placement_constraints

        out["PlacementConstraints"] = (
            capo_pipes.types.placement_constraints.serialize_json(
                value["placement_constraints"]
            )
        )
    if "placement_strategy" in value:
        import capo_pipes.types.placement_strategies

        out["PlacementStrategy"] = capo_pipes.types.placement_strategies.serialize_json(
            value["placement_strategy"]
        )
    if "propagate_tags" in value:
        out["PropagateTags"] = value["propagate_tags"]
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "overrides" in value:
        import capo_pipes.types.ecs_task_override

        out["Overrides"] = capo_pipes.types.ecs_task_override.serialize_json(
            value["overrides"]
        )
    if "tags" in value:
        import capo_pipes.types.tag_list

        out["Tags"] = capo_pipes.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PipeTargetEcsTaskParameters:
    out: PipeTargetEcsTaskParameters = {}  # type: ignore[typeddict-item]
    if data.get("TaskDefinitionArn") is not None:
        out["task_definition_arn"] = data["TaskDefinitionArn"]
    else:
        raise DeserializationError(
            "PipeTargetEcsTaskParameters.task_definition_arn required"
        )
    if data.get("TaskCount") is not None:
        out["task_count"] = data["TaskCount"]
    if data.get("LaunchType") is not None:
        out["launch_type"] = data["LaunchType"]
    if data.get("NetworkConfiguration") is not None:
        import capo_pipes.types.network_configuration

        out["network_configuration"] = (
            capo_pipes.types.network_configuration.deserialize_json(
                data["NetworkConfiguration"]
            )
        )
    if data.get("PlatformVersion") is not None:
        out["platform_version"] = data["PlatformVersion"]
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    if data.get("CapacityProviderStrategy") is not None:
        import capo_pipes.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_pipes.types.capacity_provider_strategy.deserialize_json(
                data["CapacityProviderStrategy"]
            )
        )
    if data.get("EnableECSManagedTags") is not None:
        out["enable_ecs_managed_tags"] = data["EnableECSManagedTags"]
    else:
        out["enable_ecs_managed_tags"] = False
    if data.get("EnableExecuteCommand") is not None:
        out["enable_execute_command"] = data["EnableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if data.get("PlacementConstraints") is not None:
        import capo_pipes.types.placement_constraints

        out["placement_constraints"] = (
            capo_pipes.types.placement_constraints.deserialize_json(
                data["PlacementConstraints"]
            )
        )
    if data.get("PlacementStrategy") is not None:
        import capo_pipes.types.placement_strategies

        out["placement_strategy"] = (
            capo_pipes.types.placement_strategies.deserialize_json(
                data["PlacementStrategy"]
            )
        )
    if data.get("PropagateTags") is not None:
        out["propagate_tags"] = data["PropagateTags"]
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    if data.get("Overrides") is not None:
        import capo_pipes.types.ecs_task_override

        out["overrides"] = capo_pipes.types.ecs_task_override.deserialize_json(
            data["Overrides"]
        )
    if data.get("Tags") is not None:
        import capo_pipes.types.tag_list

        out["tags"] = capo_pipes.types.tag_list.deserialize_json(data["Tags"])
    return out
