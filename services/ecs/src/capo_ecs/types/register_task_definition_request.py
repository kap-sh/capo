"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterTaskDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.compatibility_list
    import capo_ecs.types.container_definitions
    import capo_ecs.types.ephemeral_storage
    import capo_ecs.types.inference_accelerators
    import capo_ecs.types.ipc_mode
    import capo_ecs.types.network_mode
    import capo_ecs.types.pid_mode
    import capo_ecs.types.proxy_configuration
    import capo_ecs.types.runtime_platform
    import capo_ecs.types.string
    import capo_ecs.types.tags
    import capo_ecs.types.task_definition_placement_constraints
    import capo_ecs.types.volume_list


class RegisterTaskDefinitionRequest(TypedDict, closed=True):
    family: "capo_ecs.types.string.String"
    """<p>You must specify a <code>family</code> for a task definition. You can use it track multiple versions of the same task definition. The <code>family</code> is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html">IAM roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    network_mode: NotRequired["capo_ecs.types.network_mode.NetworkMode"]
    """<p>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>.</p> <p>For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>&lt;default&gt;</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode.</p> <p>With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. </p> <important> <p>When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.</p> </important> <p>If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> value when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.</p>"""
    container_definitions: "capo_ecs.types.container_definitions.ContainerDefinitions"
    """<p>A list of container definitions in JSON format that describe the different containers that make up your task.</p>"""
    volumes: NotRequired["capo_ecs.types.volume_list.VolumeList"]
    """<p>A list of volume definitions in JSON format that containers in your task might use.</p>"""
    placement_constraints: NotRequired[
        "capo_ecs.types.task_definition_placement_constraints.TaskDefinitionPlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>"""
    requires_compatibilities: NotRequired[
        "capo_ecs.types.compatibility_list.CompatibilityList"
    ]
    """<p>The task launch type that Amazon ECS validates the task definition against. A client exception is returned if the task definition doesn't validate against the compatibilities specified. If no value is specified, the parameter is omitted from the response.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of CPU units used by the task. It can be expressed as an integer using CPU units (for example, <code>1024</code>) or as a string using vCPUs (for example, <code>1 vCPU</code> or <code>1 vcpu</code>) in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If you're using the EC2 launch type or external launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>196608</code> CPU units (<code>192</code> vCPUs). If you do not specify a value, the parameter is ignored.</p> <p>This field is required for Fargate. For information about the valid values, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size">Task size</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB (for example ,<code>1024</code>) or as a string using GB (for example, <code>1GB</code> or <code>1 GB</code>) in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If using the EC2 launch type, this field is optional.</p> <p>If using the Fargate launch type, this field is required and you must use one of the following values. This determines your range of supported values for the <code>cpu</code> parameter.</p> <p>The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.</p> <ul> <li> <p>512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)</p> </li> <li> <p>1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)</p> </li> <li> <p>2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)</p> </li> <li> <p>Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)</p> </li> <li> <p>Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)</p> </li> <li> <p>Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> <li> <p>Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> </ul>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    pid_mode: NotRequired["capo_ecs.types.pid_mode.PidMode"]
    """<p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the The default is a private namespace for each container.</p> <p>If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note> <note> <p>This parameter is only supported for tasks that are hosted on Fargate if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</p> </note>"""
    ipc_mode: NotRequired["capo_ecs.types.ipc_mode.IpcMode"]
    """<p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.</p> <p>If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.</p> <p>If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">System Controls</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <ul> <li> <p>For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported.</p> </li> <li> <p>For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task.</p> </li> </ul> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>"""
    proxy_configuration: NotRequired[
        "capo_ecs.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>The configuration details for the App Mesh proxy.</p> <p>For tasks hosted on Amazon EC2 instances, the container instances require at least version <code>1.26.0</code> of the container agent and at least version <code>1.26.0-1</code> of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-versions.html">Amazon ECS-optimized AMI versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    inference_accelerators: NotRequired[
        "capo_ecs.types.inference_accelerators.InferenceAccelerators"
    ]
    """<p>The Elastic Inference accelerators to use for the containers in the task.</p>"""
    ephemeral_storage: NotRequired["capo_ecs.types.ephemeral_storage.EphemeralStorage"]
    """<p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html">Using data volumes in tasks</a> in the <i>Amazon ECS Developer Guide</i>.</p> <note> <p>For tasks using the Fargate launch type, the task requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>"""
    runtime_platform: NotRequired["capo_ecs.types.runtime_platform.RuntimePlatform"]
    """<p>The operating system that your tasks definitions run on.</p>"""
    enable_fault_injection: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Enables fault injection when you register your task definition and allows for fault injection requests to be accepted from the task's containers. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTaskDefinitionRequest) -> dict:
    out: dict = {}
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
    import capo_ecs.types.container_definitions

    out["containerDefinitions"] = (
        capo_ecs.types.container_definitions.serialize_aws_json_1_1(
            value["container_definitions"]
        )
    )
    if "volumes" in value:
        import capo_ecs.types.volume_list

        out["volumes"] = capo_ecs.types.volume_list.serialize_aws_json_1_1(
            value["volumes"]
        )
    if "placement_constraints" in value:
        import capo_ecs.types.task_definition_placement_constraints

        out["placementConstraints"] = (
            capo_ecs.types.task_definition_placement_constraints.serialize_aws_json_1_1(
                value["placement_constraints"]
            )
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
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
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
    if "inference_accelerators" in value:
        import capo_ecs.types.inference_accelerators

        out["inferenceAccelerators"] = (
            capo_ecs.types.inference_accelerators.serialize_aws_json_1_1(
                value["inference_accelerators"]
            )
        )
    if "ephemeral_storage" in value:
        import capo_ecs.types.ephemeral_storage

        out["ephemeralStorage"] = (
            capo_ecs.types.ephemeral_storage.serialize_aws_json_1_1(
                value["ephemeral_storage"]
            )
        )
    if "runtime_platform" in value:
        import capo_ecs.types.runtime_platform

        out["runtimePlatform"] = capo_ecs.types.runtime_platform.serialize_aws_json_1_1(
            value["runtime_platform"]
        )
    if "enable_fault_injection" in value:
        out["enableFaultInjection"] = value["enable_fault_injection"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTaskDefinitionRequest:
    out: RegisterTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("family") is not None:
        out["family"] = data["family"]
    else:
        raise DeserializationError("RegisterTaskDefinitionRequest.family required")
    if data.get("taskRoleArn") is not None:
        out["task_role_arn"] = data["taskRoleArn"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("networkMode") is not None:
        import capo_ecs.types.network_mode

        out["network_mode"] = capo_ecs.types.network_mode.deserialize_aws_json_1_1(
            data["networkMode"]
        )
    if data.get("containerDefinitions") is not None:
        import capo_ecs.types.container_definitions

        out["container_definitions"] = (
            capo_ecs.types.container_definitions.deserialize_aws_json_1_1(
                data["containerDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterTaskDefinitionRequest.container_definitions required"
        )
    if data.get("volumes") is not None:
        import capo_ecs.types.volume_list

        out["volumes"] = capo_ecs.types.volume_list.deserialize_aws_json_1_1(
            data["volumes"]
        )
    if data.get("placementConstraints") is not None:
        import capo_ecs.types.task_definition_placement_constraints

        out["placement_constraints"] = (
            capo_ecs.types.task_definition_placement_constraints.deserialize_aws_json_1_1(
                data["placementConstraints"]
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
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
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
    if data.get("inferenceAccelerators") is not None:
        import capo_ecs.types.inference_accelerators

        out["inference_accelerators"] = (
            capo_ecs.types.inference_accelerators.deserialize_aws_json_1_1(
                data["inferenceAccelerators"]
            )
        )
    if data.get("ephemeralStorage") is not None:
        import capo_ecs.types.ephemeral_storage

        out["ephemeral_storage"] = (
            capo_ecs.types.ephemeral_storage.deserialize_aws_json_1_1(
                data["ephemeralStorage"]
            )
        )
    if data.get("runtimePlatform") is not None:
        import capo_ecs.types.runtime_platform

        out["runtime_platform"] = (
            capo_ecs.types.runtime_platform.deserialize_aws_json_1_1(
                data["runtimePlatform"]
            )
        )
    if data.get("enableFaultInjection") is not None:
        out["enable_fault_injection"] = data["enableFaultInjection"]
    return out
