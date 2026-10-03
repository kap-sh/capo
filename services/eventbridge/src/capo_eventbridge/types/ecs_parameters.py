"""Generated from Smithy shape ``com.amazonaws.eventbridge#EcsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.arn
    import capo_eventbridge.types.boolean
    import capo_eventbridge.types.capacity_provider_strategy
    import capo_eventbridge.types.launch_type
    import capo_eventbridge.types.limit_min1
    import capo_eventbridge.types.network_configuration
    import capo_eventbridge.types.placement_constraints
    import capo_eventbridge.types.placement_strategies
    import capo_eventbridge.types.propagate_tags
    import capo_eventbridge.types.reference_id
    import capo_eventbridge.types.string
    import capo_eventbridge.types.tag_list


class EcsParameters(TypedDict, closed=True):
    task_definition_arn: "capo_eventbridge.types.arn.Arn"
    """<p>The ARN of the task definition to use if the event target is an Amazon ECS task. </p>"""
    task_count: NotRequired["capo_eventbridge.types.limit_min1.LimitMin1"]
    """<p>The number of tasks to create based on <code>TaskDefinition</code>. The default is 1.</p>"""
    launch_type: NotRequired["capo_eventbridge.types.launch_type.LaunchType"]
    """<p>Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The <code>FARGATE</code> value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html">Fargate on Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    network_configuration: NotRequired[
        "capo_eventbridge.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Use this structure if the Amazon ECS task uses the <code>awsvpc</code> network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if <code>LaunchType</code> is <code>FARGATE</code> because the <code>awsvpc</code> mode is required for Fargate tasks.</p> <p>If you specify <code>NetworkConfiguration</code> when the target ECS task does not use the <code>awsvpc</code> network mode, the task fails.</p>"""
    platform_version: NotRequired["capo_eventbridge.types.string.String"]
    """<p>Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as <code>1.1.0</code>.</p> <p>This structure is used only if <code>LaunchType</code> is <code>FARGATE</code>. For more information about valid platform versions, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    group: NotRequired["capo_eventbridge.types.string.String"]
    """<p>Specifies an ECS task group for the task. The maximum length is 255 characters.</p>"""
    capacity_provider_strategy: NotRequired[
        "capo_eventbridge.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or launchType is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used. </p>"""
    enable_ecs_managed_tags: "capo_eventbridge.types.boolean.Boolean"
    """<p>Specifies whether to enable Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the Amazon Elastic Container Service Developer Guide. </p>"""
    enable_execute_command: "capo_eventbridge.types.boolean.Boolean"
    """<p>Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.</p>"""
    placement_constraints: NotRequired[
        "capo_eventbridge.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).</p>"""
    placement_strategy: NotRequired[
        "capo_eventbridge.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task. </p>"""
    propagate_tags: NotRequired["capo_eventbridge.types.propagate_tags.PropagateTags"]
    """<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the TagResource API action. </p>"""
    reference_id: NotRequired["capo_eventbridge.types.reference_id.ReferenceId"]
    """<p>The reference ID to use for the task.</p>"""
    tags: NotRequired["capo_eventbridge.types.tag_list.TagList"]
    """<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags">RunTask</a> in the Amazon ECS API Reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EcsParameters) -> dict:
    out: dict = {}
    out["TaskDefinitionArn"] = value["task_definition_arn"]
    if "task_count" in value:
        out["TaskCount"] = value["task_count"]
    if "launch_type" in value:
        import capo_eventbridge.types.launch_type

        out["LaunchType"] = capo_eventbridge.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "network_configuration" in value:
        import capo_eventbridge.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_eventbridge.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "group" in value:
        out["Group"] = value["group"]
    if "capacity_provider_strategy" in value:
        import capo_eventbridge.types.capacity_provider_strategy

        out["CapacityProviderStrategy"] = (
            capo_eventbridge.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    out["EnableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["EnableExecuteCommand"] = value.get("enable_execute_command", False)
    if "placement_constraints" in value:
        import capo_eventbridge.types.placement_constraints

        out["PlacementConstraints"] = (
            capo_eventbridge.types.placement_constraints.serialize_aws_json_1_1(
                value["placement_constraints"]
            )
        )
    if "placement_strategy" in value:
        import capo_eventbridge.types.placement_strategies

        out["PlacementStrategy"] = (
            capo_eventbridge.types.placement_strategies.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    if "propagate_tags" in value:
        import capo_eventbridge.types.propagate_tags

        out["PropagateTags"] = (
            capo_eventbridge.types.propagate_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "tags" in value:
        import capo_eventbridge.types.tag_list

        out["Tags"] = capo_eventbridge.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EcsParameters:
    out: EcsParameters = {}  # type: ignore[typeddict-item]
    if data.get("TaskDefinitionArn") is not None:
        out["task_definition_arn"] = data["TaskDefinitionArn"]
    else:
        raise DeserializationError("EcsParameters.task_definition_arn required")
    if data.get("TaskCount") is not None:
        out["task_count"] = data["TaskCount"]
    if data.get("LaunchType") is not None:
        import capo_eventbridge.types.launch_type

        out["launch_type"] = (
            capo_eventbridge.types.launch_type.deserialize_aws_json_1_1(
                data["LaunchType"]
            )
        )
    if data.get("NetworkConfiguration") is not None:
        import capo_eventbridge.types.network_configuration

        out["network_configuration"] = (
            capo_eventbridge.types.network_configuration.deserialize_aws_json_1_1(
                data["NetworkConfiguration"]
            )
        )
    if data.get("PlatformVersion") is not None:
        out["platform_version"] = data["PlatformVersion"]
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    if data.get("CapacityProviderStrategy") is not None:
        import capo_eventbridge.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            capo_eventbridge.types.capacity_provider_strategy.deserialize_aws_json_1_1(
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
        import capo_eventbridge.types.placement_constraints

        out["placement_constraints"] = (
            capo_eventbridge.types.placement_constraints.deserialize_aws_json_1_1(
                data["PlacementConstraints"]
            )
        )
    if data.get("PlacementStrategy") is not None:
        import capo_eventbridge.types.placement_strategies

        out["placement_strategy"] = (
            capo_eventbridge.types.placement_strategies.deserialize_aws_json_1_1(
                data["PlacementStrategy"]
            )
        )
    if data.get("PropagateTags") is not None:
        import capo_eventbridge.types.propagate_tags

        out["propagate_tags"] = (
            capo_eventbridge.types.propagate_tags.deserialize_aws_json_1_1(
                data["PropagateTags"]
            )
        )
    if data.get("ReferenceId") is not None:
        out["reference_id"] = data["ReferenceId"]
    if data.get("Tags") is not None:
        import capo_eventbridge.types.tag_list

        out["tags"] = capo_eventbridge.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
