"""Generated from Smithy shape ``com.amazonaws.outposts#InstanceTypeCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.instance_type_count
    import capo_outposts.types.instance_type_name


class InstanceTypeCapacity(TypedDict, closed=True):
    instance_type: "capo_outposts.types.instance_type_name.InstanceTypeName"
    """<p>The instance type of the hosts.</p>"""
    count: "capo_outposts.types.instance_type_count.InstanceTypeCount"
    """<p>The number of instances for the specified instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeCapacity) -> dict:
    out: dict = {}
    out["InstanceType"] = value["instance_type"]
    out["Count"] = value.get("count", 0)
    return out


def deserialize_json(data: dict) -> InstanceTypeCapacity:
    out: InstanceTypeCapacity = {}  # type: ignore[typeddict-item]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    else:
        out["instance_type"] = ""
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    return out
