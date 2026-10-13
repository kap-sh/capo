"""Generated from Smithy shape ``com.amazonaws.chime#RoomMembership``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.iso8601_timestamp
    import capo_chime.types.member
    import capo_chime.types.non_empty_string
    import capo_chime.types.room_membership_role


class RoomMembership(TypedDict, closed=True):
    room_id: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The room ID.</p>"""
    member: NotRequired["capo_chime.types.member.Member"]
    """<p>The member details, such as email address, name, member ID, and member type.</p>"""
    role: NotRequired["capo_chime.types.room_membership_role.RoomMembershipRole"]
    """<p>The membership role.</p>"""
    invited_by: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the user that invited the room member.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The room membership update timestamp, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoomMembership) -> dict:
    out: dict = {}
    if "room_id" in value:
        out["RoomId"] = value["room_id"]
    if "member" in value:
        import capo_chime.types.member

        out["Member"] = capo_chime.types.member.serialize_json(value["member"])
    if "role" in value:
        import capo_chime.types.room_membership_role

        out["Role"] = capo_chime.types.room_membership_role.serialize_json(
            value["role"]
        )
    if "invited_by" in value:
        out["InvitedBy"] = value["invited_by"]
    if "updated_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["UpdatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> RoomMembership:
    out: RoomMembership = {}  # type: ignore[typeddict-item]
    if data.get("RoomId") is not None:
        out["room_id"] = data["RoomId"]
    if data.get("Member") is not None:
        import capo_chime.types.member

        out["member"] = capo_chime.types.member.deserialize_json(data["Member"])
    if data.get("Role") is not None:
        import capo_chime.types.room_membership_role

        out["role"] = capo_chime.types.room_membership_role.deserialize_json(
            data["Role"]
        )
    if data.get("InvitedBy") is not None:
        out["invited_by"] = data["InvitedBy"]
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["updated_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["UpdatedTimestamp"]
        )
    return out


def redact_sensitive(value: RoomMembership) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "member" in value:
        import capo_chime.types.member

        out["member"] = capo_chime.types.member.redact_sensitive(value["member"])
    return out
