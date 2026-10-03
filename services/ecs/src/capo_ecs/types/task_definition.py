"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.compatibility_list
    import capo_ecs.types.container_definitions
    import capo_ecs.types.ephemeral_storage
    import capo_ecs.types.inference_accelerators
    import capo_ecs.types.integer
    import capo_ecs.types.ipc_mode
    import capo_ecs.types.network_mode
    import capo_ecs.types.pid_mode
    import capo_ecs.types.proxy_configuration
    import capo_ecs.types.requires_attributes
    import capo_ecs.types.runtime_platform
    import capo_ecs.types.string
    import capo_ecs.types.task_definition_placement_constraints
    import capo_ecs.types.task_definition_status
    import capo_ecs.types.timestamp
    import capo_ecs.types.volume_list


class TaskDefinition(TypedDict, closed=True):
    task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the task definition.</p>"""
    container_definitions: NotRequired[
        "capo_ecs.types.container_definitions.ContainerDefinitions"
    ]
    """<p>A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html">Amazon ECS Task Definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    family: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of a family that this task definition is registered to. Up to 255 characters are allowed. Letters (both uppercase and lowercase letters), numbers, hyphens (-), and underscores (_) are allowed.</p> <p>A family groups multiple versions of a task definition. Amazon ECS gives the first task definition that you registered to a family a revision number of 1. Amazon ECS gives sequential revision numbers to each task definition that you add.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the Identity and Access Management role that grants containers in the task permission to call Amazon Web Services APIs on your behalf. For informationabout the required IAM roles for Amazon ECS, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html">IAM roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html">IAM roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    network_mode: NotRequired["capo_ecs.types.network_mode.NetworkMode"]
    """<p>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>.</p> <p>For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>&lt;default&gt;</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode.</p> <p>With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. </p> <important> <p>When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.</p> </important> <p>If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> value when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.</p>"""
    revision: "capo_ecs.types.integer.Integer"
    """<p>The revision of the task in a particular family. The revision is a version number of a task definition in a family. When you register a task definition for the first time, the revision is <code>1</code>. Each time that you register a new revision of a task definition in the same family, the revision value always increases by one. This is even if you deregistered previous revisions in this family.</p>"""
    volumes: NotRequired["capo_ecs.types.volume_list.VolumeList"]
    """<p>The list of data volume definitions for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html">Using data volumes in tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>The <code>host</code> and <code>sourcePath</code> parameters aren't supported for tasks run on Fargate. </p> </note>"""
    status: NotRequired["capo_ecs.types.task_definition_status.TaskDefinitionStatus"]
    """<p>The status of the task definition.</p>"""
    requires_attributes: NotRequired[
        "capo_ecs.types.requires_attributes.RequiresAttributes"
    ]
    """<p>The container instance attributes required by your task. When an Amazon EC2 instance is registered to your cluster, the Amazon ECS container agent assigns some standard attributes to the instance. You can apply custom attributes. These are specified as key-value pairs using the Amazon ECS console or the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html">PutAttributes</a> API. These attributes are used when determining task placement for tasks hosted on Amazon EC2 instances. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes">Attributes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>This parameter isn't supported for tasks run on Fargate.</p> </note>"""
    placement_constraints: NotRequired[
        "capo_ecs.types.task_definition_placement_constraints.TaskDefinitionPlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for tasks.</p> <note> <p>This parameter isn't supported for tasks run on Fargate.</p> </note>"""
    compatibilities: NotRequired["capo_ecs.types.compatibility_list.CompatibilityList"]
    """<p>Amazon ECS validates the task definition parameters with those supported by the launch type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    runtime_platform: NotRequired["capo_ecs.types.runtime_platform.RuntimePlatform"]
    """<p>The operating system that your task definitions are running on. A platform family is specified only for tasks using the Fargate launch type. </p> <p>When you specify a task in a service, this value must match the <code>runtimePlatform</code> value of the service.</p>"""
    requires_compatibilities: NotRequired[
        "capo_ecs.types.compatibility_list.CompatibilityList"
    ]
    """<p>The task launch types the task definition was validated against. The valid values are <code>MANAGED_INSTANCES</code>, <code>EC2</code>, <code>FARGATE</code>, and <code>EXTERNAL</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of <code>cpu</code> units used by the task. If you use the EC2 launch type, this field is optional. Any value can be used. If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines your range of valid values for the <code>memory</code> parameter.</p> <p>If you're using the EC2 launch type or the external launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>196608</code> CPU units (<code>192</code> vCPUs). </p> <p>This field is required for Fargate. For information about the valid values, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size">Task size</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The amount (in MiB) of memory used by the task.</p> <p>If your tasks runs on Amazon EC2 instances, you must specify either a task-level memory value or a container-level memory value. This field is optional and any value can be used. If a task-level memory value is specified, the container-level memory value is optional. For more information regarding container-level memory and memory reservation, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html">ContainerDefinition</a>.</p> <p>If your tasks runs on Fargate, this field is required. You must use one of the following values. The value you choose determines your range of valid values for the <code>cpu</code> parameter.</p> <ul> <li> <p>512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)</p> </li> <li> <p>1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)</p> </li> <li> <p>2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)</p> </li> <li> <p>Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)</p> </li> <li> <p>Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)</p> </li> <li> <p>Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> <li> <p>Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> </ul>"""
    inference_accelerators: NotRequired[
        "capo_ecs.types.inference_accelerators.InferenceAccelerators"
    ]
    """<p>The Elastic Inference accelerator that's associated with the task.</p>"""
    pid_mode: NotRequired["capo_ecs.types.pid_mode.PidMode"]
    """<p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the The default is a private namespace for each container.</p> <p>If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note> <note> <p>This parameter is only supported for tasks that are hosted on Fargate if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</p> </note>"""
    ipc_mode: NotRequired["capo_ecs.types.ipc_mode.IpcMode"]
    """<p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.</p> <p>If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.</p> <p>If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">System Controls</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <ul> <li> <p>For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported.</p> </li> <li> <p>For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task.</p> </li> </ul> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>"""
    proxy_configuration: NotRequired[
        "capo_ecs.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>The configuration details for the App Mesh proxy.</p> <p>Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version <code>20190301</code> or later, they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon ECS-optimized Linux AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    registered_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task definition was registered.</p>"""
    deregistered_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task definition was deregistered.</p>"""
    delete_requested_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task definition delete was requested.</p>"""
    registered_by: NotRequired["capo_ecs.types.string.String"]
    """<p>The principal that registered the task definition.</p>"""
    ephemeral_storage: NotRequired["capo_ecs.types.ephemeral_storage.EphemeralStorage"]
    """<p>The ephemeral storage settings to use for tasks run with the task definition.</p>"""
    enable_fault_injection: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Enables fault injection and allows for fault injection requests to be accepted from the task's containers. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinition) -> dict:
    out: dict = {}
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    if "container_definitions" in value:
        import capo_ecs.types.container_definitions

        out["containerDefinitions"] = (
            capo_ecs.types.container_definitions.serialize_aws_json_1_1(
                value["container_definitions"]
            )
        )
    if "family" in value:
        out["family"] = value["family"]
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "network_mode" in value:
        import capo_ecs.types.network_mode

        out["networkMode"] = capo_ecs.types.network_mode.serialize_aws_json_1_1(
            value["network_mode"]
        )
    out["revision"] = value.get("revision", 0)
    if "volumes" in value:
        import capo_ecs.types.volume_list

        out["volumes"] = capo_ecs.types.volume_list.serialize_aws_json_1_1(
            value["volumes"]
        )
    if "status" in value:
        import capo_ecs.types.task_definition_status

        out["status"] = capo_ecs.types.task_definition_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "requires_attributes" in value:
        import capo_ecs.types.requires_attributes

        out["requiresAttributes"] = (
            capo_ecs.types.requires_attributes.serialize_aws_json_1_1(
                value["requires_attributes"]
            )
        )
    if "placement_constraints" in value:
        import capo_ecs.types.task_definition_placement_constraints

        out["placementConstraints"] = (
            capo_ecs.types.task_definition_placement_constraints.serialize_aws_json_1_1(
                value["placement_constraints"]
            )
        )
    if "compatibilities" in value:
        import capo_ecs.types.compatibility_list

        out["compatibilities"] = (
            capo_ecs.types.compatibility_list.serialize_aws_json_1_1(
                value["compatibilities"]
            )
        )
    if "runtime_platform" in value:
        import capo_ecs.types.runtime_platform

        out["runtimePlatform"] = capo_ecs.types.runtime_platform.serialize_aws_json_1_1(
            value["runtime_platform"]
        )
    if "requires_compatibilities" in value:
        import capo_ecs.types.compatibility_list

        out["requiresCompatibilities"] = (
            capo_ecs.types.compatibility_list.serialize_aws_json_1_1(
                value["requires_compatibilities"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "inference_accelerators" in value:
        import capo_ecs.types.inference_accelerators

        out["inferenceAccelerators"] = (
            capo_ecs.types.inference_accelerators.serialize_aws_json_1_1(
                value["inference_accelerators"]
            )
        )
    if "pid_mode" in value:
        import capo_ecs.types.pid_mode

        out["pidMode"] = capo_ecs.types.pid_mode.serialize_aws_json_1_1(
            value["pid_mode"]
        )
    if "ipc_mode" in value:
        import capo_ecs.types.ipc_mode

        out["ipcMode"] = capo_ecs.types.ipc_mode.serialize_aws_json_1_1(
            value["ipc_mode"]
        )
    if "proxy_configuration" in value:
        import capo_ecs.types.proxy_configuration

        out["proxyConfiguration"] = (
            capo_ecs.types.proxy_configuration.serialize_aws_json_1_1(
                value["proxy_configuration"]
            )
        )
    if "registered_at" in value:
        import capo_ecs.types.timestamp

        out["registeredAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["registered_at"]
        )
    if "deregistered_at" in value:
        import capo_ecs.types.timestamp

        out["deregisteredAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["deregistered_at"]
        )
    if "delete_requested_at" in value:
        import capo_ecs.types.timestamp

        out["deleteRequestedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["delete_requested_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "ephemeral_storage" in value:
        import capo_ecs.types.ephemeral_storage

        out["ephemeralStorage"] = (
            capo_ecs.types.ephemeral_storage.serialize_aws_json_1_1(
                value["ephemeral_storage"]
            )
        )
    if "enable_fault_injection" in value:
        out["enableFaultInjection"] = value["enable_fault_injection"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskDefinition:
    out: TaskDefinition = {}  # type: ignore[typeddict-item]
    if data.get("taskDefinitionArn") is not None:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    if data.get("containerDefinitions") is not None:
        import capo_ecs.types.container_definitions

        out["container_definitions"] = (
            capo_ecs.types.container_definitions.deserialize_aws_json_1_1(
                data["containerDefinitions"]
            )
        )
    if data.get("family") is not None:
        out["family"] = data["family"]
    if data.get("taskRoleArn") is not None:
        out["task_role_arn"] = data["taskRoleArn"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("networkMode") is not None:
        import capo_ecs.types.network_mode

        out["network_mode"] = capo_ecs.types.network_mode.deserialize_aws_json_1_1(
            data["networkMode"]
        )
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    if data.get("volumes") is not None:
        import capo_ecs.types.volume_list

        out["volumes"] = capo_ecs.types.volume_list.deserialize_aws_json_1_1(
            data["volumes"]
        )
    if data.get("status") is not None:
        import capo_ecs.types.task_definition_status

        out["status"] = capo_ecs.types.task_definition_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("requiresAttributes") is not None:
        import capo_ecs.types.requires_attributes

        out["requires_attributes"] = (
            capo_ecs.types.requires_attributes.deserialize_aws_json_1_1(
                data["requiresAttributes"]
            )
        )
    if data.get("placementConstraints") is not None:
        import capo_ecs.types.task_definition_placement_constraints

        out["placement_constraints"] = (
            capo_ecs.types.task_definition_placement_constraints.deserialize_aws_json_1_1(
                data["placementConstraints"]
            )
        )
    if data.get("compatibilities") is not None:
        import capo_ecs.types.compatibility_list

        out["compatibilities"] = (
            capo_ecs.types.compatibility_list.deserialize_aws_json_1_1(
                data["compatibilities"]
            )
        )
    if data.get("runtimePlatform") is not None:
        import capo_ecs.types.runtime_platform

        out["runtime_platform"] = (
            capo_ecs.types.runtime_platform.deserialize_aws_json_1_1(
                data["runtimePlatform"]
            )
        )
    if data.get("requiresCompatibilities") is not None:
        import capo_ecs.types.compatibility_list

        out["requires_compatibilities"] = (
            capo_ecs.types.compatibility_list.deserialize_aws_json_1_1(
                data["requiresCompatibilities"]
            )
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("inferenceAccelerators") is not None:
        import capo_ecs.types.inference_accelerators

        out["inference_accelerators"] = (
            capo_ecs.types.inference_accelerators.deserialize_aws_json_1_1(
                data["inferenceAccelerators"]
            )
        )
    if data.get("pidMode") is not None:
        import capo_ecs.types.pid_mode

        out["pid_mode"] = capo_ecs.types.pid_mode.deserialize_aws_json_1_1(
            data["pidMode"]
        )
    if data.get("ipcMode") is not None:
        import capo_ecs.types.ipc_mode

        out["ipc_mode"] = capo_ecs.types.ipc_mode.deserialize_aws_json_1_1(
            data["ipcMode"]
        )
    if data.get("proxyConfiguration") is not None:
        import capo_ecs.types.proxy_configuration

        out["proxy_configuration"] = (
            capo_ecs.types.proxy_configuration.deserialize_aws_json_1_1(
                data["proxyConfiguration"]
            )
        )
    if data.get("registeredAt") is not None:
        import capo_ecs.types.timestamp

        out["registered_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["registeredAt"]
        )
    if data.get("deregisteredAt") is not None:
        import capo_ecs.types.timestamp

        out["deregistered_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["deregisteredAt"]
        )
    if data.get("deleteRequestedAt") is not None:
        import capo_ecs.types.timestamp

        out["delete_requested_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["deleteRequestedAt"]
        )
    if data.get("registeredBy") is not None:
        out["registered_by"] = data["registeredBy"]
    if data.get("ephemeralStorage") is not None:
        import capo_ecs.types.ephemeral_storage

        out["ephemeral_storage"] = (
            capo_ecs.types.ephemeral_storage.deserialize_aws_json_1_1(
                data["ephemeralStorage"]
            )
        )
    if data.get("enableFaultInjection") is not None:
        out["enable_fault_injection"] = data["enableFaultInjection"]
    return out
