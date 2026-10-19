"""Generated from Smithy shape ``com.amazonaws.synthetics#CreateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.group_name
    import capo_synthetics.types.tag_map


class CreateGroupRequest(TypedDict, closed=True):
    name: "capo_synthetics.types.group_name.GroupName"
    """<p>The name for the group. It can include any Unicode characters.</p> <p>The names for all groups in your account, across all Regions, must be unique.</p>"""
    tags: NotRequired["capo_synthetics.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to associate with the group. You can associate as many as 50 tags with a group.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_synthetics.types.tag_map

        out["Tags"] = capo_synthetics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Tags") is not None:
        import capo_synthetics.types.tag_map

        out["tags"] = capo_synthetics.types.tag_map.deserialize_json(data["Tags"])
    return out
