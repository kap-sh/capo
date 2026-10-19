"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTrainedModelVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.trained_model_list


class ListTrainedModelVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The pagination token to use in a subsequent <code>ListTrainedModelVersions</code> request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    trained_models: "capo_cleanroomsml.types.trained_model_list.TrainedModelList"
    """<p>A list of trained model versions that match the specified criteria. Each entry contains summary information about a trained model version, including its version identifier, status, and creation details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrainedModelVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.trained_model_list

    out["trainedModels"] = capo_cleanroomsml.types.trained_model_list.serialize_json(
        value["trained_models"]
    )
    return out


def deserialize_json(data: dict) -> ListTrainedModelVersionsResponse:
    out: ListTrainedModelVersionsResponse = {}  # type: ignore[typeddict-item]
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
