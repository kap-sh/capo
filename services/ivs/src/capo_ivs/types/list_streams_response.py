"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.pagination_token
    import capo_ivs.types.stream_list


class ListStreamsResponse(TypedDict, closed=True):
    streams: "capo_ivs.types.stream_list.StreamList"
    """<p>List of streams.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more streams than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.stream_list

    out["streams"] = capo_ivs.types.stream_list.serialize_json(value["streams"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamsResponse:
    out: ListStreamsResponse = {}  # type: ignore[typeddict-item]
    if data.get("streams") is not None:
        import capo_ivs.types.stream_list

        out["streams"] = capo_ivs.types.stream_list.deserialize_json(data["streams"])
    else:
        out["streams"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
