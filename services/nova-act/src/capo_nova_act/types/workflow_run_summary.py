"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.date_timestamp
    import capo_nova_act.types.trace_location
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_run_arn
    import capo_nova_act.types.workflow_run_status


class WorkflowRunSummary(TypedDict, closed=True):
    workflow_run_arn: "capo_nova_act.types.workflow_run_arn.WorkflowRunArn"
    """<p>The Amazon Resource Name (ARN) of the workflow run.</p>"""
    workflow_run_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run.</p>"""
    status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The current execution status of the workflow run.</p>"""
    started_at: "capo_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the workflow run started execution.</p>"""
    ended_at: NotRequired["capo_nova_act.types.date_timestamp.DateTimestamp"]
    """<p>The timestamp when the workflow run completed execution, if applicable.</p>"""
    trace_location: NotRequired["capo_nova_act.types.trace_location.TraceLocation"]
    """<p>The location where trace information for this workflow run is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunSummary) -> dict:
    out: dict = {}
    out["workflowRunArn"] = value["workflow_run_arn"]
    out["workflowRunId"] = value["workflow_run_id"]
    import capo_nova_act.types.workflow_run_status

    out["status"] = capo_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    import capo_nova_act.types.date_timestamp

    out["startedAt"] = capo_nova_act.types.date_timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_nova_act.types.date_timestamp

        out["endedAt"] = capo_nova_act.types.date_timestamp.serialize_json(
            value["ended_at"]
        )
    if "trace_location" in value:
        import capo_nova_act.types.trace_location

        out["traceLocation"] = capo_nova_act.types.trace_location.serialize_json(
            value["trace_location"]
        )
    return out


def deserialize_json(data: dict) -> WorkflowRunSummary:
    out: WorkflowRunSummary = {}  # type: ignore[typeddict-item]
    if data.get("workflowRunArn") is not None:
        out["workflow_run_arn"] = data["workflowRunArn"]
    else:
        out["workflow_run_arn"] = ""
    if data.get("workflowRunId") is not None:
        out["workflow_run_id"] = data["workflowRunId"]
    else:
        out["workflow_run_id"] = ""
    if data.get("status") is not None:
        import capo_nova_act.types.workflow_run_status

        out["status"] = capo_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_nova_act.types.workflow_run_status.WorkflowRunStatus", ""
        )
    if data.get("startedAt") is not None:
        import capo_nova_act.types.date_timestamp

        out["started_at"] = capo_nova_act.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endedAt") is not None:
        import capo_nova_act.types.date_timestamp

        out["ended_at"] = capo_nova_act.types.date_timestamp.deserialize_json(
            data["endedAt"]
        )
    if data.get("traceLocation") is not None:
        import capo_nova_act.types.trace_location

        out["trace_location"] = capo_nova_act.types.trace_location.deserialize_json(
            data["traceLocation"]
        )
    return out
