"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListMLInputChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.ml_input_channels_list
    import capo_cleanroomsml.types.next_token


class ListMLInputChannelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    ml_input_channels_list: (
        "capo_cleanroomsml.types.ml_input_channels_list.MLInputChannelsList"
    )
    """<p>The list of ML input channels that you wanted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMLInputChannelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.ml_input_channels_list

    out["mlInputChannelsList"] = (
        capo_cleanroomsml.types.ml_input_channels_list.serialize_json(
            value["ml_input_channels_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMLInputChannelsResponse:
    out: ListMLInputChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("mlInputChannelsList") is not None:
        import capo_cleanroomsml.types.ml_input_channels_list

        out["ml_input_channels_list"] = (
            capo_cleanroomsml.types.ml_input_channels_list.deserialize_json(
                data["mlInputChannelsList"]
            )
        )
    else:
        out["ml_input_channels_list"] = []
    return out
