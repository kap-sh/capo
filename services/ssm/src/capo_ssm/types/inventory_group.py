"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_filter_list
    import capo_ssm.types.inventory_group_name


class InventoryGroup(TypedDict, closed=True):
    name: "capo_ssm.types.inventory_group_name.InventoryGroupName"
    """<p>The name of the group.</p>"""
    filters: "capo_ssm.types.inventory_filter_list.InventoryFilterList"
    """<p>Filters define the criteria for the group. The <code>matchingCount</code> field displays the number of resources that match the criteria. The <code>notMatchingCount</code> field displays the number of resources that don't match the criteria. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_ssm.types.inventory_filter_list

    out["Filters"] = capo_ssm.types.inventory_filter_list.serialize_aws_json_1_1(
        value["filters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryGroup:
    out: InventoryGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Filters") is not None:
        import capo_ssm.types.inventory_filter_list

        out["filters"] = capo_ssm.types.inventory_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        out["filters"] = []
    return out
