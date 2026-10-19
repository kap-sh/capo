"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartTrainedModelInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_inference_job_arn


class StartTrainedModelInferenceJobResponse(TypedDict, closed=True):
    trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTrainedModelInferenceJobResponse) -> dict:
    out: dict = {}
    out["trainedModelInferenceJobArn"] = value["trained_model_inference_job_arn"]
    return out


def deserialize_json(data: dict) -> StartTrainedModelInferenceJobResponse:
    out: StartTrainedModelInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("trainedModelInferenceJobArn") is not None:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        out["trained_model_inference_job_arn"] = ""
    return out
