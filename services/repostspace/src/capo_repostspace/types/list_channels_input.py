"""Generated from Smithy shape ``com.amazonaws.repostspace#ListChannelsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.list_channels_limit
    import capo_repostspace.types.space_id


class ListChannelsInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of channel to return. You receive this token from a previous ListChannels operation.</p>"""
    max_results: NotRequired[
        "capo_repostspace.types.list_channels_limit.ListChannelsLimit"
    ]
    """<p>The maximum number of channels to include in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsInput:
    out: ListChannelsInput = {}  # type: ignore[typeddict-item]
    return out
