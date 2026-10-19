"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.pagination_token
    import capo_ivs.types.stream_key_list


class ListStreamKeysResponse(TypedDict, closed=True):
    stream_keys: "capo_ivs.types.stream_key_list.StreamKeyList"
    """<p>List of stream keys.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more stream keys than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamKeysResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.stream_key_list

    out["streamKeys"] = capo_ivs.types.stream_key_list.serialize_json(
        value["stream_keys"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamKeysResponse:
    out: ListStreamKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("streamKeys") is not None:
        import capo_ivs.types.stream_key_list

        out["stream_keys"] = capo_ivs.types.stream_key_list.deserialize_json(
            data["streamKeys"]
        )
    else:
        out["stream_keys"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
