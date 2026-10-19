"""Generated from Smithy shape ``com.amazonaws.datazone#GroupDetails``."""

from typing_extensions import TypedDict


class GroupDetails(TypedDict, closed=True):
    group_id: "str"
    """<p>The identifier of the group in Amazon DataZone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupDetails) -> dict:
    out: dict = {}
    out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> GroupDetails:
    out: GroupDetails = {}  # type: ignore[typeddict-item]
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    else:
        out["group_id"] = ""
    return out
