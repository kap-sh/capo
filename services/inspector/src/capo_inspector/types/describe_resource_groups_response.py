"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeResourceGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.failed_items
    import capo_inspector.types.resource_group_list


class DescribeResourceGroupsResponse(TypedDict, closed=True):
    resource_groups: "capo_inspector.types.resource_group_list.ResourceGroupList"
    """<p>Information about a resource group.</p>"""
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Resource group details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceGroupsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.resource_group_list

    out["resourceGroups"] = (
        capo_inspector.types.resource_group_list.serialize_aws_json_1_1(
            value["resource_groups"]
        )
    )
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceGroupsResponse:
    out: DescribeResourceGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceGroups") is not None:
        import capo_inspector.types.resource_group_list

        out["resource_groups"] = (
            capo_inspector.types.resource_group_list.deserialize_aws_json_1_1(
                data["resourceGroups"]
            )
        )
    else:
        out["resource_groups"] = []
    if data.get("failedItems") is not None:
        import capo_inspector.types.failed_items

        out["failed_items"] = (
            capo_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        out["failed_items"] = {}
    return out
