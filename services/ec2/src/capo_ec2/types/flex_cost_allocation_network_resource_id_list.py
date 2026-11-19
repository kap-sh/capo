"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationNetworkResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_network_resource_id

FlexCostAllocationNetworkResourceIdList: TypeAlias = list[
    "capo_ec2.types.flex_cost_allocation_network_resource_id.FlexCostAllocationNetworkResourceId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationNetworkResourceIdList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationNetworkResourceIdList:
    out: FlexCostAllocationNetworkResourceIdList = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FlexCostAllocationNetworkResourceIdList:
    out: FlexCostAllocationNetworkResourceIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
