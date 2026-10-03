"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.source_repository_branch_string
    import capo_codecatalyst.types.source_repository_name_string
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.uuid
    import capo_codecatalyst.types.workflow_definition
    import capo_codecatalyst.types.workflow_run_mode
    import capo_codecatalyst.types.workflow_status


class GetWorkflowResponse(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The ID of the workflow.</p>"""
    name: "str"
    """<p>The name of the workflow.</p>"""
    source_repository_name: NotRequired[
        "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    ]
    """<p>The name of the source repository where the workflow YAML is stored.</p>"""
    source_branch_name: NotRequired[
        "capo_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    ]
    """<p>The name of the branch that contains the workflow YAML.</p>"""
    definition: "capo_codecatalyst.types.workflow_definition.WorkflowDefinition"
    """<p>Information about the workflow definition file for the workflow.</p>"""
    created_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was created, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""
    last_updated_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The date and time the workflow was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a> </p>"""
    run_mode: "capo_codecatalyst.types.workflow_run_mode.WorkflowRunMode"
    """<p>The behavior to use when multiple workflows occur at the same time. For more information, see <a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html">https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-configure-runs.html</a> in the Amazon CodeCatalyst User Guide.</p>"""
    status: "capo_codecatalyst.types.workflow_status.WorkflowStatus"
    """<p>The status of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "source_repository_name" in value:
        out["sourceRepositoryName"] = value["source_repository_name"]
    if "source_branch_name" in value:
        out["sourceBranchName"] = value["source_branch_name"]
    import capo_codecatalyst.types.workflow_definition

    out["definition"] = capo_codecatalyst.types.workflow_definition.serialize_json(
        value["definition"]
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


def deserialize_json(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceName") is not None:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("GetWorkflowResponse.space_name required")
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("GetWorkflowResponse.project_name required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetWorkflowResponse.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetWorkflowResponse.name required")
    if data.get("sourceRepositoryName") is not None:
        out["source_repository_name"] = data["sourceRepositoryName"]
    if data.get("sourceBranchName") is not None:
        out["source_branch_name"] = data["sourceBranchName"]
    if data.get("definition") is not None:
        import capo_codecatalyst.types.workflow_definition

        out["definition"] = (
            capo_codecatalyst.types.workflow_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("GetWorkflowResponse.definition required")
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromisoformat(
            data["createdTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetWorkflowResponse.created_time required")
    if data.get("lastUpdatedTime") is not None:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromisoformat(
            data["lastUpdatedTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetWorkflowResponse.last_updated_time required")
    if data.get("runMode") is not None:
        out["run_mode"] = data["runMode"]
    else:
        raise DeserializationError("GetWorkflowResponse.run_mode required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetWorkflowResponse.status required")
    return out
