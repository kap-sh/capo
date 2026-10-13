"""Generated from Smithy shape ``com.amazonaws.chime#CreateRoomResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.room


class CreateRoomResponse(TypedDict, closed=True):
    room: NotRequired["capo_chime.types.room.Room"]
    """<p>The room details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomResponse) -> dict:
    out: dict = {}
    if "room" in value:
        import capo_chime.types.room

        out["Room"] = capo_chime.types.room.serialize_json(value["room"])
    return out


def deserialize_json(data: dict) -> CreateRoomResponse:
    out: CreateRoomResponse = {}  # type: ignore[typeddict-item]
    if data.get("Room") is not None:
        import capo_chime.types.room

        out["room"] = capo_chime.types.room.deserialize_json(data["Room"])
    return out


def redact_sensitive(value: CreateRoomResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "room" in value:
        import capo_chime.types.room

        out["room"] = capo_chime.types.room.redact_sensitive(value["room"])
    return out
