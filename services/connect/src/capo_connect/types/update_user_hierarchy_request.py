"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserHierarchyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.instance_id
    import capo_connect.types.user_id


class UpdateUserHierarchyRequest(TypedDict, closed=True):
    hierarchy_group_id: NotRequired[
        "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user account.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserHierarchyRequest) -> dict:
    out: dict = {}
    if "hierarchy_group_id" in value:
        out["HierarchyGroupId"] = value["hierarchy_group_id"]
    return out


def deserialize_json(data: dict) -> UpdateUserHierarchyRequest:
    out: UpdateUserHierarchyRequest = {}  # type: ignore[typeddict-item]
    if data.get("HierarchyGroupId") is not None:
        out["hierarchy_group_id"] = data["HierarchyGroupId"]
    return out
