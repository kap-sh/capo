"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreatePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.compute_node_list
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.tag_map
    import capo_iotsitewise.types.workspace_name


class CreatePipelineRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline to create. Must be unique within the workspace.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description of the pipeline.</p>"""
    environment_variables: NotRequired[
        "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables shared across all compute nodes in the pipeline. Individual compute nodes can override these values with their own environment variables.</p>"""
    computations: "capo_iotsitewise.types.compute_node_list.ComputeNodeList"
    """<p>The list of compute nodes that form the pipeline DAG. Each compute node references a task and can declare dependencies on other nodes.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the pipeline. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your AWS IoT SiteWise resources</a> in the AWS IoT SiteWise User Guide.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineRequest) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "environment_variables" in value:
        import capo_iotsitewise.types.environment_variables_map

        out["environmentVariables"] = (
            capo_iotsitewise.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    import capo_iotsitewise.types.compute_node_list

    out["computations"] = capo_iotsitewise.types.compute_node_list.serialize_json(
        value["computations"]
    )
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePipelineRequest:
    out: CreatePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("CreatePipelineRequest.pipeline_name required")
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
    else:
        raise DeserializationError("CreatePipelineRequest.computations required")
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
