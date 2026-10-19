"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.pagination_token
    import capo_ivs.types.stream_session_list


class ListStreamSessionsResponse(TypedDict, closed=True):
    stream_sessions: "capo_ivs.types.stream_session_list.StreamSessionList"
    """<p>List of stream sessions.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more streams than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamSessionsResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.stream_session_list

    out["streamSessions"] = capo_ivs.types.stream_session_list.serialize_json(
        value["stream_sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamSessionsResponse:
    out: ListStreamSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("streamSessions") is not None:
        import capo_ivs.types.stream_session_list

        out["stream_sessions"] = capo_ivs.types.stream_session_list.deserialize_json(
            data["streamSessions"]
        )
    else:
        out["stream_sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
