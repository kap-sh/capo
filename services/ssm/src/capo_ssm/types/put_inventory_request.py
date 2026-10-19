"""Generated from Smithy shape ``com.amazonaws.ssm#PutInventoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_id
    import capo_ssm.types.inventory_item_list


class PutInventoryRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>An managed node ID where you want to add or update inventory items.</p>"""
    items: "capo_ssm.types.inventory_item_list.InventoryItemList"
    """<p>The inventory items that you want to add or update on managed nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInventoryRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import capo_ssm.types.inventory_item_list

    out["Items"] = capo_ssm.types.inventory_item_list.serialize_aws_json_1_1(
        value["items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInventoryRequest:
    out: PutInventoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("Items") is not None:
        import capo_ssm.types.inventory_item_list

        out["items"] = capo_ssm.types.inventory_item_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    else:
        out["items"] = []
    return out
