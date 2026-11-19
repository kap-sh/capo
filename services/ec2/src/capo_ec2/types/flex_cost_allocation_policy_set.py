"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationPolicySet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.flex_cost_allocation_policy_description

FlexCostAllocationPolicySet: TypeAlias = list[
    "capo_ec2.types.flex_cost_allocation_policy_description.FlexCostAllocationPolicyDescription"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FlexCostAllocationPolicySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.flex_cost_allocation_policy_description

        capo_ec2.types.flex_cost_allocation_policy_description.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> FlexCostAllocationPolicySet:
    import capo_ec2.types.flex_cost_allocation_policy_description

    out: FlexCostAllocationPolicySet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.flex_cost_allocation_policy_description.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> FlexCostAllocationPolicySet:
    import capo_ec2.types.flex_cost_allocation_policy_description

    out: FlexCostAllocationPolicySet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.flex_cost_allocation_policy_description.deserialize_ec2_query(
                child
            )
        )
    return out
