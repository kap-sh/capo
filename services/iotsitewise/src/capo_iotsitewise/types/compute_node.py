"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNode``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_name_list
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.resource_name


class ComputeNode(TypedDict, closed=True):
    compute_node_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The unique name for this compute node within the pipeline.</p>"""
    task_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the task to execute for this compute node.</p>"""
    environment_variables: NotRequired[
        "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables specific to this compute node. These override pipeline-level environment variables with the same key.</p>"""
    depends_on: NotRequired[
        "capo_iotsitewise.types.compute_node_name_list.ComputeNodeNameList"
    ]
    """<p>A list of compute node names that must complete successfully before this node can start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNode) -> dict:
    out: dict = {}
    out["computeNodeName"] = value["compute_node_name"]
    out["taskName"] = value["task_name"]
    if "environment_variables" in value:
        import capo_iotsitewise.types.environment_variables_map

        out["environmentVariables"] = (
            capo_iotsitewise.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "depends_on" in value:
        import capo_iotsitewise.types.compute_node_name_list

        out["dependsOn"] = capo_iotsitewise.types.compute_node_name_list.serialize_json(
            value["depends_on"]
        )
    return out


def deserialize_json(data: dict) -> ComputeNode:
    out: ComputeNode = {}  # type: ignore[typeddict-item]
    if data.get("computeNodeName") is not None:
        out["compute_node_name"] = data["computeNodeName"]
    else:
        raise DeserializationError("ComputeNode.compute_node_name required")
    if data.get("taskName") is not None:
        out["task_name"] = data["taskName"]
    else:
        raise DeserializationError("ComputeNode.task_name required")
    if data.get("environmentVariables") is not None:
        import capo_iotsitewise.types.environment_variables_map

        out["environment_variables"] = (
            capo_iotsitewise.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("dependsOn") is not None:
        import capo_iotsitewise.types.compute_node_name_list

        out["depends_on"] = (
            capo_iotsitewise.types.compute_node_name_list.deserialize_json(
                data["dependsOn"]
            )
        )
    return out


def redact_sensitive(value: ComputeNode) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    return out
