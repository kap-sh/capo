"""Generated from Smithy shape ``com.amazonaws.outposts#AssetInstanceTypeCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.instance_type_count
    import capo_outposts.types.instance_type_name


class AssetInstanceTypeCapacity(TypedDict, closed=True):
    instance_type: "capo_outposts.types.instance_type_name.InstanceTypeName"
    """<p>The type of instance.</p>"""
    count: "capo_outposts.types.instance_type_count.InstanceTypeCount"
    """<p>The number of each instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetInstanceTypeCapacity) -> dict:
    out: dict = {}
    out["InstanceType"] = value["instance_type"]
    out["Count"] = value.get("count", 0)
    return out


def deserialize_json(data: dict) -> AssetInstanceTypeCapacity:
    out: AssetInstanceTypeCapacity = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    else:
        out["instance_type"] = ""
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
