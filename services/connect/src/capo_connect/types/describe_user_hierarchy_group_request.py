"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserHierarchyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_id
    import capo_connect.types.instance_id


class DescribeUserHierarchyGroupRequest(TypedDict, closed=True):
    hierarchy_group_id: "capo_connect.types.hierarchy_group_id.HierarchyGroupId"
    """<p>The identifier of the hierarchy group.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserHierarchyGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeUserHierarchyGroupRequest:
    out: DescribeUserHierarchyGroupRequest = {}  # type: ignore[typeddict-item]
    return out
