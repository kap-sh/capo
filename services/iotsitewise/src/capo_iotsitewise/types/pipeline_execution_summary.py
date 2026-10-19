"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.execution_priority
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.pipeline_execution_status
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version


class PipelineExecutionSummary(TypedDict, closed=True):
    pipeline_execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the pipeline execution.</p>"""
    pipeline_version: "capo_iotsitewise.types.version.Version"
    """<p>The pipeline version this execution ran against.</p>"""
    status: "capo_iotsitewise.types.pipeline_execution_status.PipelineExecutionStatus"
    """<p>The current execution status of the pipeline.</p>"""
    execution_priority: NotRequired[
        "capo_iotsitewise.types.execution_priority.ExecutionPriority"
    ]
    """<p>Scheduling priority for the execution. When not specified, defaults to lowest priority.</p>"""
    start_time: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the pipeline execution started, in Unix epoch time.</p>"""
    end_time: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the pipeline execution completed, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineExecutionSummary) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    out["pipelineVersion"] = value["pipeline_version"]
    import capo_iotsitewise.types.pipeline_execution_status

    out["status"] = capo_iotsitewise.types.pipeline_execution_status.serialize_json(
        value["status"]
    )
    if "execution_priority" in value:
        out["executionPriority"] = value["execution_priority"]
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
    return out


def deserialize_json(data: dict) -> PipelineExecutionSummary:
    out: PipelineExecutionSummary = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        out["pipeline_execution_id"] = ""
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    else:
        out["pipeline_version"] = ""
    if data.get("status") is not None:
        import capo_iotsitewise.types.pipeline_execution_status

        out["status"] = (
            capo_iotsitewise.types.pipeline_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PipelineExecutionSummary.status required")
    if data.get("executionPriority") is not None:
        out["execution_priority"] = data["executionPriority"]
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
    return out
