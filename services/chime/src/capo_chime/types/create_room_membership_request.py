"""Generated from Smithy shape ``com.amazonaws.chime#CreateRoomMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.room_membership_role


class CreateRoomMembershipRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    member_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime member ID (user ID or bot ID).</p>"""
    role: NotRequired["capo_chime.types.room_membership_role.RoomMembershipRole"]
    """<p>The role of the member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomMembershipRequest) -> dict:
    out: dict = {}
    out["MemberId"] = value["member_id"]
    if "role" in value:
        import capo_chime.types.room_membership_role

        out["Role"] = capo_chime.types.room_membership_role.serialize_json(
            value["role"]
        )
    return out


def deserialize_json(data: dict) -> CreateRoomMembershipRequest:
    out: CreateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("MemberId") is not None:
        out["member_id"] = data["MemberId"]
    else:
        out["member_id"] = ""
    if data.get("Role") is not None:
        import capo_chime.types.room_membership_role

        out["role"] = capo_chime.types.room_membership_role.deserialize_json(
            data["Role"]
        )
    return out
