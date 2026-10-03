"""Generated from Smithy shape ``com.amazonaws.connect#CreateUserHierarchyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.hierarchy_group_name
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map


class CreateUserHierarchyGroupRequest(TypedDict, closed=True):
    name: "capo_connect.types.hierarchy_group_name.HierarchyGroupName"
    """<p>The name of the user hierarchy group. Must not be more than 100 characters.</p>"""
    parent_group_id: NotRequired[
        "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier for the parent hierarchy group. The user hierarchy is created at level one if the parent group ID is null.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserHierarchyGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "parent_group_id" in value:
        out["ParentGroupId"] = value["parent_group_id"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateUserHierarchyGroupRequest:
    out: CreateUserHierarchyGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateUserHierarchyGroupRequest.name required")
    if data.get("ParentGroupId") is not None:
        out["parent_group_id"] = data["ParentGroupId"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
