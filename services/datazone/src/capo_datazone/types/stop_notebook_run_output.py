"""Generated from Smithy shape ``com.amazonaws.datazone#StopNotebookRunOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_run_id
    import capo_datazone.types.notebook_run_status
    import capo_datazone.types.project_id


class StopNotebookRunOutput(TypedDict, closed=True):
    id: "capo_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain.</p>"""
    owning_project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that owns the notebook run.</p>"""
    status: "capo_datazone.types.notebook_run_status.NotebookRunStatus"
    """<p>The status of the notebook run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopNotebookRunOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["domainId"] = value["domain_id"]
    out["owningProjectId"] = value["owning_project_id"]
    import capo_datazone.types.notebook_run_status

    out["status"] = capo_datazone.types.notebook_run_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> StopNotebookRunOutput:
    out: StopNotebookRunOutput = {}  # type: ignore[typeddict-item]
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
    return out
