"""Generated from Smithy shape ``com.amazonaws.ec2#FlexCostAllocationAssociationMode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

"""<p>The mode of a policy association. Valid values:</p> <ul> <li> <p> <code>direct</code> - The policy is associated with specific resources by resource ID.</p> </li> <li> <p> <code>scope</code> - The policy is associated with a scope of resources.</p> </li> </ul>"""
FlexCostAllocationAssociationMode: TypeAlias = Literal[
    "direct",
    "scope",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: FlexCostAllocationAssociationMode) -> str:
    return value


def from_ec2_query_text(text: str) -> FlexCostAllocationAssociationMode:
    return cast(FlexCostAllocationAssociationMode, text)


def serialize_ec2_query(
    value: FlexCostAllocationAssociationMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FlexCostAllocationAssociationMode:
    return from_ec2_query_text(el.text or "")
