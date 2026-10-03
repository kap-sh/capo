"""Generated from Smithy shape ``com.amazonaws.ecs#StartTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.network_configuration
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags
    import capo_ecs.types.task_override
    import capo_ecs.types.task_volume_configurations


class StartTaskRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster where to start your task. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instances: "capo_ecs.types.string_list.StringList"
    """<p>The container instance IDs or full ARN entries for the container instances where you would like to place your task. You can specify up to 10 container instances.</p>"""
    enable_ecs_managed_tags: "capo_ecs.types.boolean.Boolean"
    """<p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "capo_ecs.types.boolean.Boolean"
    """<p>Whether or not the execute command functionality is turned on for the task. If <code>true</code>, this turns on the execute command functionality on all containers in the task.</p>"""
    group: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).</p>"""
    network_configuration: NotRequired[
        "capo_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>"""
    overrides: NotRequired["capo_ecs.types.task_override.TaskOverride"]
    """<p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it receives. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <note> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p> </note>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_tags.PropagateTags"]
    """<p>Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p>"""
    reference_id: NotRequired["capo_ecs.types.string.String"]
    """<p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>"""
    started_by: NotRequired["capo_ecs.types.string.String"]
    """<p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 36 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    task_definition: "capo_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to start. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p>"""
    volume_configurations: NotRequired[
        "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
    ]
    """<p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTaskRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import capo_ecs.types.string_list

    out["containerInstances"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["container_instances"]
    )
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    if "group" in value:
        out["group"] = value["group"]
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
    if "volume_configurations" in value:
        import capo_ecs.types.task_volume_configurations

        out["volumeConfigurations"] = (
            capo_ecs.types.task_volume_configurations.serialize_aws_json_1_1(
                value["volume_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTaskRequest:
    out: StartTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("containerInstances") is not None:
        import capo_ecs.types.string_list

        out["container_instances"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["containerInstances"]
            )
        )
    else:
        raise DeserializationError("StartTaskRequest.container_instances required")
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
        raise DeserializationError("StartTaskRequest.task_definition required")
    if data.get("volumeConfigurations") is not None:
        import capo_ecs.types.task_volume_configurations

        out["volume_configurations"] = (
            capo_ecs.types.task_volume_configurations.deserialize_aws_json_1_1(
                data["volumeConfigurations"]
            )
        )
    return out
