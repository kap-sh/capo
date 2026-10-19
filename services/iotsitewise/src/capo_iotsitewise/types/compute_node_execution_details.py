"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeExecutionDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.compute_node_execution_status
    import capo_iotsitewise.types.compute_node_name_list
    import capo_iotsitewise.types.execution_environment_variables_map
    import capo_iotsitewise.types.mount_list
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class ComputeNodeExecutionDetails(TypedDict, closed=True):
    compute_node_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the compute node.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task executed for this compute node.</p>"""
    task_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the task.</p>"""
    task_version: "capo_iotsitewise.types.version.Version"
    """<p>The task version that executed for this compute node.</p>"""
    depends_on: "capo_iotsitewise.types.compute_node_name_list.ComputeNodeNameList"
    """<p>A list of compute node names that this node depends on.</p>"""
    status: "capo_iotsitewise.types.compute_node_execution_status.ComputeNodeExecutionStatus"
    """<p>The current execution status of the compute node.</p>"""
    start_time: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the compute node execution started, in Unix epoch time.</p>"""
    end_time: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the compute node execution completed, in Unix epoch time.</p>"""
    execution_environment_variables: NotRequired[
        "capo_iotsitewise.types.execution_environment_variables_map.ExecutionEnvironmentVariablesMap"
    ]
    """<p>The fully resolved environment variables used for this compute node execution.</p>"""
    execution_mounts: NotRequired["capo_iotsitewise.types.mount_list.MountList"]
    """<p>The fully resolved mounts used for this compute node execution, after merging task-defined mounts with any execution-level mount overrides. Each mount attaches an external data source to the container filesystem at a relative path under the service-owned mount root.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeExecutionDetails) -> dict:
    out: dict = {}
    out["computeNodeName"] = value["compute_node_name"]
    out["taskName"] = value["task_name"]
    out["taskArn"] = value["task_arn"]
    out["taskVersion"] = value["task_version"]
    import capo_iotsitewise.types.compute_node_name_list

    out["dependsOn"] = capo_iotsitewise.types.compute_node_name_list.serialize_json(
        value["depends_on"]
    )
    import capo_iotsitewise.types.compute_node_execution_status

    out["status"] = capo_iotsitewise.types.compute_node_execution_status.serialize_json(
        value["status"]
    )
    if "start_time" in value:
        import capo_iotsitewise.types.timestamp

        out["startTime"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_iotsitewise.types.timestamp

        out["endTime"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "execution_environment_variables" in value:
        import capo_iotsitewise.types.execution_environment_variables_map

        out["executionEnvironmentVariables"] = (
            capo_iotsitewise.types.execution_environment_variables_map.serialize_json(
                value["execution_environment_variables"]
            )
        )
    if "execution_mounts" in value:
        import capo_iotsitewise.types.mount_list

        out["executionMounts"] = capo_iotsitewise.types.mount_list.serialize_json(
            value["execution_mounts"]
        )
    return out


def deserialize_json(data: dict) -> ComputeNodeExecutionDetails:
    out: ComputeNodeExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("computeNodeName") is not None:
        out["compute_node_name"] = data["computeNodeName"]
    else:
        out["compute_node_name"] = ""
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    else:
        out["task_name"] = ""
    if data.get("taskArn") is not None:
        out["task_arn"] = data["taskArn"]
    else:
        out["task_arn"] = ""
    if data.get("taskVersion") is not None:
        out["task_version"] = data["taskVersion"]
    else:
        out["task_version"] = ""
    if data.get("dependsOn") is not None:
        import capo_iotsitewise.types.compute_node_name_list

        out["depends_on"] = (
            capo_iotsitewise.types.compute_node_name_list.deserialize_json(
                data["dependsOn"]
            )
        )
    else:
        out["depends_on"] = []
    if data.get("status") is not None:
        import capo_iotsitewise.types.compute_node_execution_status

        out["status"] = (
            capo_iotsitewise.types.compute_node_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeExecutionDetails.status required")
    if data.get("startTime") is not None:
        import capo_iotsitewise.types.timestamp

        out["start_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_iotsitewise.types.timestamp

        out["end_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("executionEnvironmentVariables") is not None:
        import capo_iotsitewise.types.execution_environment_variables_map

        out["execution_environment_variables"] = (
            capo_iotsitewise.types.execution_environment_variables_map.deserialize_json(
                data["executionEnvironmentVariables"]
            )
        )
    if data.get("executionMounts") is not None:
        import capo_iotsitewise.types.mount_list

        out["execution_mounts"] = capo_iotsitewise.types.mount_list.deserialize_json(
            data["executionMounts"]
        )
    return out


def redact_sensitive(value: ComputeNodeExecutionDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "execution_environment_variables" in value:
        out["execution_environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
