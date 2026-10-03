"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.agent_update_status
    import capo_ecs.types.attachments
    import capo_ecs.types.attributes
    import capo_ecs.types.boolean
    import capo_ecs.types.container_instance_health_status
    import capo_ecs.types.integer
    import capo_ecs.types.long
    import capo_ecs.types.resources
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.timestamp
    import capo_ecs.types.version_info


class ContainerInstance(TypedDict, closed=True):
    container_instance_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container instance. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    ec2_instance_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the container instance. For Amazon EC2 instances, this value is the Amazon EC2 instance ID. For external instances, this value is the Amazon Web Services Systems Manager managed instance ID.</p>"""
    capacity_provider_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The capacity provider that's associated with the container instance.</p>"""
    version: "capo_ecs.types.long.Long"
    """<p>The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If you're replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the <code>detail</code> object) to verify that the version in your event stream is current.</p>"""
    version_info: NotRequired["capo_ecs.types.version_info.VersionInfo"]
    """<p>The version information for the Amazon ECS container agent and Docker daemon running on the container instance.</p>"""
    remaining_resources: NotRequired["capo_ecs.types.resources.Resources"]
    """<p>For CPU and memory resource types, this parameter describes the remaining CPU and memory that wasn't already allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the <code>host</code> or <code>bridge</code> network mode). Any port that's not specified here is available for new tasks.</p>"""
    registered_resources: NotRequired["capo_ecs.types.resources.Resources"]
    """<p>For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.</p>"""
    status: NotRequired["capo_ecs.types.string.String"]
    """<p>The status of the container instance. The valid values are <code>REGISTERING</code>, <code>REGISTRATION_FAILED</code>, <code>ACTIVE</code>, <code>INACTIVE</code>, <code>DEREGISTERING</code>, or <code>DRAINING</code>.</p> <p>If your account has opted in to the <code>awsvpcTrunking</code> account setting, then any newly registered container instance will transition to a <code>REGISTERING</code> status while the trunk elastic network interface is provisioned for the instance. If the registration fails, the instance will transition to a <code>REGISTRATION_FAILED</code> status. You can describe the container instance and see the reason for failure in the <code>statusReason</code> parameter. Once the container instance is terminated, the instance transitions to a <code>DEREGISTERING</code> status while the trunk elastic network interface is deprovisioned. The instance then transitions to an <code>INACTIVE</code> status.</p> <p>The <code>ACTIVE</code> status indicates that the container instance can accept tasks. The <code>DRAINING</code> indicates that new tasks aren't placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html">Container instance draining</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    status_reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason that the container instance reached its current status.</p>"""
    agent_connected: "capo_ecs.types.boolean.Boolean"
    """<p>This parameter returns <code>true</code> if the agent is connected to Amazon ECS. An instance with an agent that may be unhealthy or stopped return <code>false</code>. Only instances connected to an agent can accept task placement requests.</p>"""
    running_tasks_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks on the container instance that have a desired status (<code>desiredStatus</code>) of <code>RUNNING</code>.</p>"""
    pending_tasks_count: "capo_ecs.types.integer.Integer"
    """<p>The number of tasks on the container instance that are in the <code>PENDING</code> status.</p>"""
    agent_update_status: NotRequired[
        "capo_ecs.types.agent_update_status.AgentUpdateStatus"
    ]
    """<p>The status of the most recent agent update. If an update wasn't ever requested, this value is <code>NULL</code>.</p>"""
    attributes: NotRequired["capo_ecs.types.attributes.Attributes"]
    """<p>The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html">PutAttributes</a> operation.</p>"""
    registered_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the container instance was registered.</p>"""
    attachments: NotRequired["capo_ecs.types.attachments.Attachments"]
    """<p>The resources attached to a container instance, such as an elastic network interface.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    health_status: NotRequired[
        "capo_ecs.types.container_instance_health_status.ContainerInstanceHealthStatus"
    ]
    """<p>An object representing the health status of the container instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstance) -> dict:
    out: dict = {}
    if "container_instance_arn" in value:
        out["containerInstanceArn"] = value["container_instance_arn"]
    if "ec2_instance_id" in value:
        out["ec2InstanceId"] = value["ec2_instance_id"]
    if "capacity_provider_name" in value:
        out["capacityProviderName"] = value["capacity_provider_name"]
    out["version"] = value.get("version", 0)
    if "version_info" in value:
        import capo_ecs.types.version_info

        out["versionInfo"] = capo_ecs.types.version_info.serialize_aws_json_1_1(
            value["version_info"]
        )
    if "remaining_resources" in value:
        import capo_ecs.types.resources

        out["remainingResources"] = capo_ecs.types.resources.serialize_aws_json_1_1(
            value["remaining_resources"]
        )
    if "registered_resources" in value:
        import capo_ecs.types.resources

        out["registeredResources"] = capo_ecs.types.resources.serialize_aws_json_1_1(
            value["registered_resources"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["agentConnected"] = value.get("agent_connected", False)
    out["runningTasksCount"] = value.get("running_tasks_count", 0)
    out["pendingTasksCount"] = value.get("pending_tasks_count", 0)
    if "agent_update_status" in value:
        import capo_ecs.types.agent_update_status

        out["agentUpdateStatus"] = (
            capo_ecs.types.agent_update_status.serialize_aws_json_1_1(
                value["agent_update_status"]
            )
        )
    if "attributes" in value:
        import capo_ecs.types.attributes

        out["attributes"] = capo_ecs.types.attributes.serialize_aws_json_1_1(
            value["attributes"]
        )
    if "registered_at" in value:
        import capo_ecs.types.timestamp

        out["registeredAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["registered_at"]
        )
    if "attachments" in value:
        import capo_ecs.types.attachments

        out["attachments"] = capo_ecs.types.attachments.serialize_aws_json_1_1(
            value["attachments"]
        )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "health_status" in value:
        import capo_ecs.types.container_instance_health_status

        out["healthStatus"] = (
            capo_ecs.types.container_instance_health_status.serialize_aws_json_1_1(
                value["health_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerInstance:
    out: ContainerInstance = {}  # type: ignore[typeddict-item]
    if data.get("containerInstanceArn") is not None:
        out["container_instance_arn"] = data["containerInstanceArn"]
    if data.get("ec2InstanceId") is not None:
        out["ec2_instance_id"] = data["ec2InstanceId"]
    if data.get("capacityProviderName") is not None:
        out["capacity_provider_name"] = data["capacityProviderName"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = 0
    if data.get("versionInfo") is not None:
        import capo_ecs.types.version_info

        out["version_info"] = capo_ecs.types.version_info.deserialize_aws_json_1_1(
            data["versionInfo"]
        )
    if data.get("remainingResources") is not None:
        import capo_ecs.types.resources

        out["remaining_resources"] = capo_ecs.types.resources.deserialize_aws_json_1_1(
            data["remainingResources"]
        )
    if data.get("registeredResources") is not None:
        import capo_ecs.types.resources

        out["registered_resources"] = capo_ecs.types.resources.deserialize_aws_json_1_1(
            data["registeredResources"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("agentConnected") is not None:
        out["agent_connected"] = data["agentConnected"]
    else:
        out["agent_connected"] = False
    if data.get("runningTasksCount") is not None:
        out["running_tasks_count"] = data["runningTasksCount"]
    else:
        out["running_tasks_count"] = 0
    if data.get("pendingTasksCount") is not None:
        out["pending_tasks_count"] = data["pendingTasksCount"]
    else:
        out["pending_tasks_count"] = 0
    if data.get("agentUpdateStatus") is not None:
        import capo_ecs.types.agent_update_status

        out["agent_update_status"] = (
            capo_ecs.types.agent_update_status.deserialize_aws_json_1_1(
                data["agentUpdateStatus"]
            )
        )
    if data.get("attributes") is not None:
        import capo_ecs.types.attributes

        out["attributes"] = capo_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    if data.get("registeredAt") is not None:
        import capo_ecs.types.timestamp

        out["registered_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["registeredAt"]
        )
    if data.get("attachments") is not None:
        import capo_ecs.types.attachments

        out["attachments"] = capo_ecs.types.attachments.deserialize_aws_json_1_1(
            data["attachments"]
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("healthStatus") is not None:
        import capo_ecs.types.container_instance_health_status

        out["health_status"] = (
            capo_ecs.types.container_instance_health_status.deserialize_aws_json_1_1(
                data["healthStatus"]
            )
        )
    return out
