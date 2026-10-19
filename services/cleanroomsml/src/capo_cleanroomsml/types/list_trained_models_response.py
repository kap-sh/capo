"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainedModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.trained_model_list


class ListTrainedModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    trained_models: "capo_cleanroomsml.types.trained_model_list.TrainedModelList"
    """<p>The list of trained models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainedModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.trained_model_list

    out["trainedModels"] = capo_cleanroomsml.types.trained_model_list.serialize_json(
        value["trained_models"]
    )
    return out


def deserialize_json(data: dict) -> ListTrainedModelsResponse:
    out: ListTrainedModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("trainedModels") is not None:
        import capo_cleanroomsml.types.trained_model_list

        out["trained_models"] = (
            capo_cleanroomsml.types.trained_model_list.deserialize_json(
                data["trainedModels"]
            )
        )
    else:
        out["trained_models"] = []
    return out
