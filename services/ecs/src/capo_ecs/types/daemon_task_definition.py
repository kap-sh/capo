"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_container_definition_list
    import capo_ecs.types.daemon_ipc_mode
    import capo_ecs.types.daemon_pid_mode
    import capo_ecs.types.daemon_task_definition_status
    import capo_ecs.types.daemon_volume_list
    import capo_ecs.types.integer
    import capo_ecs.types.string
    import capo_ecs.types.timestamp


class DaemonTaskDefinition(TypedDict, closed=True):
    daemon_task_definition_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the daemon task definition.</p>"""
    family: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of a family that this daemon task definition is registered to.</p>"""
    revision: "capo_ecs.types.integer.Integer"
    """<p>The revision of the daemon task in a particular family. The revision is a version number of a daemon task definition in a family. When you register a daemon task definition for the first time, the revision is <code>1</code>. Each time that you register a new revision of a daemon task definition in the same family, the revision value always increases by one.</p>"""
    task_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the IAM role that grants containers in the daemon task permission to call Amazon Web Services APIs on your behalf.</p>"""
    execution_role_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf.</p>"""
    container_definitions: NotRequired[
        "capo_ecs.types.daemon_container_definition_list.DaemonContainerDefinitionList"
    ]
    """<p>A list of container definitions in JSON format that describe the containers that make up the daemon task.</p>"""
    volumes: NotRequired["capo_ecs.types.daemon_volume_list.DaemonVolumeList"]
    """<p>The list of data volume definitions for the daemon task.</p>"""
    cpu: NotRequired["capo_ecs.types.string.String"]
    """<p>The number of CPU units used by the daemon task.</p>"""
    memory: NotRequired["capo_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the daemon task.</p>"""
    status: NotRequired[
        "capo_ecs.types.daemon_task_definition_status.DaemonTaskDefinitionStatus"
    ]
    """<p>The status of the daemon task definition. The valid values are <code>ACTIVE</code>, <code>DELETE_IN_PROGRESS</code>, and <code>DELETED</code>.</p>"""
    registered_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition was registered.</p>"""
    delete_requested_at: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition delete was requested.</p>"""
    registered_by: NotRequired["capo_ecs.types.string.String"]
    """<p>The principal that registered the daemon task definition.</p>"""
    pid_mode: NotRequired["capo_ecs.types.daemon_pid_mode.DaemonPidMode"]
    """<p>The PID namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use <code>pidMode: "host"</code> or other daemons that use <code>pidMode: "shared"</code>.</p>"""
    ipc_mode: NotRequired["capo_ecs.types.daemon_ipc_mode.DaemonIpcMode"]
    """<p>The IPC namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use <code>ipcMode: "host"</code> or other daemons that use <code>ipcMode: "shared"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinition) -> dict:
    out: dict = {}
    if "daemon_task_definition_arn" in value:
        out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    if "family" in value:
        out["family"] = value["family"]
    out["revision"] = value.get("revision", 0)
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "container_definitions" in value:
        import capo_ecs.types.daemon_container_definition_list

        out["containerDefinitions"] = (
            capo_ecs.types.daemon_container_definition_list.serialize_aws_json_1_1(
                value["container_definitions"]
            )
        )
    if "volumes" in value:
        import capo_ecs.types.daemon_volume_list

        out["volumes"] = capo_ecs.types.daemon_volume_list.serialize_aws_json_1_1(
            value["volumes"]
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "status" in value:
        import capo_ecs.types.daemon_task_definition_status

        out["status"] = (
            capo_ecs.types.daemon_task_definition_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "registered_at" in value:
        import capo_ecs.types.timestamp

        out["registeredAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["registered_at"]
        )
    if "delete_requested_at" in value:
        import capo_ecs.types.timestamp

        out["deleteRequestedAt"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(
            value["delete_requested_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "pid_mode" in value:
        import capo_ecs.types.daemon_pid_mode

        out["pidMode"] = capo_ecs.types.daemon_pid_mode.serialize_aws_json_1_1(
            value["pid_mode"]
        )
    if "ipc_mode" in value:
        import capo_ecs.types.daemon_ipc_mode

        out["ipcMode"] = capo_ecs.types.daemon_ipc_mode.serialize_aws_json_1_1(
            value["ipc_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonTaskDefinition:
    out: DaemonTaskDefinition = {}  # type: ignore[typeddict-item]
    if data.get("daemonTaskDefinitionArn") is not None:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    if data.get("family") is not None:
        out["family"] = data["family"]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    if data.get("taskRoleArn") is not None:
        out["task_role_arn"] = data["taskRoleArn"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("containerDefinitions") is not None:
        import capo_ecs.types.daemon_container_definition_list

        out["container_definitions"] = (
            capo_ecs.types.daemon_container_definition_list.deserialize_aws_json_1_1(
                data["containerDefinitions"]
            )
        )
    if data.get("volumes") is not None:
        import capo_ecs.types.daemon_volume_list

        out["volumes"] = capo_ecs.types.daemon_volume_list.deserialize_aws_json_1_1(
            data["volumes"]
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("status") is not None:
        import capo_ecs.types.daemon_task_definition_status

        out["status"] = (
            capo_ecs.types.daemon_task_definition_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("registeredAt") is not None:
        import capo_ecs.types.timestamp

        out["registered_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["registeredAt"]
        )
    if data.get("deleteRequestedAt") is not None:
        import capo_ecs.types.timestamp

        out["delete_requested_at"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["deleteRequestedAt"]
        )
    if data.get("registeredBy") is not None:
        out["registered_by"] = data["registeredBy"]
    if data.get("pidMode") is not None:
        import capo_ecs.types.daemon_pid_mode

        out["pid_mode"] = capo_ecs.types.daemon_pid_mode.deserialize_aws_json_1_1(
            data["pidMode"]
        )
    if data.get("ipcMode") is not None:
        import capo_ecs.types.daemon_ipc_mode

        out["ipc_mode"] = capo_ecs.types.daemon_ipc_mode.deserialize_aws_json_1_1(
            data["ipcMode"]
        )
    return out
