"""Generated from Smithy shape ``com.amazonaws.chime#BatchCreateRoomMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.membership_item_list
    import capo_chime.types.non_empty_string


class BatchCreateRoomMembershipRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    membership_item_list: "capo_chime.types.membership_item_list.MembershipItemList"
    """<p>The list of membership items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRoomMembershipRequest) -> dict:
    out: dict = {}
    import capo_chime.types.membership_item_list

    out["MembershipItemList"] = capo_chime.types.membership_item_list.serialize_json(
        value["membership_item_list"]
    )
    return out


def deserialize_json(data: dict) -> BatchCreateRoomMembershipRequest:
    out: BatchCreateRoomMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("MembershipItemList") is not None:
        import capo_chime.types.membership_item_list

        out["membership_item_list"] = (
            capo_chime.types.membership_item_list.deserialize_json(
                data["MembershipItemList"]
            )
        )
    else:
        out["membership_item_list"] = []
    return out
