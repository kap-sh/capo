"""Generated from Smithy shape ``com.amazonaws.securityagent#GroupMetadata``."""

from typing_extensions import NotRequired, TypedDict


class GroupMetadata(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The display name of the group.</p>"""
    description: NotRequired["str"]
    """<p>The description of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupMetadata) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GroupMetadata:
    out: GroupMetadata = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
