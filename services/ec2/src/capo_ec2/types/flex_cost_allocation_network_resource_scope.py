"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationNetworkResourceScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_network_resource_scope_id_list
    import capo_ec2.types.flex_cost_allocation_network_resource_scope_type


class FlexCostAllocationNetworkResourceScope(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_ec2.types.flex_cost_allocation_network_resource_scope_type.FlexCostAllocationNetworkResourceScopeType"
    ]
    """<p>The type of scope. This parameter is required. Valid values are <code>account</code>, <code>vpc</code>, and <code>subnet</code>.</p>"""
    resource_ids: NotRequired[
        "capo_ec2.types.flex_cost_allocation_network_resource_scope_id_list.FlexCostAllocationNetworkResourceScopeIdList"
    ]
    """<p>The IDs of the resources owned by you that define the scope. You can specify from 1 to 20 IDs. This parameter is required.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationNetworkResourceScope,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_type" in value:
        import capo_ec2.types.flex_cost_allocation_network_resource_scope_type

        capo_ec2.types.flex_cost_allocation_network_resource_scope_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "resource_ids" in value:
        import capo_ec2.types.flex_cost_allocation_network_resource_scope_id_list

        capo_ec2.types.flex_cost_allocation_network_resource_scope_id_list.serialize_ec2_query(
            value["resource_ids"], pairs, f"{key_prefix}ResourceIds"
        )


def deserialize_ec2_query(el: Element) -> FlexCostAllocationNetworkResourceScope:
    out: FlexCostAllocationNetworkResourceScope = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.flex_cost_allocation_network_resource_scope_type

        out["resource_type"] = (
            capo_ec2.types.flex_cost_allocation_network_resource_scope_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_resource_ids = el.find("ResourceIds")
    if child_resource_ids is not None:
        import capo_ec2.types.flex_cost_allocation_network_resource_scope_id_list

        out["resource_ids"] = (
            capo_ec2.types.flex_cost_allocation_network_resource_scope_id_list.deserialize_ec2_query(
                child_resource_ids
            )
        )
    return out
