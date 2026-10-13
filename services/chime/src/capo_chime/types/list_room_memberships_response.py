"""Generated from Smithy shape ``com.amazonaws.chime#ListRoomMembershipsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.room_membership_list
    import capo_chime.types.string


class ListRoomMembershipsResponse(TypedDict, closed=True):
    room_memberships: NotRequired[
        "capo_chime.types.room_membership_list.RoomMembershipList"
    ]
    """<p>The room membership details.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomMembershipsResponse) -> dict:
    out: dict = {}
    if "room_memberships" in value:
        import capo_chime.types.room_membership_list

        out["RoomMemberships"] = capo_chime.types.room_membership_list.serialize_json(
            value["room_memberships"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRoomMembershipsResponse:
    out: ListRoomMembershipsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RoomMemberships") is not None:
        import capo_chime.types.room_membership_list

        out["room_memberships"] = (
            capo_chime.types.room_membership_list.deserialize_json(
                data["RoomMemberships"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRoomMembershipsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "room_memberships" in value:
        import capo_chime.types.room_membership_list

        out["room_memberships"] = (
            capo_chime.types.room_membership_list.redact_sensitive(
                value["room_memberships"]
            )
        )
    return out
