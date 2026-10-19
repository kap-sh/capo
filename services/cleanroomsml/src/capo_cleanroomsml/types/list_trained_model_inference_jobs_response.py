"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainedModelInferenceJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.trained_model_inference_job_list


class ListTrainedModelInferenceJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    trained_model_inference_jobs: "capo_cleanroomsml.types.trained_model_inference_job_list.TrainedModelInferenceJobList"
    """<p>Returns the requested trained model inference jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainedModelInferenceJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.trained_model_inference_job_list

    out["trainedModelInferenceJobs"] = (
        capo_cleanroomsml.types.trained_model_inference_job_list.serialize_json(
            value["trained_model_inference_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTrainedModelInferenceJobsResponse:
    out: ListTrainedModelInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("trainedModelInferenceJobs") is not None:
        import capo_cleanroomsml.types.trained_model_inference_job_list

        out["trained_model_inference_jobs"] = (
            capo_cleanroomsml.types.trained_model_inference_job_list.deserialize_json(
                data["trainedModelInferenceJobs"]
            )
        )
    else:
        out["trained_model_inference_jobs"] = []
    return out
