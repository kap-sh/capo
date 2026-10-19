"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDatasetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_export_job_id
    import capo_iotsitewise.types.workspace_name


class CreateDatasetExportJobResponse(TypedDict, closed=True):
    job_id: "capo_iotsitewise.types.dataset_export_job_id.DatasetExportJobId"
    """<p>The unique identifier for the dataset export job.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace in which the dataset export job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetExportJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["workspaceName"] = value["workspace_name"]
    return out


def deserialize_json(data: dict) -> CreateDatasetExportJobResponse:
    out: CreateDatasetExportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    return out
