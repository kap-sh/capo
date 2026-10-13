"""Generated from Smithy shape ``com.amazonaws.chime#ListRoomsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.room_list
    import capo_chime.types.string


class ListRoomsResponse(TypedDict, closed=True):
    rooms: NotRequired["capo_chime.types.room_list.RoomList"]
    """<p>The room details.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomsResponse) -> dict:
    out: dict = {}
    if "rooms" in value:
        import capo_chime.types.room_list

        out["Rooms"] = capo_chime.types.room_list.serialize_json(value["rooms"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoomsResponse:
    out: ListRoomsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Rooms") is not None:
        import capo_chime.types.room_list

        out["rooms"] = capo_chime.types.room_list.deserialize_json(data["Rooms"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRoomsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rooms" in value:
        import capo_chime.types.room_list

        out["rooms"] = capo_chime.types.room_list.redact_sensitive(value["rooms"])
    return out
