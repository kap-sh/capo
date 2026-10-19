"""Generated from Smithy shape ``com.amazonaws.machinelearning#DeleteBatchPredictionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id


class DeleteBatchPredictionInput(TypedDict, closed=True):
    batch_prediction_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>BatchPrediction</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBatchPredictionInput) -> dict:
    out: dict = {}
    out["BatchPredictionId"] = value["batch_prediction_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBatchPredictionInput:
    out: DeleteBatchPredictionInput = {}  # type: ignore[typeddict-item]
    if data.get("BatchPredictionId") is not None:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    else:
        out["batch_prediction_id"] = ""
    return out
