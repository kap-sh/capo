"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListCollaborationMLInputChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_ml_input_channels_list
    import capo_cleanroomsml.types.next_token


class ListCollaborationMLInputChannelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    collaboration_ml_input_channels_list: "capo_cleanroomsml.types.collaboration_ml_input_channels_list.CollaborationMLInputChannelsList"
    """<p>The list of ML input channels that you wanted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationMLInputChannelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.collaboration_ml_input_channels_list

    out["collaborationMLInputChannelsList"] = (
        capo_cleanroomsml.types.collaboration_ml_input_channels_list.serialize_json(
            value["collaboration_ml_input_channels_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationMLInputChannelsResponse:
    out: ListCollaborationMLInputChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationMLInputChannelsList") is not None:
        import capo_cleanroomsml.types.collaboration_ml_input_channels_list

        out["collaboration_ml_input_channels_list"] = (
            capo_cleanroomsml.types.collaboration_ml_input_channels_list.deserialize_json(
                data["collaborationMLInputChannelsList"]
            )
        )
    else:
        out["collaboration_ml_input_channels_list"] = []
    return out
