"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainingDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.training_dataset_list


class ListTrainingDatasetsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    training_datasets: (
        "capo_cleanroomsml.types.training_dataset_list.TrainingDatasetList"
    )
    """<p>The training datasets that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainingDatasetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.training_dataset_list

    out["trainingDatasets"] = (
        capo_cleanroomsml.types.training_dataset_list.serialize_json(
            value["training_datasets"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTrainingDatasetsResponse:
    out: ListTrainingDatasetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("trainingDatasets") is not None:
        import capo_cleanroomsml.types.training_dataset_list

        out["training_datasets"] = (
            capo_cleanroomsml.types.training_dataset_list.deserialize_json(
                data["trainingDatasets"]
            )
        )
    else:
        out["training_datasets"] = []
    return out
