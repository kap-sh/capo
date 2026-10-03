"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserHierarchyGroupNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.hierarchy_group_name
    import capo_connect.types.instance_id


class UpdateUserHierarchyGroupNameRequest(TypedDict, closed=True):
    name: "capo_connect.types.hierarchy_group_name.HierarchyGroupName"
    """<p>The name of the hierarchy group. Must not be more than 100 characters.</p>"""
    hierarchy_group_id: "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    """<p>The identifier of the hierarchy group.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserHierarchyGroupNameRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateUserHierarchyGroupNameRequest:
    out: UpdateUserHierarchyGroupNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateUserHierarchyGroupNameRequest.name required")
    return out
