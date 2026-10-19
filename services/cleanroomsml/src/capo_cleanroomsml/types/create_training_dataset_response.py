"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateTrainingDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.training_dataset_arn


class CreateTrainingDatasetResponse(TypedDict, closed=True):
    training_dataset_arn: (
        "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrainingDatasetResponse) -> dict:
    out: dict = {}
    out["trainingDatasetArn"] = value["training_dataset_arn"]
    return out


def deserialize_json(data: dict) -> CreateTrainingDatasetResponse:
    out: CreateTrainingDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("trainingDatasetArn") is not None:
        out["training_dataset_arn"] = data["trainingDatasetArn"]
    else:
        out["training_dataset_arn"] = ""
    return out
