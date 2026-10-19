"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_trained_model_export_job_list
    import capo_cleanroomsml.types.next_token


class ListCollaborationTrainedModelExportJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_trained_model_export_jobs: "capo_cleanroomsml.types.collaboration_trained_model_export_job_list.CollaborationTrainedModelExportJobList"
    """<p>The exports jobs that exist for the requested trained model in the requested collaboration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelExportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.collaboration_trained_model_export_job_list

    out["collaborationTrainedModelExportJobs"] = (
        capo_cleanroomsml.types.collaboration_trained_model_export_job_list.serialize_json(
            value["collaboration_trained_model_export_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelExportJobsResponse:
    out: ListCollaborationTrainedModelExportJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationTrainedModelExportJobs") is not None:
        import capo_cleanroomsml.types.collaboration_trained_model_export_job_list

        out["collaboration_trained_model_export_jobs"] = (
            capo_cleanroomsml.types.collaboration_trained_model_export_job_list.deserialize_json(
                data["collaborationTrainedModelExportJobs"]
            )
        )
    else:
        out["collaboration_trained_model_export_jobs"] = []
    return out
