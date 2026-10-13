"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribePipelineExecutionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.compute_node_execution_details_list
    import capo_iotsitewise.types.execution_environment_variables
    import capo_iotsitewise.types.execution_priority
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.mount_overrides
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.pipeline_execution_status
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribePipelineExecutionResponse(TypedDict, closed=True):
    pipeline_execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the pipeline execution.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_version: "capo_iotsitewise.types.version.Version"
    """<p>The pipeline version this execution ran against.</p>"""
    status: "capo_iotsitewise.types.pipeline_execution_status.PipelineExecutionStatus"
    """<p>The current execution status of the pipeline.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The time the pipeline execution started, in Unix epoch time.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time the pipeline execution completed, in Unix epoch time.</p>"""
    request_environment_variables: "capo_iotsitewise.types.execution_environment_variables.ExecutionEnvironmentVariables"
    """<p>The environment variables provided as input for the pipeline execution.</p>"""
    request_mount_overrides: NotRequired[
        "capo_iotsitewise.types.mount_overrides.MountOverrides"
    ]
    """<p>The mount overrides provided as input for the pipeline execution. Present when mount overrides were supplied at execution time.</p>"""
    execution_priority: NotRequired[
        "capo_iotsitewise.types.execution_priority.ExecutionPriority"
    ]
    """<p>Scheduling priority for the execution. When not specified, defaults to lowest priority.</p>"""
    compute_node_execution_details: "capo_iotsitewise.types.compute_node_execution_details_list.ComputeNodeExecutionDetailsList"
    """<p>A list of compute node execution details within this pipeline execution.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipelineExecutionResponse) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    out["pipelineName"] = value["pipeline_name"]
    out["workspaceName"] = value["workspace_name"]
    out["pipelineVersion"] = value["pipeline_version"]
    import capo_iotsitewise.types.pipeline_execution_status

    out["status"] = capo_iotsitewise.types.pipeline_execution_status.serialize_json(
        value["status"]
    )
    if "start_time" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["startTime"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_iotsitewise.types._prelude.timestamp

        out["endTime"] = capo_iotsitewise.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    import capo_iotsitewise.types.execution_environment_variables

    out["requestEnvironmentVariables"] = (
        capo_iotsitewise.types.execution_environment_variables.serialize_json(
            value["request_environment_variables"]
        )
    )
    if "request_mount_overrides" in value:
        import capo_iotsitewise.types.mount_overrides

        out["requestMountOverrides"] = (
            capo_iotsitewise.types.mount_overrides.serialize_json(
                value["request_mount_overrides"]
            )
        )
    if "execution_priority" in value:
        out["executionPriority"] = value["execution_priority"]
    import capo_iotsitewise.types.compute_node_execution_details_list

    out["computeNodeExecutionDetails"] = (
        capo_iotsitewise.types.compute_node_execution_details_list.serialize_json(
            value["compute_node_execution_details"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribePipelineExecutionResponse:
    out: DescribePipelineExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError(
            "DescribePipelineExecutionResponse.pipeline_execution_id required"
        )
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError(
            "DescribePipelineExecutionResponse.pipeline_name required"
        )
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        raise DeserializationError(
            "DescribePipelineExecutionResponse.workspace_name required"
        )
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    else:
        raise DeserializationError(
            "DescribePipelineExecutionResponse.pipeline_version required"
        )
    if data.get("status") is not None:
        import capo_iotsitewise.types.pipeline_execution_status

        out["status"] = (
            capo_iotsitewise.types.pipeline_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DescribePipelineExecutionResponse.status required")
    if data.get("startTime") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["start_time"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_iotsitewise.types._prelude.timestamp

        out["end_time"] = capo_iotsitewise.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("requestEnvironmentVariables") is not None:
        import capo_iotsitewise.types.execution_environment_variables

        out["request_environment_variables"] = (
            capo_iotsitewise.types.execution_environment_variables.deserialize_json(
                data["requestEnvironmentVariables"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePipelineExecutionResponse.request_environment_variables required"
        )
    if data.get("requestMountOverrides") is not None:
        import capo_iotsitewise.types.mount_overrides

        out["request_mount_overrides"] = (
            capo_iotsitewise.types.mount_overrides.deserialize_json(
                data["requestMountOverrides"]
            )
        )
    if data.get("executionPriority") is not None:
        out["execution_priority"] = data["executionPriority"]
    if data.get("computeNodeExecutionDetails") is not None:
        import capo_iotsitewise.types.compute_node_execution_details_list

        out["compute_node_execution_details"] = (
            capo_iotsitewise.types.compute_node_execution_details_list.deserialize_json(
                data["computeNodeExecutionDetails"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePipelineExecutionResponse.compute_node_execution_details required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: DescribePipelineExecutionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "request_environment_variables" in value:
        out["request_environment_variables"] = "*** Sensitive Data Redacted ***"
    if "compute_node_execution_details" in value:
        import capo_iotsitewise.types.compute_node_execution_details_list

        out["compute_node_execution_details"] = (
            capo_iotsitewise.types.compute_node_execution_details_list.redact_sensitive(
                value["compute_node_execution_details"]
            )
        )
    return out
