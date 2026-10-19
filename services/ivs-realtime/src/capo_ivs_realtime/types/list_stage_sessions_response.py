"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStageSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.stage_session_list


class ListStageSessionsResponse(TypedDict, closed=True):
    stage_sessions: "capo_ivs_realtime.types.stage_session_list.StageSessionList"
    """<p>List of matching stage sessions.</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more stage sessions than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStageSessionsResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.stage_session_list

    out["stageSessions"] = capo_ivs_realtime.types.stage_session_list.serialize_json(
        value["stage_sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStageSessionsResponse:
    out: ListStageSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("stageSessions") is not None:
        import capo_ivs_realtime.types.stage_session_list

        out["stage_sessions"] = (
            capo_ivs_realtime.types.stage_session_list.deserialize_json(
                data["stageSessions"]
            )
        )
    else:
        out["stage_sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
