"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelInferenceJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_trained_model_inference_job_list
    import capo_cleanroomsml.types.next_token


class ListCollaborationTrainedModelInferenceJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_trained_model_inference_jobs: "capo_cleanroomsml.types.collaboration_trained_model_inference_job_list.CollaborationTrainedModelInferenceJobList"
    """<p>The trained model inference jobs that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelInferenceJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.collaboration_trained_model_inference_job_list

    out["collaborationTrainedModelInferenceJobs"] = (
        capo_cleanroomsml.types.collaboration_trained_model_inference_job_list.serialize_json(
            value["collaboration_trained_model_inference_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelInferenceJobsResponse:
    out: ListCollaborationTrainedModelInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationTrainedModelInferenceJobs") is not None:
        import capo_cleanroomsml.types.collaboration_trained_model_inference_job_list

        out["collaboration_trained_model_inference_jobs"] = (
            capo_cleanroomsml.types.collaboration_trained_model_inference_job_list.deserialize_json(
                data["collaborationTrainedModelInferenceJobs"]
            )
        )
    else:
        out["collaboration_trained_model_inference_jobs"] = []
    return out
