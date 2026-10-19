"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationTrainedModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_trained_model_list
    import capo_cleanroomsml.types.next_token


class ListCollaborationTrainedModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_trained_models: "capo_cleanroomsml.types.collaboration_trained_model_list.CollaborationTrainedModelList"
    """<p>The trained models in the collaboration that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationTrainedModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.collaboration_trained_model_list

    out["collaborationTrainedModels"] = (
        capo_cleanroomsml.types.collaboration_trained_model_list.serialize_json(
            value["collaboration_trained_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationTrainedModelsResponse:
    out: ListCollaborationTrainedModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationTrainedModels") is not None:
        import capo_cleanroomsml.types.collaboration_trained_model_list

        out["collaboration_trained_models"] = (
            capo_cleanroomsml.types.collaboration_trained_model_list.deserialize_json(
                data["collaborationTrainedModels"]
            )
        )
    else:
        out["collaboration_trained_models"] = []
    return out
