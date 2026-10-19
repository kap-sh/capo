"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_source_user_id
    import capo_qbusiness.types.membership_type


class MemberUser(TypedDict, closed=True):
    user_id: "capo_qbusiness.types.data_source_user_id.DataSourceUserId"
    """<p>The identifier of the user you want to map to a group.</p>"""
    type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberUser) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "type" in value:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> MemberUser:
    out: MemberUser = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("type") is not None:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
