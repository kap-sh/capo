"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribePipelineResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.compute_node_list
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.resource_status
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribePipelineResponse(TypedDict, closed=True):
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>A unique name of the pipeline within the workspace.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The description of the pipeline.</p>"""
    pipeline_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The ARN of the pipeline.</p>"""
    version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the pipeline.</p>"""
    environment_variables: NotRequired[
        "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>The environment variables shared across all compute nodes in the pipeline.</p>"""
    computations: "capo_iotsitewise.types.compute_node_list.ComputeNodeList"
    """<p>The list of compute nodes that form the pipeline DAG.</p>"""
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the pipeline.</p>"""
    created_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the pipeline was created, in Unix epoch time.</p>"""
    updated_at: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the pipeline was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipelineResponse) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["workspaceName"] = value["workspace_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["pipelineArn"] = value["pipeline_arn"]
    out["version"] = value["version"]
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
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    import capo_iotsitewise.types.timestamp

    out["createdAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_iotsitewise.types.timestamp

    out["updatedAt"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DescribePipelineResponse:
    out: DescribePipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("DescribePipelineResponse.pipeline_name required")
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        raise DeserializationError("DescribePipelineResponse.workspace_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("pipelineArn") is not None:
        out["pipeline_arn"] = data["pipelineArn"]
    else:
        raise DeserializationError("DescribePipelineResponse.pipeline_arn required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("DescribePipelineResponse.version required")
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
        raise DeserializationError("DescribePipelineResponse.computations required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.resource_status

        out["status"] = capo_iotsitewise.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DescribePipelineResponse.status required")
    if data.get("createdAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["created_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DescribePipelineResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_iotsitewise.types.timestamp

        out["updated_at"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DescribePipelineResponse.updated_at required")
    return out


def redact_sensitive(value: DescribePipelineResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_variables" in value:
        out["environment_variables"] = "*** Sensitive Data Redacted ***"
    if "computations" in value:
        import capo_iotsitewise.types.compute_node_list

        out["computations"] = capo_iotsitewise.types.compute_node_list.redact_sensitive(
            value["computations"]
        )
    return out
