"""Generated from Smithy shape ``com.amazonaws.batch#EcsTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.ephemeral_storage
    import capo_batch.types.list_task_container_details
    import capo_batch.types.network_configuration
    import capo_batch.types.runtime_platform
    import capo_batch.types.string
    import capo_batch.types.volumes


class EcsTaskDetails(TypedDict, closed=True):
    containers: NotRequired[
        "capo_batch.types.list_task_container_details.ListTaskContainerDetails"
    ]
    """<p>A list of containers that are included in the <code>taskProperties</code> list.</p>"""
    container_instance_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container instance that hosts the task.</p>"""
    task_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The ARN of the Amazon ECS task.</p>"""
    ephemeral_storage: NotRequired[
        "capo_batch.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The amount of ephemeral storage allocated for the task.</p>"""
    execution_role_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the execution role that Batch can assume. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html">Batch execution IAM role</a> in the <i>Batch User Guide</i>.</p>"""
    platform_version: NotRequired["capo_batch.types.string.String"]
    """<p>The Fargate platform version where the jobs are running.</p>"""
    ipc_mode: NotRequired["capo_batch.types.string.String"]
    """<p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. For more information see <code>ipcMode</code> in <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_EcsTaskProperties.html">EcsTaskProperties</a>.</p>"""
    task_role_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the container can assume for Amazon Web Services permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM roles for tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>This is object is comparable to <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_ContainerProperties.html">ContainerProperties:jobRoleArn</a>.</p> </note>"""
    pid_mode: NotRequired["capo_batch.types.string.String"]
    """<p>The process namespace to use for the containers in the task. The valid values are <code>host</code>, or <code>task</code>. For more information see <code>pidMode</code> in <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_EcsTaskProperties.html">EcsTaskProperties</a>.</p>"""
    network_configuration: NotRequired[
        "capo_batch.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.</p>"""
    runtime_platform: NotRequired["capo_batch.types.runtime_platform.RuntimePlatform"]
    """<p>An object that represents the compute environment architecture for Batch jobs on Fargate or Amazon ECS Managed Instances. Contains the operating system family and CPU architecture of the task.</p>"""
    volumes: NotRequired["capo_batch.types.volumes.Volumes"]
    """<p>A list of data volumes used in a job.</p>"""
    enable_execute_command: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Determines whether execute command functionality is turned on for this task. If <code>true</code>, execute command functionality is turned on all the containers in the task.</p>"""
    network_mode: NotRequired["capo_batch.types.string.String"]
    """<p>The network mode configured for the task. This field is populated for jobs running on Amazon ECS Managed Instances (<code>MANAGED_INSTANCES</code> platform capability) and always returns <code>host</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsTaskDetails) -> dict:
    out: dict = {}
    if "containers" in value:
        import capo_batch.types.list_task_container_details

        out["containers"] = capo_batch.types.list_task_container_details.serialize_json(
            value["containers"]
        )
    if "container_instance_arn" in value:
        out["containerInstanceArn"] = value["container_instance_arn"]
    if "task_arn" in value:
        out["taskArn"] = value["task_arn"]
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


def deserialize_json(data: dict) -> EcsTaskDetails:
    out: EcsTaskDetails = {}  # type: ignore[typeddict-item]
    if data.get("containers") is not None:
        import capo_batch.types.list_task_container_details

        out["containers"] = (
            capo_batch.types.list_task_container_details.deserialize_json(
                data["containers"]
            )
        )
    if data.get("containerInstanceArn") is not None:
        out["container_instance_arn"] = data["containerInstanceArn"]
    if data.get("taskArn") is not None:
        out["task_arn"] = data["taskArn"]
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
