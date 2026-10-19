"""Generated from Smithy shape ``com.amazonaws.machinelearning#UpdateBatchPredictionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name


class UpdateBatchPredictionInput(TypedDict, closed=True):
    batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The ID assigned to the <code>BatchPrediction</code> during creation.</p>"""
    batch_prediction_name: "capo_machine_learning.types.entity_name.EntityName"
    """<p>A new user-supplied name or description of the <code>BatchPrediction</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBatchPredictionInput) -> dict:
    out: dict = {}
    out["BatchPredictionId"] = value["batch_prediction_id"]
    out["BatchPredictionName"] = value["batch_prediction_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBatchPredictionInput:
    out: UpdateBatchPredictionInput = {}  # type: ignore[typeddict-item]
    if data.get("BatchPredictionId") is not None:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    else:
        out["batch_prediction_id"] = ""
    if data.get("BatchPredictionName") is not None:
        out["batch_prediction_name"] = data["BatchPredictionName"]
    else:
        out["batch_prediction_name"] = ""
    return out
