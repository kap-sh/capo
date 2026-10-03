"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.uuid
    import capo_codecatalyst.types.workflow_run_status
    import capo_codecatalyst.types.workflow_run_status_reasons


class WorkflowRunSummary(TypedDict, closed=True):
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the workflow run.</p>"""
    workflow_id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the workflow.</p>"""
    workflow_name: "str"
    """<p>The name of the workflow.</p>"""
    status: "capo_codecatalyst.types.workflow_run_status.WorkflowRunStatus"
    """<p>The status of the workflow run.</p>"""
    status_reasons: NotRequired[
        "capo_codecatalyst.types.workflow_run_status_reasons.WorkflowRunStatusReasons"
    ]
    """<p>The reasons for the workflow run status.</p>"""
    start_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow run began, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    end_time: NotRequired["capo_codecatalyst.types.timestamp.Timestamp"]
    """<p>The date and time the workflow run ended, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""
    last_updated_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["workflowId"] = value["workflow_id"]
    out["workflowName"] = value["workflow_name"]
    out["status"] = value["status"]
    if "status_reasons" in value:
        import capo_codecatalyst.types.workflow_run_status_reasons

        out["statusReasons"] = (
            capo_codecatalyst.types.workflow_run_status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    import capo_codecatalyst._protocol.serialize

    out["startTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_codecatalyst._protocol.serialize

        out["endTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    import capo_codecatalyst._protocol.serialize

    out["lastUpdatedTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["last_updated_time"]
    )
    return out


def deserialize_json(data: dict) -> WorkflowRunSummary:
    out: WorkflowRunSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("WorkflowRunSummary.id required")
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("WorkflowRunSummary.workflow_id required")
    if data.get("workflowName") is not None:
        out["workflow_name"] = data["workflowName"]
    else:
        raise DeserializationError("WorkflowRunSummary.workflow_name required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("WorkflowRunSummary.status required")
    if data.get("statusReasons") is not None:
        import capo_codecatalyst.types.workflow_run_status_reasons

        out["status_reasons"] = (
            capo_codecatalyst.types.workflow_run_status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("WorkflowRunSummary.start_time required")
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    if data.get("lastUpdatedTime") is not None:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromisoformat(
            data["lastUpdatedTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("WorkflowRunSummary.last_updated_time required")
    return out
