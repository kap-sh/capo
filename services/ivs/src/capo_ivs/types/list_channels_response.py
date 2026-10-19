"""Generated from Smithy shape ``com.amazonaws.ivs#ListChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_list
    import capo_ivs.types.pagination_token


class ListChannelsResponse(TypedDict, closed=True):
    channels: "capo_ivs.types.channel_list.ChannelList"
    """<p>List of the matching channels.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more channels than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.channel_list

    out["channels"] = capo_ivs.types.channel_list.serialize_json(value["channels"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("channels") is not None:
        import capo_ivs.types.channel_list

        out["channels"] = capo_ivs.types.channel_list.deserialize_json(data["channels"])
    else:
        out["channels"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
