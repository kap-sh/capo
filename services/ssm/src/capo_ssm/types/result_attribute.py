"""Generated from Smithy shape ``com.amazonaws.ssm#ResultAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_item_type_name


class ResultAttribute(TypedDict, closed=True):
    type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName"
    """<p>Name of the inventory item type. Valid value: <code>AWS:InstanceInformation</code>. Default Value: <code>AWS:InstanceInformation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultAttribute) -> dict:
    out: dict = {}
    out["TypeName"] = value["type_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultAttribute:
    out: ResultAttribute = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    else:
        out["type_name"] = ""
    return out
