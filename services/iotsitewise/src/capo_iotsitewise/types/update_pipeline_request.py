"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdatePipelineRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_list
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.workspace_name


class UpdatePipelineRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline to update.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A new description for the pipeline.</p>"""
    environment_variables: NotRequired[
        "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Updated environment variables shared across all compute nodes.</p>"""
    computations: NotRequired[
        "capo_iotsitewise.types.compute_node_list.ComputeNodeList"
    ]
    """<p>Updated list of compute nodes forming the pipeline DAG.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipelineRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "environment_variables" in value:
        import capo_iotsitewise.types.environment_variables_map

        out["environmentVariables"] = (
            capo_iotsitewise.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "computations" in value:
        import capo_iotsitewise.types.compute_node_list

        out["computations"] = capo_iotsitewise.types.compute_node_list.serialize_json(
            value["computations"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePipelineRequest:
    out: UpdatePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("environmentVariables") is not None:
        import capo_iotsitewise.types.environment_variables_map

        out["environment_variables"] = (
            capo_iotsitewise.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("computations") is not None:
        import capo_iotsitewise.types.compute_node_list

        out["computations"] = capo_iotsitewise.types.compute_node_list.deserialize_json(
            data["computations"]
        )
    return out


def redact_sensitive(value: UpdatePipelineRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    if "computations" in value:
        import capo_iotsitewise.types.compute_node_list

        out["computations"] = capo_iotsitewise.types.compute_node_list.redact_sensitive(
            value["computations"]
        )
    return out
