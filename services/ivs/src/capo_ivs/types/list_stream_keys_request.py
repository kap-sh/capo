"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.max_stream_key_results
    import capo_ivs.types.pagination_token


class ListStreamKeysRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>Channel ARN used to filter the list.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>The first stream key to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs.types.max_stream_key_results.MaxStreamKeyResults"
    ]
    """<p>Maximum number of streamKeys to return. Default: 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamKeysRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListStreamKeysRequest:
    out: ListStreamKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        out["channel_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
