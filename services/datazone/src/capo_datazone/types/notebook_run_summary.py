"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_run_id
    import capo_datazone.types.notebook_run_status
    import capo_datazone.types.project_id
    import capo_datazone.types.schedule_id
    import capo_datazone.types.trigger_source
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class NotebookRunSummary(TypedDict, closed=True):
    id: "capo_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook run.</p>"""
    notebook_id: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""
    schedule_id: NotRequired["capo_datazone.types.schedule_id.ScheduleId"]
    """<p>The identifier of the schedule associated with the notebook run.</p>"""
    status: "capo_datazone.types.notebook_run_status.NotebookRunStatus"
    """<p>The status of the notebook run.</p>"""
    trigger_source: NotRequired["capo_datazone.types.trigger_source.TriggerSource"]
    """<p>The source that triggered the notebook run.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the notebook run was created.</p>"""
    created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The identifier of the user who created the notebook run.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the notebook run was last updated.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The identifier of the user who last updated the notebook run.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook run started executing.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the notebook run completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotebookRunSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    out["notebookId"] = value["notebook_id"]
    if "schedule_id" in value:
        out["scheduleId"] = value["schedule_id"]
    import capo_datazone.types.notebook_run_status

    out["status"] = capo_datazone.types.notebook_run_status.serialize_json(
        value["status"]
    )
    if "trigger_source" in value:
        import capo_datazone.types.trigger_source

        out["triggerSource"] = capo_datazone.types.trigger_source.serialize_json(
            value["trigger_source"]
        )
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "started_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["startedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "completed_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["completedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["completed_at"]
        )
    return out


def deserialize_json(data: dict) -> NotebookRunSummary:
    out: NotebookRunSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        out["owning_project_id"] = ""
    if data.get("notebookId") is not None:
        out["notebook_id"] = data["notebookId"]
    else:
        out["notebook_id"] = ""
    if data.get("scheduleId") is not None:
        out["schedule_id"] = data["scheduleId"]
    if data.get("status") is not None:
        import capo_datazone.types.notebook_run_status

        out["status"] = capo_datazone.types.notebook_run_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.notebook_run_status.NotebookRunStatus", ""
        )
    if data.get("triggerSource") is not None:
        import capo_datazone.types.trigger_source

        out["trigger_source"] = capo_datazone.types.trigger_source.deserialize_json(
            data["triggerSource"]
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("updatedAt") is not None:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("startedAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["started_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if data.get("completedAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["completed_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["completedAt"]
        )
    return out
