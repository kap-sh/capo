"""Generated from Smithy shape ``com.amazonaws.ivschat#ListRoomsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.pagination_token
    import capo_ivschat.types.room_list


class ListRoomsResponse(TypedDict, closed=True):
    rooms: "capo_ivschat.types.room_list.RoomList"
    """<p>List of the matching rooms (summary information only).</p>"""
    next_token: NotRequired["capo_ivschat.types.pagination_token.PaginationToken"]
    """<p>If there are more rooms than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomsResponse) -> dict:
    out: dict = {}
    import capo_ivschat.types.room_list

    out["rooms"] = capo_ivschat.types.room_list.serialize_json(value["rooms"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoomsResponse:
    out: ListRoomsResponse = {}  # type: ignore[typeddict-item]
    if data.get("rooms") is not None:
        import capo_ivschat.types.room_list

        out["rooms"] = capo_ivschat.types.room_list.deserialize_json(data["rooms"])
    else:
        out["rooms"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
