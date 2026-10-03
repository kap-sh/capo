"""Generated from Smithy shape ``com.amazonaws.batch#EcsTaskProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.ephemeral_storage
    import capo_batch.types.list_task_container_properties
    import capo_batch.types.network_configuration
    import capo_batch.types.runtime_platform
    import capo_batch.types.string
    import capo_batch.types.volumes


class EcsTaskProperties(TypedDict, closed=True):
    containers: NotRequired[
        "capo_batch.types.list_task_container_properties.ListTaskContainerProperties"
    ]
    """<p>This object is a list of containers.</p>"""
    ephemeral_storage: NotRequired[
        "capo_batch.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate.</p>"""
    execution_role_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the execution role that Batch can assume. For jobs that run on Fargate resources, you must provide an execution role. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html">Batch execution IAM role</a> in the <i>Batch User Guide</i>.</p>"""
    platform_version: NotRequired["capo_batch.types.string.String"]
    """<p>The Fargate platform version where the jobs are running. A platform version is specified only for jobs that are running on Fargate resources. If one isn't specified, the <code>LATEST</code> platform version is used by default. This uses a recent, approved version of the Fargate platform for compute resources. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    ipc_mode: NotRequired["capo_batch.types.string.String"]
    """<p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified <code>task</code> share the same IPC resources.</p> <p>If <code>none</code> is specified, the IPC resources within the containers of a task are private, and are not shared with other containers in a task or on the container instance. </p> <p>If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see <a href="https://docs.docker.com/engine/reference/run/#ipc-settings---ipc">IPC settings</a> in the Docker run reference.</p> <note> <p>This parameter is not supported for jobs that run on Fargate resources.</p> </note>"""
    task_role_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that's associated with the Amazon ECS task.</p> <note> <p>This is object is comparable to <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html">ContainerProperties:jobRoleArn</a>.</p> </note>"""
    pid_mode: NotRequired["capo_batch.types.string.String"]
    """<p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the default is a private namespace for each container. For more information, see <a href="https://docs.docker.com/engine/reference/run/#pid-settings---pid">PID settings</a> in the Docker run reference.</p>"""
    network_configuration: NotRequired[
        "capo_batch.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources or Amazon ECS Managed Instances must not specify this parameter.</p>"""
    runtime_platform: NotRequired["capo_batch.types.runtime_platform.RuntimePlatform"]
    """<p>An object that represents the compute environment architecture for Batch jobs on Fargate or Amazon ECS Managed Instances. Use this to specify the operating system family (<code>operatingSystemFamily</code>) and CPU architecture (<code>cpuArchitecture</code>).</p> <p>For Amazon ECS Managed Instances, the valid value for <code>operatingSystemFamily</code> is <code>LINUX</code> (default). The valid values for <code>cpuArchitecture</code> are <code>X86_64</code> and <code>ARM64</code>.</p>"""
    volumes: NotRequired["capo_batch.types.volumes.Volumes"]
    """<p>A list of volumes that are associated with the job.</p>"""
    enable_execute_command: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Determines whether execute command functionality is turned on for this task. If <code>true</code>, execute command functionality is turned on all the containers in the task.</p>"""
    network_mode: NotRequired["capo_batch.types.string.String"]
    """<p>The network mode to use for the task. Valid values: <code>host</code>. When not specified, the default is <code>host</code>.</p> <p>With <code>host</code> mode, the container shares the host instance's network stack directly. When running tasks that use the <code>host</code> network mode, do not run containers using the root user (UID 0). Running as root grants unrestricted access to host resources and increases the attack surface.</p> <p>This parameter only applies to jobs running on Amazon ECS Managed Instances (<code>MANAGED_INSTANCES</code> platform capability). It cannot be specified for Fargate or Amazon EC2 platform job definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsTaskProperties) -> dict:
    out: dict = {}
    if "containers" in value:
        import capo_batch.types.list_task_container_properties

        out["containers"] = (
            capo_batch.types.list_task_container_properties.serialize_json(
                value["containers"]
            )
        )
    if "ephemeral_storage" in value:
        import capo_batch.types.ephemeral_storage

        out["ephemeralStorage"] = capo_batch.types.ephemeral_storage.serialize_json(
            value["ephemeral_storage"]
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "ipc_mode" in value:
        out["ipcMode"] = value["ipc_mode"]
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "pid_mode" in value:
        out["pidMode"] = value["pid_mode"]
    if "network_configuration" in value:
        import capo_batch.types.network_configuration

        out["networkConfiguration"] = (
            capo_batch.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "runtime_platform" in value:
        import capo_batch.types.runtime_platform

        out["runtimePlatform"] = capo_batch.types.runtime_platform.serialize_json(
            value["runtime_platform"]
        )
    if "volumes" in value:
        import capo_batch.types.volumes

        out["volumes"] = capo_batch.types.volumes.serialize_json(value["volumes"])
    if "enable_execute_command" in value:
        out["enableExecuteCommand"] = value["enable_execute_command"]
    if "network_mode" in value:
        out["networkMode"] = value["network_mode"]
    return out


def deserialize_json(data: dict) -> EcsTaskProperties:
    out: EcsTaskProperties = {}  # type: ignore[typeddict-item]
    if data.get("containers") is not None:
        import capo_batch.types.list_task_container_properties

        out["containers"] = (
            capo_batch.types.list_task_container_properties.deserialize_json(
                data["containers"]
            )
        )
    if data.get("ephemeralStorage") is not None:
        import capo_batch.types.ephemeral_storage

        out["ephemeral_storage"] = capo_batch.types.ephemeral_storage.deserialize_json(
            data["ephemeralStorage"]
        )
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("platformVersion") is not None:
        out["platform_version"] = data["platformVersion"]
    if data.get("ipcMode") is not None:
        out["ipc_mode"] = data["ipcMode"]
    if data.get("taskRoleArn") is not None:
        out["task_role_arn"] = data["taskRoleArn"]
    if data.get("pidMode") is not None:
        out["pid_mode"] = data["pidMode"]
    if data.get("networkConfiguration") is not None:
        import capo_batch.types.network_configuration

        out["network_configuration"] = (
            capo_batch.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if data.get("runtimePlatform") is not None:
        import capo_batch.types.runtime_platform

        out["runtime_platform"] = capo_batch.types.runtime_platform.deserialize_json(
            data["runtimePlatform"]
        )
    if data.get("volumes") is not None:
        import capo_batch.types.volumes

        out["volumes"] = capo_batch.types.volumes.deserialize_json(data["volumes"])
    if data.get("enableExecuteCommand") is not None:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    if data.get("networkMode") is not None:
        out["network_mode"] = data["networkMode"]
    return out
