"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.source_repository_branch_string
    import capo_codecatalyst.types.source_repository_name_string
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.uuid
    import capo_codecatalyst.types.workflow_definition_summary
    import capo_codecatalyst.types.workflow_run_mode
    import capo_codecatalyst.types.workflow_status


class WorkflowSummary(TypedDict, closed=True):
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of a workflow.</p>"""
    name: "str"
    """<p>The name of the workflow.</p>"""
    source_repository_name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository where the workflow definition file is stored.</p>"""
    source_branch_name: "capo_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    """<p>The name of the branch of the source repository where the workflow definition file is stored.</p>"""
    definition: (
        "capo_codecatalyst.types.workflow_definition_summary.WorkflowDefinitionSummary"
    )
    """<p>Information about the workflow definition file.</p>"""
    created_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was created, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""
    last_updated_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""
    run_mode: "capo_codecatalyst.types.workflow_run_mode.WorkflowRunMode"
    """<p>The run mode of the workflow.</p>"""
    status: "capo_codecatalyst.types.workflow_status.WorkflowStatus"
    """<p>The status of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["sourceRepositoryName"] = value["source_repository_name"]
    out["sourceBranchName"] = value["source_branch_name"]
    import capo_codecatalyst.types.workflow_definition_summary

    out["definition"] = (
        capo_codecatalyst.types.workflow_definition_summary.serialize_json(
            value["definition"]
        )
    )
    import capo_codecatalyst._protocol.serialize

    out["createdTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["created_time"]
    )
    import capo_codecatalyst._protocol.serialize

    out["lastUpdatedTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
        value["last_updated_time"]
    )
    out["runMode"] = value["run_mode"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> WorkflowSummary:
    out: WorkflowSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("sourceRepositoryName") is not None:
        out["source_repository_name"] = data["sourceRepositoryName"]
    else:
        out["source_repository_name"] = ""
    if data.get("sourceBranchName") is not None:
        out["source_branch_name"] = data["sourceBranchName"]
    else:
        out["source_branch_name"] = ""
    if data.get("definition") is not None:
        import capo_codecatalyst.types.workflow_definition_summary

        out["definition"] = (
            capo_codecatalyst.types.workflow_definition_summary.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("WorkflowSummary.definition required")
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromisoformat(
            data["createdTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedTime") is not None:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromisoformat(
            data["lastUpdatedTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("runMode") is not None:
        out["run_mode"] = data["runMode"]
    else:
        out["run_mode"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
