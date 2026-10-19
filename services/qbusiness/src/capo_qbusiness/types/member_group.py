"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.group_name
    import capo_qbusiness.types.membership_type


class MemberGroup(TypedDict, closed=True):
    group_name: "capo_qbusiness.types.group_name.GroupName"
    """<p>The name of the sub group.</p>"""
    type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the sub group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberGroup) -> dict:
    out: dict = {}
    out["groupName"] = value["group_name"]
    if "type" in value:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> MemberGroup:
    out: MemberGroup = {}  # type: ignore[typeddict-item]
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    else:
        out["group_name"] = ""
    if data.get("type") is not None:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
